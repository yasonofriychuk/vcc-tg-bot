from datetime import datetime, timedelta
from typing import Set
from random import choice
import locale
from contextlib import contextmanager


@contextmanager
def set_locale(locale_name):
    old_locale = locale.getlocale(locale.LC_TIME)
    try:
        locale.setlocale(locale.LC_TIME, locale_name)
        yield
    finally:
        locale.setlocale(locale.LC_TIME, old_locale)


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
    with set_locale('ru_RU.UTF-8'):
        if start.date() == end.date():
            return f"{start.day} {start.strftime('%B')} {start.year} {start.hour}:{start.minute:02d} - {end.hour}:{end.minute:02d}"
    
        return f"{start.day} {start.strftime('%B')} {start.year} {start.hour}:{start.minute:02d} - {end.day} {end.strftime('%B')} {end.year} {end.hour}:{end.minute:02d}"


def plural(number: int, forms: set[str, str, str]) -> str:
    singular, few, many = forms

    if number % 10 == 1 and number % 100 != 11:
        return f"{number} {singular}"
    elif number % 10 in {2, 3, 4} and not (number % 100 in {12, 13, 14}):
        return f"{number} {few}"
    else:
        return f"{number} {many}"

def get_success_message() -> str:
    return choice([
        "Авторизация прошла успешно! Чем могу помочь?",
        "Вы успешно авторизованы. Что вас интересует?",
        "Добро пожаловать! Как я могу помочь после авторизации?",
        "Вы вошли в систему! Какой вопрос у вас есть?",
        "Авторизация завершена. Готов к работе! Чем помочь?",
    ])

def get_authorization_message() -> str:
    return choice([
        "Для использования этого функционала необходимо авторизоваться.",
        "Чтобы продолжить, нужно пройти авторизацию.",
        "Для доступа к данному функционалу требуется авторизация.",
        "Авторизация обязательна для использования этого функционала.",
        "Чтобы воспользоваться этой функцией, выполните авторизацию.",
    ])

def get_greetings_message() -> str:
    greeting_options = [
        """Привет! Я ВКС-бот. С моей помощью ты можешь посмотреть запланированные встречи или создать новую.
Для моей полноценной работы тебе необходимо авторизоваться в ВКС. Жми кнопку под этим сообщением, чтобы получить доступ ко всем функциям бота""",
        
        """Здравствуйте! Я ВКС-бот. С помощью меня ты можешь узнать о своих встречах или создать новые.
Для полноценного использования бота необходимо авторизоваться в ВКС. Нажми на кнопку ниже, чтобы получить доступ ко всем возможностям.""",
        
        """Приветствую! Я ВКС-бот. Ты можешь просматривать запланированные мероприятия или создать новое.
Для того чтобы я мог полноценно помочь, тебе нужно авторизоваться в ВКС. Нажми кнопку под этим сообщением для доступа ко всем функциям.""",
        
        """Добро пожаловать! Я ВКС-бот, и с моей помощью ты можешь управлять своими встречами. 
Для полного доступа к функциям бота тебе нужно авторизоваться в ВКС. Нажми кнопку ниже, чтобы продолжить.""",
        
        """Привет! Я ВКС-бот. Ты можешь использовать меня для просмотра встреч или создания новых.
Для того чтобы использовать все функции бота, тебе нужно авторизоваться в ВКС. Просто жми кнопку под этим сообщением!"""
    ]
    
    return choice(greeting_options)

def get_greeting_message(token) -> str:
    greeting_options = [
        f"Привет, {token.user.login if token.user else 'пользователь'}! Я ВКС-бот. Чем могу помочь?",
        f"Здравствуйте, {token.user.login if token.user else 'пользователь'}! Я ваш ВКС-бот. Как могу помочь?",
        f"Приветствую, {token.user.login if token.user else 'пользователь'}! Я ВКС-бот. Чем могу помочь вам?",
        f"Добро пожаловать, {token.user.login if token.user else 'пользователь'}! Я ВКС-бот, готов помочь.",
        f"Привет, {token.user.login if token.user else 'пользователь'}! Я ВКС-бот. Чем могу быть полезен?"
    ]
    
    return choice(greeting_options)

def get_error_message() -> str:
    error_options = [
        "Что-то пошло не так, повторите попытку позже.",
        "Ой, произошла ошибка. Попробуйте снова позже.",
        "Что-то не так, попробуйте повторить операцию позже.",
        "Возникла ошибка, попробуйте снова через некоторое время.",
        "Упс! Произошла ошибка, попробуйте позже."
    ]
    
    return choice(error_options)

def get_vks_error_message() -> str:
    vks_error_options = [
        "Ой, сайт ВКС упал. Повторите попытку позже.",
        "ВКС временно недоступен. Попробуйте позже.",
        "Кажется, ВКС не отвечает. Попробуйте снова через некоторое время.",
        "Сайт ВКС в данный момент недоступен. Пожалуйста, повторите попытку позже.",
        "Произошла ошибка с ВКС. Попробуйте зайти позже."
    ]
    
    return choice(vks_error_options)

def get_outdated_data_message(key, page, callback_data) -> str:
    outdated_data_options = [
        f"Данные устарели: {key}, {page}, {callback_data}. Попробуйте обновить информацию.",
        f"Информация больше не актуальна: {key}, {page}, {callback_data}. Пожалуйста, обновите данные.",
        f"Данные для {key} на странице {page} с кодом {callback_data} устарели. Попробуйте снова позже.",
        f"Обновление не удалось! Данные устарели: {key}, {page}, {callback_data}. Пожалуйста, повторите попытку.",
        f"Ошибка: данные {key} на странице {page} с параметрами {callback_data} больше не актуальны."
    ]
    
    return choice(outdated_data_options)