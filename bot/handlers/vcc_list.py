from aiogram import types, Dispatcher, F


async def handle_web_app_data(message: types.Message):
    data = message.web_app_data.data
    await message.answer(f"Полученные данные: {data}")


def register_vcc_list_handlers(dp: Dispatcher):
    dp.message.register(
        handle_web_app_data,
        F.web_app_data.data.startswith("vcc-list")
    )
