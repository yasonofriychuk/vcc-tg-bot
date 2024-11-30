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


@dataclass
class Role:
    name: Optional[str] = None
    description: Optional[str] = None
    id: Optional[int] = None
    permissions: Optional[List[str]] = None


@dataclass
class User:
    id: Optional[int] = None
    department_id: Optional[int] = None
    post: Optional[str] = None
    permissions: Optional[List[str]] = None
    login: Optional[str] = None
    email: Optional[str] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    middle_name: Optional[str] = None
    birthday: Optional[str] = None
    phone: Optional[str] = None
    updated_at: Optional[float] = None
    priority: Optional[int] = None
    roles: Optional[List[Role]] = None


@dataclass
class TokenData:
    user: Optional[User] = None
    token_expired_at: Optional[float] = None
    token_created_at: Optional[float] = None
    refresh_token: Optional[str] = None
    original_token: Optional[str] = None


def _decode_token(token: str) -> TokenData:
    decoded_payload: dict = jwt.decode(token, options={
        "verify_signature": False,
        "verify_exp": False
    })
    decoded_payload["original_token"] = token
    return from_dict(data_class=TokenData, data=decoded_payload)


class Auth:
    def __init__(self, redis_url: str = REDIS_URL):
        self.redis = redis.from_url(redis_url, encoding="utf-8", decode_responses=True)

    async def set_token(self, user_id: int, token: str) -> bool:
        return await self.__set_token_redis(user_id, token)

    async def get_token(self, user_id: int) -> Optional[TokenData]:
        token = await self.__get_token_redis(user_id)
        if token is None:
            return None

        token_data = _decode_token(token)
        if token_data.refresh_token is None or token_data.token_expired_at is None:
            await self.redis.delete(f"user_token:{user_id}")
            return None

        if datetime.fromtimestamp(token_data.token_expired_at) >= datetime.now():
            return await self.__refresh(user_id, token_data.refresh_token)

    async def __set_token_redis(self, user_id: int, token: str, expire_in: int = 3600 * 24 * 7) -> bool:
        try:
            await self.redis.setex(f"user_token:{user_id}", expire_in, token)
            return True
        except Exception as e:
            return False

    async def __get_token_redis(self, user_id: int) -> Optional[str]:
        try:
            token = await self.redis.get(f"user_token:{user_id}")
            return token
        except Exception as e:
            print(e)
            return None

    async def __refresh(self, user_id: int, refresh_token: str) -> Optional[TokenData]:
        try:
            async with Client(base_url=API_BASE_URL, verify_ssl=False) as client:
                response: Response[LoginOut] = await generate_refresh_token_auth_refresh_token_post.asyncio_detailed(
                    client=client,
                    body=RefreshTokenIn(token=refresh_token),
                )
        except:
            return None

        if response is None or response.status_code != 200:
            return None

        if not await self.__set_token_redis(user_id, response.parsed.token):
            return None

        return _decode_token(response.parsed.token)

    async def close(self):
        await self.redis.close()
