import httpx
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, BufferedInputFile
from config import API_BASE_URL
from presenters.message import get_error_message, get_vks_error_message, get_ics_not_found
from services.auth import Auth

auth = Auth()


async def get_ics(callback: CallbackQuery):
    token = await auth.get_token(callback.message.chat.id)
    if not token:
        await callback.message.edit_text(text=f"Данные устарели")
        await callback.answer()
        return

    meet_id = int(callback.data.removeprefix("get_ics:"))

    headers = {
        'Authorization': f'Bearer {token.original_token}',
        'Accept': 'application/json, plain, */*;'
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{API_BASE_URL}/meetings/{meet_id}/ics", headers=headers)

        if response.status_code == 200:
            ics_file = BufferedInputFile(response.content, filename="meeting.ics")
            await callback.message.answer_document(
                document=ics_file,
                caption="Вот ваше мероприятие в формате ICS. Вы можете добавить его в свой календарь."
            )
            return
        elif response.status_code == 404:
            await callback.answer(get_ics_not_found())
            return
        else:
            await callback.answer(get_vks_error_message())
            return

    except Exception as e:
        await callback.answer(get_error_message())


def register_ics_handlers(dp: Dispatcher):
    dp.callback_query.register(get_ics, lambda c: str(c.data).startswith("get_ics:"))
