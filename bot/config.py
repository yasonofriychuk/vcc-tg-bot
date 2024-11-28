import os

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
if not TELEGRAM_API_TOKEN:
    raise ValueError("TELEGRAM_API_TOKEN не найден в .env")

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1")

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
