from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from api.deps.security import HeaderInitParams
from client import AuthenticatedClient
from client.api.meetings import get_meetings_meetings_get
from client.models import MeetingList, UserPriority
from client.types import Response
from config import API_BASE_URL
from keyboards.boards import auth_keyboard
from services.auth import Auth
from bot import bot

auth = Auth()
router = APIRouter(tags=["list"])


class VccListIn(BaseModel):
    date_from: Optional[datetime]
    date_to: Optional[datetime]


@router.post("/vcc/list/")
async def vcc_list(
    init_data: HeaderInitParams,
    params: VccListIn
):
    token = await auth.get_token(init_data.user_id)
    if not token:
        await bot.send_message(
            init_data.user_id,
            "Для использования этого функционала необходима авторизоваться",
            reply_markup=auth_keyboard
        )
        return

    today = datetime.today()
    if not params.date_from:
        params.date_from = today - timedelta(days=7)
    if not params.date_to:
        params.date_to = today

    try:
        async with AuthenticatedClient(base_url=API_BASE_URL, verify_ssl=False, token=token.original_token) as client:
            response: Response[MeetingList] = await get_meetings_meetings_get.asyncio_detailed(
                client=client,
                from_datetime=params.date_from,
                to_datetime=params.date_to,
                priority=UserPriority.VALUE_1
            )
    except Exception as e:
        await bot.send_message(init_data.user_id, "Что-то пошло не так, повторите попытку позже")
        return

    if not response or response.status_code != 200:
        await bot.send_message(init_data.user_id, "Нет подходящих встреч")
        return

    await bot.send_message(init_data.user_id, "\n".join([m.name for m in response.parsed.data][:10]))
