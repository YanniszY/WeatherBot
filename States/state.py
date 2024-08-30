
from aiogram.fsm.state import State, StatesGroup

class UserOptions(StatesGroup):
    user_city = State()
    user_message = State()