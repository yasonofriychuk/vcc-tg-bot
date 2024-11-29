from datetime import datetime

from aiogram import types, Dispatcher
from aiogram.filters import Command

from client import AuthenticatedClient
from client.types import Response
from config import API_BASE_URL
from services.auth import Auth
from client.api.meetings import get_meetings_meetings_get
from client.models.meeting_list import MeetingList
from client.models.user_priority import UserPriority

auth = Auth()


async def vcc_list(message: types.Message):
    token = await auth.get_token(message.chat.id)
    if token is None:
        await message.answer(text="Нужно авторизоваться")
        return

    msg_part = message.text.split()
    if len(msg_part) != 3:
        await message.answer(text="Неверный формат команды")
        return

    try:
        date_from, date_to = datetime.strptime(msg_part[1], "%d-%m-%Y"), datetime.strptime(msg_part[2], "%d-%m-%Y")
    except:
        await message.answer(text="Нверный формат даты")
        return

    async with AuthenticatedClient(base_url=API_BASE_URL, verify_ssl=False, token=token.original_token) as client:
        response: Response[MeetingList] = await get_meetings_meetings_get.asyncio_detailed(
            client=client,
            from_datetime=date_from,
            to_datetime=date_to,
            priority=UserPriority.VALUE_1
        )

    await message.answer(text=response.content.decode('utf-8')[:100])


def register_vcc_list_handlers(dp: Dispatcher):
    dp.message.register(vcc_list, Command("list"))
