import redis.asyncio as redis
from typing import Optional
from config import REDIS_URL


class Auth:
    def __init__(self, redis_url: str = REDIS_URL):
        self.redis = redis.from_url(redis_url, encoding="utf-8", decode_responses=True)

    async def set_token(self, user_id: str, token: str) -> bool:
        return await self.__set_token_redis(user_id, token)

    async def get_token(self, user_id: str) -> Optional[str]:
        # TODO добавить refresh при истечении TTL
        return await self.__get_token_redis(user_id)

    async def __set_token_redis(self, user_id: str, token: str, expire_in: int = 3600*24*7) -> bool:
        try:
            await self.redis.setex(f"user_token:{user_id}", expire_in, token)
            return True
        except Exception as e:
            return False

    async def __get_token_redis(self, user_id: str) -> Optional[str]:
        try:
            token = await self.redis.get(f"user_token:{user_id}")
            return token
        except Exception as e:
            return None

    async def close(self):
        await self.redis.close()

