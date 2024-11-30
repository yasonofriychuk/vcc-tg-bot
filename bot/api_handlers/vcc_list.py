import json
from datetime import datetime, timedelta
from typing import Optional, List
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from fastapi import APIRouter, HTTPException

from api_handlers.deps.security import HeaderInitParams
from presenters.boards import auth_keyboard
from presenters.date import plural
from presenters.message import get_authorization_message
from services.auth import Auth
from bot import bot
from services.data_saver import ContextSaver
from services.meetings_client import MeetingsClient, GetMeetingIn, get_dict

auth = Auth()
saver = ContextSaver()
meet_client = MeetingsClient()

router = APIRouter(tags=["list"])


@router.post("/vcc/meetings/")
async def vcc_list(
        init_data: HeaderInitParams,
        params: GetMeetingIn
):
    token = await auth.get_token(init_data.user_id)
    if not token:
        await bot.send_message(
            init_data.user_id,
            get_authorization_message(),
            reply_markup=auth_keyboard
        )
        return

    today = datetime.today()
    if not params.from_datetime:
        params.from_datetime = today - timedelta(days=7)
    if not params.to_datetime:
        params.to_datetime = today

    try:
        meets, meet = await meet_client.get_meeting_by_filter(token, params)
    except Exception as e:
        raise HTTPException(500, f"Internal Server Error: {e}")

    rows = meets.rows_number

    if not rows or not meet:
        await bot.send_message(init_data.user_id, "Нет событий для отображения")
        return

    key = await saver.save_data(init_data.user_id, get_dict(params))
    if not key:
        raise HTTPException(500, "Internal Server Error")

    await bot.send_message(
        init_data.user_id,
        f"По вашим фильтрам найдено {rows} {plural(rows, ('событие', 'события', 'событий'))}",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Показать", callback_data=f"show_meet:{params.page}:{key}")],
        ])
    )
