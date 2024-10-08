# Telegram Weather Bot

Этот проект представляет собой простого Telegram-бота, который позволяет пользователям получать информацию о погоде в их городе.

## Функциональность

- **Настройка города**: Пользователь указывает свой город в настройках бота.
- **Погода на сегодня**: Бот предоставляет информацию о погоде на текущий день для выбранного города.

## Установка и настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/ваш-логин/имя-репозитория.git
```
### 2. Установка зависимостей

## Перейдите в директорию с проектом и установите необходимые зависимости:

```
pip install -r requirements.txt
```

### 3. Настройка бота

   - Получите токен вашего Telegram-бота через BotFather.
   - Создайте файл или отредактируйте файл .env в корневой папке проекта и добавьте в него ваш токен:
   ```
   BOT_TOKEN="YOUR TOKEN"
   ```
   - Вставтье свой API ключ в request/request.py (его можно получить на сайте openweathermap)
   ```
   api_key = ""
   ```
   - Напишите свой user id в файле handlers/handlers.py (строка 135)
   ```
   owner_id = 0 # your telegram id
   ```

### 4. Запуск бота

## Запустите бота командой:

```
python bot.py
```

