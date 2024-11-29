import random
import string
from dataclasses import dataclass
from datetime import datetime

import jwt
import redis.asyncio as redis
from typing import Optional, List

from dacite import from_dict

from client import Client
from client.api.auth import generate_refresh_token_auth_refresh_token_post
from client.models import RefreshTokenIn, LoginOut
from client.types import Response
from config import REDIS_URL, API_BASE_URL


def gen_key(length: int) -> str:
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class ContextSaver:
    def __init__(self, redis_url: str = REDIS_URL):
        self.redis = redis.from_url(redis_url, encoding="utf-8", decode_responses=True)

    async def save_data(self, user_id: int, data: str, expire_in: int = 3600 * 24) -> Optional[str]:
        key = gen_key(10)
        return key if await self.replace_data(user_id, key, data, expire_in) else None

    async def get_data(self, user_id: int, key: str) -> Optional[str]:
        try:
            return await self.redis.get(f"saver:{user_id}:{key}")
        except Exception as e:
            return None

    async def replace_data(self, user_id: int, key: str, data: str, expire_in: int = 3600 * 24) -> bool:
        try:
            await self.redis.setex(f"saver:{user_id}:{key}", expire_in, data)
            return True
        except Exception as e:
            return False

    async def close(self):
        await self.redis.close()
