from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from src.keyboards.pupil_keyboard import answer_buttons

new_children_buttons = {"yes": "👨‍👩‍👧‍👦 Есть ещё дети", "next": "➡️ Продолжить"}


def new_children_keyboard():
    request_keyboard_builder = ReplyKeyboardBuilder()
    button = KeyboardButton(text=new_children_buttons["yes"])
    request_keyboard_builder.add(button)
    button = KeyboardButton(text=new_children_buttons["next"])
    request_keyboard_builder.add(button)
    return request_keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


# 1. Хотели бы вы, чтобы ваш ребенок связал свое будущее с ИТ-сферой?
parents_answer_q5 = [
    "Да, считаю это перспективным направлением.",
    "Возможно, если ребенок будет заинтересован.",
    "Нет, думаю, ему/ей подойдет что-то другое."
]


def keyboard_q5_parents():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in parents_answer_q5:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


# 2. Вы поддерживаете своего ребенка в изучении новых технологий?
parents_answer_q6 = [
    "Да, всегда стараюсь помогать.",
    "Иногда, если вижу его/ее интерес.",
    "Нет, пока не знаю, как это делать."
]


def keyboard_q6_parents():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in parents_answer_q6:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


# 3. Есть ли у вас опыт работы с ИТ-технологиями?
parents_answer_q7 = [
    "Да, использую их в работе.",
    "Немного, на базовом уровне.",
    "Нет, но хотел(а) бы разобраться."
]


def keyboard_q7_parents():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in parents_answer_q7:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


# 4. Что вы считаете главным преимуществом для ребенка при изучении ИТ-технологий?
parents_answer_q8 = [
    "Возможность построить успешную карьеру.",
    "Развитие логики и креативного мышления.",
    "Знание современных технологий для повседневной жизни.",
    "Не уверен(а), но считаю это полезным."
]


def keyboard_q8_parents():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in parents_answer_q8:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


# 5. Какие ИТ-навыки, по вашему мнению, будут наиболее полезны в будущем для вашего ребенка?
parents_answer_q9 = [
    "Программирование.",
    "Работа с данными (анализ, обработка).",
    "Навыки кибербезопасности.",
    "Умение работать с современными технологиями.",
    "Не знаю, но считаю важным развивать общее понимание."
]


def keyboard_q9_parents():
    keyboard_builder = ReplyKeyboardBuilder()
    for answer in parents_answer_q9:
        button = KeyboardButton(text=answer)
        keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


check_group_buttons = {
    "present": "🎁 Хочу подарок",
    "give_me": "🎁 Забрать подарок"
}


def keyboard_check_group_parents():
    keyboard_builder = ReplyKeyboardBuilder()
    button = KeyboardButton(text=check_group_buttons["present"])
    keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)


def keyboard_check_present_parents():
    keyboard_builder = ReplyKeyboardBuilder()
    button = KeyboardButton(text=check_group_buttons["give_me"])
    keyboard_builder.row(button)
    return keyboard_builder.as_markup(resize_keyboard=True, is_persistent=True)
