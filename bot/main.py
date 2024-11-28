import asyncio

import redis.asyncio as redis
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from handlers import register_all_handlers
from config import TELEGRAM_API_TOKEN, REDIS_URL


async def main():
    bot = Bot(token=TELEGRAM_API_TOKEN)
    dp = Dispatcher(
        storage=RedisStorage(redis.from_url(
            REDIS_URL,
            encoding="utf-8",
            decode_responses=True,
        )),
    )

    register_all_handlers(dp)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
