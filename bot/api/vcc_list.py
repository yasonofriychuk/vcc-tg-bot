import json
from datetime import datetime, timedelta
from typing import Optional, List
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.deps.security import HeaderInitParams
from client import AuthenticatedClient
from client.api.meetings import get_meetings_meetings_get
from client.models import MeetingList
from client.types import Response
from config import API_BASE_URL
from keyboards.boards import auth_keyboard
from presenters.date import plural
from services.auth import Auth
from bot import bot
from services.data_saver import ContextSaver
from services.meetings_client import MeetingsClient

auth = Auth()
saver = ContextSaver()
# meetings_client = MeetingsClient()

router = APIRouter(tags=["list"])


class VccListIn(BaseModel):
    from_datetime: Optional[datetime]
    to_datetime: Optional[datetime]
    filter: Optional[str] = None
    priority: Optional[int] = None
    building_id: Optional[int] = None
    room_id: Optional[int] = None
    department_id: Optional[int] = None
    user_id: Optional[int] = None
    backend: Optional[str] = None
    user_participant: Optional[int] = None
    state: Optional[List[str]] = None


def get_callback_data(data: VccListIn, **kwargs) -> str:
    data_dict = data.dict()
    if data_dict.get('from_datetime') and isinstance(data_dict['from_datetime'], datetime):
        data_dict['from_datetime'] = data_dict['from_datetime'].isoformat()
    if data_dict.get('to_datetime') and isinstance(data_dict['to_datetime'], datetime):
        data_dict['to_datetime'] = data_dict['to_datetime'].isoformat()

    data_dict.update(kwargs)
    return json.dumps(data_dict)


@router.post("/vcc/meetings/")
async def vcc_list(
        init_data: HeaderInitParams,
        params: VccListIn
):
    token = await auth.get_token(init_data.user_id)
    if not token:
        await bot.send_message(
            init_data.user_id,
            "Для использования этого функционала необходимо авторизоваться",
            reply_markup=auth_keyboard
        )
        return

    today = datetime.today()
    if not params.from_datetime:
        params.from_datetime = today - timedelta(days=7)
    if not params.to_datetime:
        params.to_datetime = today

    try:
        async with AuthenticatedClient(base_url=API_BASE_URL, verify_ssl=False, token=token.original_token) as client:
            response: Response[MeetingList] = await get_meetings_meetings_get.asyncio_detailed(
                client=client,
                from_datetime=params.from_datetime,
                to_datetime=params.to_datetime,
                rows_per_page=1,
                page=1,
            )
    except Exception as e:
        raise HTTPException(500, f"Internal Server Error")

    if not response or response.status_code != 200 or not response.parsed.rows_number:
        await bot.send_message(init_data.user_id, "Нет событий для отображения")
        return

    key = await saver.save_data(init_data.user_id, get_callback_data(params, page=1))
    if not key:
        raise HTTPException(500, "Internal Server Error 2")

    rows = response.parsed.rows_number

    await bot.send_message(
        init_data.user_id,
        f"По вашим фильтрам найдено {rows} {plural(rows, ('событие', 'события', 'событий'))}",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Показать", callback_data=f"show_meet:{1}:{key}")],
        ])
    )
