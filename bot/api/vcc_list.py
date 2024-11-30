import json
from datetime import datetime, timedelta
from typing import Optional
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
from services.auth import Auth
from bot import bot
from services.data_saver import ContextSaver

auth = Auth()
saver = ContextSaver()

router = APIRouter(tags=["list"])


class VccListIn(BaseModel):
    date_from: Optional[datetime]
    date_to: Optional[datetime]


def get_callback_data(data: VccListIn, **kwargs) -> str:
    data_dict = data.dict()
    if data_dict.get('date_from') and isinstance(data_dict['date_from'], datetime):
        data_dict['date_from'] = data_dict['date_from'].isoformat()
    if data_dict.get('date_to') and isinstance(data_dict['date_to'], datetime):
        data_dict['date_to'] = data_dict['date_to'].isoformat()

    data_dict.update(kwargs)
    return json.dumps(data_dict)


@router.post("/vcc/list/")
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
                rows_per_page=1,
                page=1,
            )
    except Exception as e:
        raise HTTPException(500, "Internal Server Error")

    if not response or response.status_code != 200 or not response.parsed.rows_number:
        await bot.send_message(init_data.user_id, "Нет подходящих встреч")
        return

    key = await saver.save_data(init_data.user_id, get_callback_data(params, page=1))
    if not key:
        raise HTTPException(500, "Internal Server Error")

    await bot.send_message(
        init_data.user_id,
        f"По вашим фильтрам найдено {response.parsed.rows_number} встреч",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Показать", callback_data=f"show_meet:{1}:{key}")],
        ])
    )
