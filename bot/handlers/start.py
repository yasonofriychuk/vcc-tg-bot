from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

from keyboards.boards import auth_keyboard, reply_menu
from services.auth import Auth

auth = Auth()


async def start_command(message: Message):
    token = await auth.get_token(message.chat.id)

    if token is None:
        await message.answer(
            """Привет! Я ВКС-бот. С моей помошью ты можешь посмотреть запланированные встречи или создать новую.
Для моей полноценной работы тебе необходимо авторизоваться в ВКС. Жми кнопку под этим сообщением, чтобы получить доступ ко всем функциям бота""",
            reply_markup=auth_keyboard(),
        )
        return

    await message.answer(
        f"""Привет, {token.user.login if token.user else 'пользователь'}! Ты авторизован, поэтому держи меню""",
        reply_markup=reply_menu()
    )


def register_start_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command("start"))
