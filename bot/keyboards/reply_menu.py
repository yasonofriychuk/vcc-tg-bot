from aiogram.types import WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton

from config import WEB_BASE_URL


def reply_menu():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Поиск", web_app=WebAppInfo(url=WEB_BASE_URL))],
        [InlineKeyboardButton(text="Создание", web_app=WebAppInfo(url=WEB_BASE_URL))],
    ])
