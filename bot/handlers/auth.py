from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from client import Client
from client.api.auth import login_auth_login_post
from client.models.body_login_auth_login_post import BodyLoginAuthLoginPost
from client.models.login_out import LoginOut
from client.types import Response
from config import API_BASE_URL
from keyboards.boards import reply_menu
from services.auth import Auth

auth = Auth()


class AuthForm(StatesGroup):
    login = State()
    password = State()


async def auth_start(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Приступим, введите ваш логин")
    await state.set_state(AuthForm.login)


async def process_login(message: Message, state: FSMContext):
    await state.update_data(login=message.text)
    await message.answer(f"Теперь введите ваш пароль")
    await state.set_state(AuthForm.password)


async def process_password(message: Message, state: FSMContext):
    user_data = await state.get_data()

    login = user_data.get("login")
    password = message.text

    try:
        async with Client(base_url=API_BASE_URL, verify_ssl=False) as client:
            response: Response[LoginOut] = await login_auth_login_post.asyncio_detailed(
                client=client,
                body=BodyLoginAuthLoginPost(login=login, password=password),
            )
    except:
        await message.answer("Что-то пошло не так, попробуйте позже")
        return

    if response.status_code == 500:
        await message.answer("Что-то пошло не так, попробуйте позже")
    elif response.status_code == 200:
        if await auth.set_token(message.chat.id, response.parsed.token):
            await message.answer("Авторизация прошла успешно!", reply_markup=reply_menu())
        else:
            await message.answer("Что-то пошло не так, попробуйте позже")
    else:
        await message.answer(
            "Неверные данные",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Попробовать снова", callback_data="auth_start")]
            ])
        )

    await state.clear()


def register_auth_handlers(dp: Dispatcher):
    dp.callback_query.register(auth_start, lambda c: c.data == "auth_start")
    dp.message.register(process_login, AuthForm.login)
    dp.message.register(process_password, AuthForm.password)
