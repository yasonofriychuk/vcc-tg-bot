from datetime import datetime, timedelta
from typing import Set
from random import choice

months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декабрь'
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
        result.append(f"{minutes} мин")
    if seconds > 0:
        result.append(f"{seconds} сек")
    return ' '.join(result) if result else "0 сек"


def present_date(start: datetime, end: datetime) -> str:
    if start.date() == end.date():
        return f"{start.day} {months[start.month]} {start.year} {start.hour}:{start.minute:02d} - {end.hour}:{end.minute:02d}"
    return f"{start.day} {months[start.month]} {start.year} {start.hour}:{start.minute:02d} - {end.day} {months[end.month]} {end.year} {end.hour}:{end.minute:02d}"

def plural(number: int, forms: set[str, str, str]) -> str:
    singular, few, many = forms

    if number % 10 == 1 and number % 100 != 11:
        return f"{number} {singular}"
    elif number % 10 in {2, 3, 4} and not (number % 100 in {12, 13, 14}):
        return f"{number} {few}"
    else:
        return f"{number} {many}"