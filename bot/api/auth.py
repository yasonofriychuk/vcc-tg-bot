from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from api.deps.security import HeaderInitParams
from client import Client
from bot import bot
from client.api.auth import login_auth_login_post
from client.models import LoginOut, BodyLoginAuthLoginPost
from client.types import Response
from config import API_BASE_URL
from keyboards.boards import reply_menu
from services.auth import Auth

auth = Auth()
router = APIRouter(tags=["auth"])


class AuthLoginIn(BaseModel):
    login: str
    password: str


@router.post("/auth/login/")
async def auth_login(
        init_data: HeaderInitParams,
        params: AuthLoginIn
):
    try:
        async with Client(base_url=API_BASE_URL, verify_ssl=False) as client:
            response: Response[LoginOut] = await login_auth_login_post.asyncio_detailed(
                client=client,
                body=BodyLoginAuthLoginPost(login=params.login, password=params.password),
            )
    except:
        raise HTTPException(500, "Internal Server Error")

    if response.status_code == 500:
        raise HTTPException(500, "Internal Server Error")

    if response.status_code != 200:
        return {"status": False}

    if not await auth.set_token(init_data.user_id, response.parsed.token):
        raise HTTPException(500, "Internal Server Error")

    await bot.send_message(init_data.user_id, "Авторизация прошла успешно! Выбери чем могу помочь", reply_markup=reply_menu())
    return {"status": True}


@router.get("/auth/jwt")
async def auth_jwt(
    init_data: HeaderInitParams,
):
    token = await auth.get_token(init_data.user_id)
    if not token:
        raise HTTPException(status_code=403, detail="Unauthorized")

    return {"token": token}
