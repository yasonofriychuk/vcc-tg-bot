from datetime import datetime, timedelta
from typing import Set
from random import choice

months = {
    1: 'января',
    2: 'февраля',
    3: 'марта',
    4: 'апреля',
    5: 'мая',
    6: 'июня',
    7: 'июля',
    8: 'августа',
    9: 'сентября',
    10: 'октября',
    11: 'ноября',
    12: 'декабря'
}


def format_duration(duration: timedelta | int) -> str:
    if isinstance(duration, int):
        duration = timedelta(seconds=duration)

    days = duration.days
    hours = duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60
    seconds = duration.seconds % 60
    result = []
    if days > 0:
        result.append(f"{days} д{'ень' if days == 1 else 'ней'}")
    if hours > 0:
        result.append(f"{hours} ч{'ас' if hours == 1 else 'аса'}")
    if minutes > 0:
        result.append(f"{minutes} минут")
    if seconds > 0:
        result.append(f"{seconds} секунд")
    return ' '.join(result) if result else ""


def present_date(start: datetime, end: datetime) -> str:
    if start.date() == end.date():
        return f"{start.day} {months[start.month]} {start.year} {start.hour}:{start.minute:02d} - {end.hour}:{end.minute:02d}"
    return f"{start.day} {months[start.month]} {start.year} {start.hour}:{start.minute:02d} - {end.day} {months[end.month]} {end.year} {end.hour}:{end.minute:02d}"


def plural(number: int, forms: tuple[str, str, str]) -> str:
    singular, few, many = forms

    if number % 10 == 1 and number % 100 != 11:
        return singular
    elif number % 10 in {2, 3, 4} and not (number % 100 in {12, 13, 14}):
        return few
    else:
        return many
