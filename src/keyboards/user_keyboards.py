from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

personal_data_buttons = {"phone": "✅ Даю согласие на обработку персональных данных"}
role_buttons = {"pupil": "👨‍💻 Ученик", "parent": "👨‍👩‍👧‍👦 Родитель"} #, "teacher": "👨‍🏫 Учитель"}


def give_phone_keyboard():
    give_phone_keyboard_builder = ReplyKeyboardBuilder()
    button = KeyboardButton(text=personal_data_buttons['phone'], request_contact=True)
    give_phone_keyboard_builder.row(button)
    return give_phone_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


def role_keyboard():
    role_keyboard_builder = ReplyKeyboardBuilder()
    for role in role_buttons:
        button = KeyboardButton(text=role_buttons[role])
        role_keyboard_builder.row(button)
    return role_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)
