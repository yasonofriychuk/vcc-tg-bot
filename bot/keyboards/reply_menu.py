from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

from config import WEB_BASE_URL


def reply_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Поиск", web_app=WebAppInfo(url=f"{WEB_BASE_URL}/static/vcc-list.html"))],
        [InlineKeyboardButton(text="Создание", web_app=WebAppInfo(url=f"{WEB_BASE_URL}/static/vcc-create.html"))],
    ])
