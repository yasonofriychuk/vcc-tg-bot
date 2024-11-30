from aiogram import Dispatcher

from .ics import register_ics_handlers
from .base_cmd import register_start_handlers
from .vcc_list import register_vcc_list_handlers


def register_all_handlers(dp: Dispatcher):
    register_start_handlers(dp)
    register_vcc_list_handlers(dp)
    register_ics_handlers(dp)
