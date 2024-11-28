from aiogram import Dispatcher
from .start import register_start_handlers
from .auth import register_auth_handlers


def register_all_handlers(dp: Dispatcher):
    register_start_handlers(dp)
    register_auth_handlers(dp)
