from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

from config import WEB_BASE_URL


def reply_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Найти ВКС 🔍", web_app=WebAppInfo(url=f"{WEB_BASE_URL}/static/vcc-list.html"))],
        [InlineKeyboardButton(text="Добавить новую ВКС ➕", web_app=WebAppInfo(url=f"{WEB_BASE_URL}/static/vcc-create.html"))],
    ])


def auth_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Войти в ВКС", web_app=WebAppInfo(url=f"{WEB_BASE_URL}/static/login.html"))]
    ])
