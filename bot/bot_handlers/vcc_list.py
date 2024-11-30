import json

from aiogram import Dispatcher
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from client.models import MeetingBare
from presenters.date import present_date, format_duration
from presenters.message import get_error_message
from services.auth import Auth, TokenData
from services.data_saver import ContextSaver
from services.meetings_client import MeetingsClient, dict_to_model

auth = Auth()
saver = ContextSaver()
meet_client = MeetingsClient()


def present_vcc_msg(
        page: int,
        total: int,
        meeting: MeetingBare,
        meeting_more: dict,
) -> str:
    msg_parts = [
        f"Встреча <i>{page}</i> из {total}.",
        "",
        f"<u>Название:</u> {meeting.name}",
        f"<u>Дата и время:</u> {present_date(meeting.started_at, meeting.ended_at)}",
        f"<u>Продолжительность:</u> {format_duration(meeting.duration) if meeting.duration else 'Не указана'}",
        f"<u>Платформа:</u> {meeting_more.get('backend', 'Внешняя платформа')}",
        ""
    ]

    participant_list = []
    for participant in meeting_more.get('participants', []):
        full_name = " ".join(filter(lambda i: i, [
            participant.get('lastName'),
            participant.get('firstName'),
            participant.get('middleName'),
        ]))

        approved_text = "✅" if participant.get("isApproved") else "❌"
        participant_text = f"{full_name} {approved_text}"
        if "email" in participant:
            participant_text = f"<a href='mailto:{participant.get('email')}'>{full_name}</a> {approved_text}"

        participant_list.append(participant_text)

    if participant_list:
        msg_parts.append(f"<u>Участники:</u>")
        msg_parts.extend(participant_list)

    return "\n".join(msg_parts)


def need_ics(token: TokenData, meeting_more: dict) -> bool:
    for participant in meeting_more.get('participants', []):
        if participant.get("id", -1) == token.user.id:
            return True

    if meeting_more.get("createdUser", {}).get("id", -1) == token.user.id:
        return True

    if meeting_more.get("organizedUser", {}).get("id", -1) == token.user.id:
        return True


def present_vcc_buttons(
        key: str,
        token: TokenData,
        page: int,
        total: int,
        meeting: MeetingBare,
        meeting_more: dict,
) -> InlineKeyboardMarkup:
    buttons_row_1 = []
    if need_ics(token, meeting_more):
        buttons_row_1.append(InlineKeyboardButton(text="Добавить в календарь", callback_data=f"get_ics:{meeting.id}"))

    if "organizerPermalink" in meeting_more:
        buttons_row_1.append(InlineKeyboardButton(text="Ссылка", url=meeting_more.get("organizerPermalink")))
    elif "permalink" in meeting_more:
        buttons_row_1.append(InlineKeyboardButton(text="Ссылка", url=meeting_more.get("permalink")))

    buttons_row_2 = []
    if page > 1:
        buttons_row_2.append(InlineKeyboardButton(text="⬅️", callback_data=f"show_meet:{page - 1}:{key}"))

    if page < total:
        buttons_row_2.append(InlineKeyboardButton(text="➡️", callback_data=f"show_meet:{page + 1}:{key}"))

    return InlineKeyboardMarkup(inline_keyboard=[
        buttons_row_1,
        buttons_row_2
    ])


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

    data_dict = dict(json.loads(data))
    data_dict["page"] = page

    try:
        meetings, meeting_more = await meet_client.get_meeting_by_filter(token, dict_to_model(data_dict))
    except Exception as e:
        await callback.answer(get_error_message())
        return

    rows = meetings.rows_number

    if not rows or not meeting_more:
        await callback.message.edit_text(
            "Вы достигли конца списка",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data=f"show_meet:{max(page - 1, 1)}:{key}")],
            ])
        )
        return

    total = meetings.rows_number
    meeting = meetings.data[0]

    msg = present_vcc_msg(page, total, meeting, meeting_more.to_dict())
    markup = present_vcc_buttons(key, token, page, total, meeting, meeting_more.to_dict())

    await callback.message.edit_text(msg, reply_markup=markup, parse_mode="HTML")


def register_vcc_list_handlers(dp: Dispatcher):
    dp.callback_query.register(show_meetings, lambda c: str(c.data).startswith("show_meet:"))
