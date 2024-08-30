
import requests
import asyncio

from aiogram.types import Message

from database.db import *


# Замените YOUR_API_KEY на ваш реальный API-ключ от OpenWeatherMap
api_key = "5ca44a21a4f90b2d9ccf41c12e708cff"
url = "http://api.openweathermap.org/data/2.5/weather"
one_call_url = "https://api.openweathermap.org/data/3.0/onecall"


async def get_current_weather(city, message: Message):
    # Параметры запроса
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",  # Единицы измерения в градусах Цельсия
        "lang": "ru"  # Ответ на русском языке
    }

    # Выполнение GET-запроса
    response = requests.get(url, params=params)


    # Проверка статуса ответа и вывод данных
    if response.status_code == 200:
        data = response.json()

        # Извлечение нужных данных
        city_name = data.get("name", "Неизвестно")
        country = data.get("sys", {}).get("country", "Неизвестно")
        temp_min = data.get("main", {}).get("temp_min", "N/A")
        temp_max = data.get("main", {}).get("temp_max", "N/A")
        weather_description = data.get("weather", [{}])[0].get("description", "N/A").capitalize()
        wind_speed = data.get("wind", {}).get("speed", "N/A")
        visibility = data.get("visibility", "N/A") / 1000  # видимость в км
        cloudiness = data.get("clouds", {}).get("all", "N/A")
        
        # Формирование сообщения с эмодзи
        weather_message = (
            f"🌍 Погода в городе: {city_name}, {country}\n"
            f"🌡 Минимальная температура: {temp_min}°C\n"
            f"🌡 Максимальная температура: {temp_max}°C\n"
            f"☁️ Состояние погоды: {weather_description}\n"
            f"💨 Скорость ветра: {wind_speed} км/ч\n"
            f"👁‍🗨 Видимость: {visibility:.2f} км\n"
            f"☁️ Облачность: {cloudiness}%"
        )
        await message.answer(weather_message)
    else:
        print(f"Ошибка: {response.status_code}")


