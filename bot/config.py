import os

TELEGRAM_API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
if not TELEGRAM_API_TOKEN:
    raise ValueError("TELEGRAM_API_TOKEN no set")

WEB_BASE_URL = os.getenv("WEB_BASE_URL")
if not WEB_BASE_URL:
    raise ValueError("WEB_BASE_URL no set")

API_PORT = int(os.getenv("API_PORT", "5000"))

API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1")
VCC_URL = os.getenv("VCC_URL", "http://127.0.0.1")
FRONTEND_BASE_URL = os.getenv("FRONTEND_BASE_URL", "http://127.0.0.1")

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')
REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}"
