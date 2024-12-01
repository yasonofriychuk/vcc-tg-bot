import pprint
from datetime import datetime, timedelta

from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, BufferedInputFile

from presenters.boards import auth_keyboard
from services.auth import Auth
from services.meetings_client import MeetingsClient, dict_to_model
from ics import Calendar, Event

auth = Auth()
meet_client = MeetingsClient()


async def week_command(message: Message):
    user_id = message.chat.id

    token = await auth.get_token(user_id)
    if not token:
        await message.answer(text=f"Данные устарели", reply_markup=auth_keyboard())
        return

    current = datetime.today()

    meetings = await meet_client.get_meetings(token, dict_to_model({
        "from_datetime": current.isoformat(),
        "to_datetime": (current + timedelta(days=7)).isoformat(),
        "user_id": token.user.id,
    }))

    if not meetings.parsed.data:
        await message.answer("У вас нет запланированных ВКС")
        return

    calendar = Calendar(events=[
        Event(
            name=meeting.name,
            begin=meeting.started_at,
            end=meeting.ended_at,
            url=meeting.permalink,
        ) for meeting in meetings.parsed.data
    ])

    await message.answer_document(
        document=BufferedInputFile(calendar.serialize().encode(encoding="utf-8"), filename="meeting.ics"),
        caption="Вот ваши ВКС на неделю. Вы можете добавить их в свой календарь."
    )
    calendar.serialize()


def register_week_handlers(dp: Dispatcher):
    dp.message.register(week_command, Command("week"))