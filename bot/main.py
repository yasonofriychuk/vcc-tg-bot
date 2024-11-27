import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")

if not TELEGRAM_API_TOKEN:
    raise ValueError("TELEGRAM_API_TOKEN не найден в окружении. Проверьте файл .env.")

bot = Bot(token=TELEGRAM_API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(f"Привет, {message.from_user.first_name}!\nЯ бот на aiogram 3.x 🚀")


@dp.message()
async def echo_message(message: Message):
    await message.answer(f"Вы написали: {message.text}")


async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
