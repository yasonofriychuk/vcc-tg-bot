from http import HTTPStatus

import httpx
import redis.asyncio as redis

from client.models import MeetingList
from client.types import Response
from config import API_BASE_URL, REDIS_URL


class MeetingsClient:
    def __init__(self, redis_url: str = REDIS_URL):
        self.redis = redis.from_url(redis_url, encoding="utf-8", decode_responses=True)

    async def get_meetings(self, token: str, data: dict) -> Response[MeetingList]:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{API_BASE_URL}/vcc/meetings/", json=data, headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/json",
            })

            return Response(
                parsed=MeetingList.from_dict(response.json()),
                content=response.content,
                status_code=HTTPStatus(response.status_code),
                headers=response.headers,
            )
