from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

from config import WEB_BASE_URL, VCC_URL, FRONTEND_BASE_URL


def reply_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Найти ВКС 🔍", web_app=WebAppInfo(url=f"{FRONTEND_BASE_URL}#/search"))],
        # [InlineKeyboardButton(text="Найти ВКС 🔍", web_app=WebAppInfo(url=f"{WEB_BASE_URL}/static/vcc-list.html"))],
        [InlineKeyboardButton(text="Открыть сервис ВКС 🔗", web_app=WebAppInfo(url=VCC_URL))],
    ])


def auth_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Войти в ВКС", web_app=WebAppInfo(url=f"{WEB_BASE_URL}/static/login.html"))]
    ])
