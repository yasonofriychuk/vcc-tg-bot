import json
from datetime import datetime

from aiogram import Dispatcher
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

from client import AuthenticatedClient
from client.models import MeetingSortingFields
from client.types import Response
from config import API_BASE_URL, WEB_BASE_URL
from presenters.date import present_date, format_duration
from presenters.message import get_error_message, get_vks_error_message
from services.auth import Auth
from client.api.meetings import get_meetings_meetings_get
from client.models.meeting_list import MeetingList
from services.data_saver import ContextSaver

auth = Auth()
saver = ContextSaver()


async def show_meetings(callback: CallbackQuery):
    page, key = callback.data.removeprefix("show_meet:").split(":", 1)

    user_id = callback.message.chat.id
    page = int(page)

    token = await auth.get_token(user_id)
    data = await saver.get_data(user_id, key)
    if not data or not token:
        await callback.message.edit_text(text=f"Данные устарели")
        await callback.answer()
        return

    data_json = dict(json.loads(data))

    from_datetime = datetime.fromisoformat(data_json.get("from_datetime"))
    to_datetime = datetime.fromisoformat(data_json.get("to_datetime"))

    client = AuthenticatedClient(base_url=API_BASE_URL, verify_ssl=False, token=token.original_token)

    try:
        async with client as client:
            response_meetings: Response[MeetingList] = await get_meetings_meetings_get.asyncio_detailed(
                client=client,
                from_datetime=from_datetime,
                to_datetime=to_datetime,
                sort_by=MeetingSortingFields.STARTEDAT,
                rows_per_page=1,
                page=page
            )
    except Exception as e:
        await callback.answer(get_error_message())
        return

    if not response_meetings or response_meetings.status_code != 200:
        await callback.answer(get_vks_error_message())
        return

    if not response_meetings.parsed.data:
        await callback.message.edit_text(
            "Вы достигли конца списка",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data=f"show_meet:{max(page-1, 1)}:{key}")],
            ])
        )
        return

    meeting = response_meetings.parsed.data[0]
    total = response_meetings.parsed.rows_number

    msg_parts = [
        f"Встреча <i>{page}</i> из {total}.",
        "",
        f"<u>Название:</u> {meeting.name}",
        f"<u>Дата и время:</u> {present_date(meeting.started_at, meeting.ended_at)}",
        f"<u>Продолжительность:</u> {format_duration(meeting.duration)}",
        f"<u>Участников:</u> {meeting.participants_count}",
    ]

    buttons = []
    if page > 1:
        buttons.append(InlineKeyboardButton(text="⬅️", callback_data=f"show_meet:{page-1}:{key}"))

    if page < total:
        buttons.append(InlineKeyboardButton(text="➡️", callback_data=f"show_meet:{page+1}:{key}"))

    detail_button = InlineKeyboardButton(text="Подробнее", web_app=WebAppInfo(
        url=f"{WEB_BASE_URL}/static/vcc-detail.html?meeting={meeting.id}"
    ))

    await callback.message.edit_text("\n".join(msg_parts), reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [detail_button],
        buttons
    ]), parse_mode="HTML")


def register_vcc_list_handlers(dp: Dispatcher):
    dp.callback_query.register(show_meetings, lambda c: str(c.data).startswith("show_meet:"))
