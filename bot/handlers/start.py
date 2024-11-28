from aiogram import Dispatcher
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

from services.auth import Auth

auth_redis = Auth()


async def start_command(message: Message):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Авторизация", callback_data="auth_start")]
    ])
    await message.answer("Привет! Нажми 'Авторизация', чтобы войти", reply_markup=keyboard)


async def check_command(message: Message):
    await message.answer(f"{await auth_redis.get_token(str(message.chat.id))}")


def register_start_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command("start"))
    dp.message.register(check_command, Command("check"))
