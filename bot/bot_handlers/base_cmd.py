from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from presenters.boards import auth_keyboard, reply_menu
from presenters.message import get_greetings_message, get_greeting_message
from services.auth import Auth

auth = Auth()


async def start_command(message: Message):
    token = await auth.get_token(message.chat.id)

    if token is None:
        await message.answer(get_greetings_message(), reply_markup=auth_keyboard())
        return

    await message.answer(get_greeting_message(token), reply_markup=reply_menu())


async def menu_command(message: Message):
    token = await auth.get_token(message.chat.id)
    if token is None:
        await message.answer(get_greetings_message(), reply_markup=auth_keyboard())
        return

    await message.answer("Чем могу помочь?", reply_markup=reply_menu())


def register_start_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command("start"))
    dp.message.register(start_command, Command("menu"))
