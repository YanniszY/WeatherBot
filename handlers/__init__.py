from aiogram import Dispatcher
from handlers.handlers import router as router

def register_handlers(dp: Dispatcher):
    dp.include_router(router)