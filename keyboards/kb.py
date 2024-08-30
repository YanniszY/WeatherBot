from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Текущая погода")],
        #[KeyboardButton(text="Прогноз на неделю")],
        [KeyboardButton(text="Настройки")],
        [KeyboardButton(text="Отзыв | связь с разработчиком")],
    ]
)

settings_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Мой город")],
        [KeyboardButton(text="Изменить город")],
        [KeyboardButton(text="Назад")],
    ]
)



add_city_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Добавить город", callback_data="add_user_city")]
    ]
)

send_user_message = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Да, отправить", callback_data="yes_send")],
        [InlineKeyboardButton(text="Нет, не отправляйте его", callback_data="no_send")],
    ]
)