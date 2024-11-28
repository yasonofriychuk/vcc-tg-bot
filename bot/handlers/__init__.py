from aiogram import Dispatcher
from .start import register_start_handlers
from .auth import register_auth_handlers
from .vcc_list import register_vcc_list_handlers


def register_all_handlers(dp: Dispatcher):
    register_start_handlers(dp)
    register_auth_handlers(dp)
    register_vcc_list_handlers(dp)
