
import asyncio

from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

from config_reader import BOT_TOKEN
from handlers import register_handlers

router = Router()
bot = Bot(BOT_TOKEN)








async def main():
    dp = Dispatcher()
    dp.include_router(router)
    register_handlers(dp)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())