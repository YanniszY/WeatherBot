from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.state import State
from aiogram.fsm.context import FSMContext


from keyboards.kb import main_kb, settings_kb, add_city_kb, send_user_message
from database.db import init_db, has_city, get_city, add_city, update_city
from States.state import UserOptions
from request.request import get_current_weather
from import_bot import bot

router = Router()

init_db()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer("""
    Привет! 👋 Я твой личный бот-погодник. 🌤️

Напиши мне название города или выбери одну из команд ниже, чтобы узнать погоду!

Я могу:
- Показать текущую погоду.
- Отправлять тебе ежедневные уведомления с погодой.
- И многое другое!

Выбери, что тебя интересует:

    """, reply_markup=main_kb)

@router.message(F.text == "Текущая погода")
async def current_weather(message: Message):
    user_id = message.from_user.id

    if has_city(user_id):
        city = get_city(user_id)
        current = await get_current_weather(city, message)
    else:
        await message.answer("У вас не добавлен город", reply_markup=add_city_kb)


@router.message(F.text == "Настройки")
async def settings(message: Message):
    await message.answer("Настройки бота:", reply_markup=settings_kb)

@router.message(F.text == "Мой город")
async def my_city(message: Message, state: FSMContext):
    user_id = message.from_user.id  # Получаем ID пользователя

    if has_city(user_id):
        city = get_city(user_id)
        await message.answer(f"Ваш город: {city}")
    else:
        await message.answer("У вас не добавлен город", reply_markup=add_city_kb)

@router.message(F.text == "Изменить город")
async def change_city(message: Message, state: FSMContext):
    await message.answer("Напишите новый город")
    await state.set_state(UserOptions.user_city)

@router.message(UserOptions.user_city)
async def input_city(message: Message, state: FSMContext):
    user_id = message.from_user.id  # Получаем ID пользователя
    
    await state.update_data(user_city=message.text)
    data = await state.get_data()
    user_city = data.get('user_city')
    
    if has_city(user_id):
        update_city(user_id, user_city)
    else:
        add_city(user_id, user_city)
    
    await state.clear()
    await message.answer(f"Готово! Теперь ваш город это: {user_city}", reply_markup=main_kb)

@router.callback_query(F.data == "add_user_city")
async def change_city_inline(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Напишите свой город")
    await state.set_state(UserOptions.user_city)

@router.message(UserOptions.user_city)
async def get_city_inline(message: Message, state: FSMContext):
    user_id = message.from_user.id  # Получаем ID пользователя
    
    await state.update_data(user_city=message.text)
    data = await state.get_data()
    user_city = data.get('user_city')
    
    if has_city(user_id):
        update_city(user_id, user_city)
    else:
        add_city(user_id, user_city)
    
    await state.clear()
    await message.answer(f"Готово! Теперь ваш город это: {user_city}", reply_markup=main_kb)

@router.message(F.text == "Настройка уведомлений")
async def notification_settings(message: Message):
    user_id = message.from_user.id

    if has_city(user_id):
        city = get_city(user_id)
        await subcribe(city, message)
    else:
        await message.answer("У вас не добавлен город", reply_markup=add_city_kb)

@router.message(F.text == "Отзыв | связь с разработчиком")
async def help(message: Message, state: FSMContext):
    await state.set_state(UserOptions.user_message)
    await message.answer("Напишите жалобу или свое предположение. Если хотите связаться с разработчиком на прямую укажите свой юзернейм.") # ! сделать так чтобы бот запрашивал сообщение от пользователя и потом бот писал "сообщение получено отправить?" и две инлайн кнопки да нет.

@router.message(UserOptions.user_message)
async def get_user_message(message: Message, state: FSMContext):
    await state.update_data(user_message=message.text)

    data = await state.get_data()
    user_message = data.get('user_message')

    await message.answer(f"Ваше сообщение:\n\n{user_message}\n\nВсе верно?", reply_markup=send_user_message)

@router.callback_query(F.data == "yes_send")
async def send_help_message(callback_query: CallbackQuery, state: FSMContext):

    owner_id = 0 # your telegram id

    data = await state.get_data()

    user_message = data.get('user_message')
    await state.clear()

    await bot.send_message(owner_id, f"Поступило новое сообщение:\n{user_message}")


    await callback_query.message.answer(f"ваше сообщение: '{user_message}' отправлено разработчику!")

@router.callback_query(F.data == "no_send")
async def no_send_help_message(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.answer("Отмена")
