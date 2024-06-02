import asyncio
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="узнать погоду!")]
    ]
)