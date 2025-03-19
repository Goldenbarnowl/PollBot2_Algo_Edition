from aiogram.fsm.state import State, StatesGroup


class User(StatesGroup):
    wait_phone_number = State()
    wait_name = State()
    wait_role = State()