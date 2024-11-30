import json
from datetime import datetime
from typing import Optional, List

import redis.asyncio as redis
from fastapi import HTTPException
from pydantic import BaseModel

from client import AuthenticatedClient
from client.api.meetings import get_meetings_meetings_get, get_meeting_meetings_meeting_id_get
from client.models import MeetingList, UserPriority, MeetingBackend, MeetingSortingFields, MeetingFull, MeetingShortExtended
from client.types import Response, UNSET
from config import API_BASE_URL, REDIS_URL
from services.auth import TokenData


class GetMeetingIn(BaseModel):
    from_datetime: Optional[datetime]
    to_datetime: Optional[datetime]
    filter: Optional[str] = None
    priority: Optional[UserPriority] = None
    department_id: Optional[int] = None
    backend: Optional[MeetingBackend] = None
    user_participant: Optional[int] = None
    state: Optional[List[str]] = None
    user_id: Optional[int] = None
    page: int = 1


class MeetingsClient:
    def __init__(self, redis_url: str = REDIS_URL):
        self.redis = redis.from_url(redis_url, encoding="utf-8", decode_responses=True)

    async def get_meetings(self, token: TokenData, params: GetMeetingIn) -> Response[MeetingList]:
        meetings_resp = await self.__get_meetings(token, params)
        if not meetings_resp or meetings_resp.status_code != 200:
            raise HTTPException(500, f"Internal Server Error: GET meetings")
        return meetings_resp

    async def get_meeting_by_filter(
            self,
            token: TokenData,
            params: GetMeetingIn,
    ) -> tuple[MeetingList, Optional[MeetingShortExtended | MeetingFull]]:
        meetings_resp = await self.__get_meetings(token, params)
        if not meetings_resp or meetings_resp.status_code != 200:
            raise HTTPException(500, f"Internal Server Error: GET meetings")

        if not meetings_resp.parsed.data:
            return meetings_resp.parsed, None

        meeting_resp = await self.__get_meeting(token, meetings_resp.parsed.data[0].id)
        if not meeting_resp or meeting_resp.status_code != 200:
            raise HTTPException(500, f"Internal Server Error: GET meeting")
        return meetings_resp.parsed, meeting_resp.parsed

    async def __get_meetings(self, token: TokenData, params: GetMeetingIn) -> Response[MeetingList]:
        async with AuthenticatedClient(base_url=API_BASE_URL, verify_ssl=False, token=token.original_token) as client:
            response: Response[MeetingList] = await get_meetings_meetings_get.asyncio_detailed(
                client=client,
                from_datetime=params.from_datetime if params.from_datetime else UNSET,
                to_datetime=params.to_datetime if params.to_datetime else UNSET,
                filter_=params.filter if params.filter else UNSET,
                priority=params.priority if params.priority else UNSET,
                department_id=params.department_id if params.department_id else UNSET,
                backend=params.backend if params.backend else UNSET,
                user_participant=params.user_participant if params.user_participant else UNSET,
                user_id=params.user_id if params.user_id else UNSET,
                rows_per_page=1,
                page=params.page,
                sort_by=MeetingSortingFields.STARTEDAT
            )
        return response

    async def __get_meeting(self, token: TokenData, meet_id: int) -> Response[MeetingShortExtended]:
        async with AuthenticatedClient(base_url=API_BASE_URL, verify_ssl=False, token=token.original_token) as client:
            response: Response[MeetingShortExtended] = await get_meeting_meetings_meeting_id_get.asyncio_detailed(
                client=client,
                meeting_id=meet_id
            )
        return response


def get_dict(data: GetMeetingIn, **kwargs) -> str:
    data_dict = data.dict()
    if data_dict.get('from_datetime') and isinstance(data_dict['from_datetime'], datetime):
        data_dict['from_datetime'] = data_dict['from_datetime'].isoformat()
    if data_dict.get('to_datetime') and isinstance(data_dict['to_datetime'], datetime):
        data_dict['to_datetime'] = data_dict['to_datetime'].isoformat()

    data_dict.update(kwargs)
    return json.dumps(data_dict)


def dict_to_model(data: dict) -> GetMeetingIn:
    data["from_datetime"] = datetime.fromisoformat(data.get("from_datetime"))
    data["to_datetime"] = datetime.fromisoformat(data.get("to_datetime"))

    return GetMeetingIn(**data)
