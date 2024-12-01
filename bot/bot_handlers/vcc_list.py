import json

from aiogram import Dispatcher
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from presenters.message import get_error_message
from presenters.vcs_list_presenter import present_vcc_msg, present_vcc_buttons
from services.auth import Auth
from services.data_saver import ContextSaver
from services.meetings_client import MeetingsClient, dict_to_model

auth = Auth()
saver = ContextSaver()
meet_client = MeetingsClient()


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
    await callback.answer()

    try:
        await callback.message.edit_text(msg, reply_markup=markup, parse_mode="HTML")
    except Exception as e:
        pass  # No modify content


def register_vcc_list_handlers(dp: Dispatcher):
    dp.callback_query.register(show_meetings, lambda c: str(c.data).startswith("show_meet:"))
