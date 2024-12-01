# vcc-tg-bot

## Запуск сервиса

Настроить .env файл:
- TELEGRAM_API_TOKEN - api токен бота
- REDIS_HOST - хост редиса, можно оставить так при запуске через docker
- REDIS_PORT - порт редиса, можно оставить так при запуске через docker
- API_BASE_URL - хост API ВКС для запросов
- VCC_URL - ссылка на сам сервис ВКС (для открытия в боте)
- WEB_BASE_URL - хост этого API, обязательно должен быть публичным с https, так бот работает на webhook. Если нет, то можно использовать ngrok или cloudpub.ru для прокси
- FRONTEND_BASE_URL - хост frontend приложения
- API_PORT - порт сервиса

После заполнения .env файла, нужно запустить сервис командой
```shell
docker-compose up --build
```