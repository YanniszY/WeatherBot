import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from keyboards import kb
import requests
import json
from config_reader import config

class Form(StatesGroup):
    city = State()


bot = Bot(config.bot_token.get_secret_value())
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("привет!", reply_markup=kb.main)


@dp.message(F.text == "узнать погоду!")
async def know_weather(message: Message, state: FSMContext):
    await state.set_state(Form.city)
    await message.answer("введите свой город")


@dp.message(Form.city)
async def city_name(message: Message, state: FSMContext):
    await state.update_data(city=message.text)
    data = await state.get_data()
    city = data.get('city')
    await state.clear()
    await weather(city, message)


async def weather(city: str, message: Message):
    api_url = "http://api.weatherapi.com/v1/current.json"
    api_key = "e23c81900754433b9a9152858240106"
    
    params = {
        'key': api_key,
        'q': city
    }

    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()

        await send_weather(data, message)
    else:
        print(f"ошибка при запросе данных {response.status_code}")
        return None


async def send_weather(data, message: Message):
        location = data['location']
        current = data['current']

        weather_info = (
        f"Город: {location['name']}\n"
        f"Регион: {location['region']}\n"
        f"Страна: {location['country']}\n"
        f"Широта: {location['lat']}\n"
        f"Долгота: {location['lon']}\n"
        f"Местное время: {location['localtime']}\n"
        f"Температура: {current['temp_c']}°C\n"
        f"Состояние: {current['condition']['text']}\n"
        f"Влажность: {current['humidity']}%\n"
        f"Скорость ветра: {current['wind_kph']} км/ч\n"
        )
        await message.answer(weather_info)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
