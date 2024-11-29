import logging
from aiogram.types import Update
from fastapi import FastAPI, APIRouter
from fastapi.requests import Request
import uvicorn
from contextlib import asynccontextmanager

from starlette.staticfiles import StaticFiles

from config import WEB_BASE_URL, API_PORT
from bot import bot, dp
from api.vcc_list import router as vcc_list_router
from api.vcc_create import router as vcc_create_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        await bot.set_webhook(
            url=f"{WEB_BASE_URL}/webhook",
            allowed_updates=dp.resolve_used_update_types(),
            drop_pending_updates=True,
        )
        logging.info(f"Webhook set at {WEB_BASE_URL}/webhook")
        yield
    finally:
        await bot.delete_webhook()


app = FastAPI(lifespan=lifespan)


@app.post("/webhook")
async def webhook(request: Request) -> None:
    data = await request.json()
    update = Update.model_validate(data, context={"bot": bot})
    await dp.feed_update(bot, update)


base_router = APIRouter(prefix="/api")

base_router.include_router(vcc_list_router)
base_router.include_router(vcc_create_router)

app.include_router(base_router)
app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=API_PORT)
