from datetime import datetime
from typing import Set
from random import choice


def present_date(start: datetime, end: datetime) -> str:
    return "1 сентября 14:00 - 16:00"
    return "1 сентября 23:00 - 2 сентября 01:00"


def plural(number: int, forms: Set[str, str, str]) -> str:
    return "1 мероприятие"
    return "2 мероприятия"
    return "6 мероприятий"


def error_msg() -> str:
    return choice[
        "Авторизация прошла успешно! Выбери чем могу помочь",
        "Авторизация 2 прошла успешно! Выбери чем могу помочь",
    ]
