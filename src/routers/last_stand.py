import asyncio

from aiogram import Router, F
from aiogram.types import Message

from config import bot, admin_group, users_data_repo, teacher_thread, parent_thread, pupil_thread
from phrases import LAST_STAND
from src.keyboards.pupil_keyboard import event_info_keyboard
from src.keyboards.user_keyboards import role_buttons
from src.states.user_states import User

last_stand_router = Router()


async def db_checker(message: Message):
    #if message.text == role_buttons['teacher']:
        #message_thread = teacher_thread
    if message.text == role_buttons['parent']:
        message_thread = parent_thread
    elif message.text == role_buttons['pupil']:
        message_thread = pupil_thread
    else:
        message_thread = 0

    user_data = users_data_repo.get_user_by_chat_id(message.chat.id)
    user_data = user_data.data[0]
    adm_mes = await bot.send_message(
        chat_id=admin_group,
        message_thread_id=message_thread,
        text=f"(Проходит тест) Пользователь {message.chat.id} - @{message.from_user.username}"
             f"\nФИО: {user_data['name']}"
             f"\nРоль: {message.text}"
             f"\nТелефон: +{user_data['tg_phone']}",
    )
    users_data_repo.update_field(message.chat.id, "message", adm_mes.message_id)


@last_stand_router.callback_query(User.end)
async def handle_event_end(call: Message):
    event_dict = {
        "e_1": """<b>Бесплатные курсы программирования Python для школьников 8-11 классов</b>

📍 <b>Место проведения:</b> На базе вашего образовательного учреждения

🎯 <b>Что получит участник:</b>

🔥 Практическое обучение языку Python с нуля

👨‍🏫 Занятия с сертифицированными преподавателями

💼 Профориентационные консультации от IT-специалистов (frontend/backend)

🎮 Создание собственных игровых проектов

📂 Готовое портфолио для поступления

📜 Официальный сертификат (с фиксацией на Госуслугах)

💎 До 5 дополнительных баллов к ЕГЭ

🤝 Возможность стажировки в IT-студии Botoforge

🎯 Внеучебные активности: квесты, пейнтбол, лазертаг

📅 <b>Формат обучения:</b>

Очные занятия 2 раза в неделю

Расписание согласуется со школой

Группы формируются с учетом возраста и уровня подготовки

❗ <b>Важно:</b>

Количество мест строго ограничено

Участие возможно только один раз

Обязательна предварительная регистрация

👉 <b>Как записаться</b>: Заполните форму регистрации ниже""",


        "e_2": """Компания Сбер и кафедра ПМиФИ ОмГТУ открывают регистрацию на масштабные командные соревнования. Кейсы по большим языковым моделям и фирменному продукту «Навигатор BI» от Сбера, гибридный формат участия, экспертная поддержка, крутые подарки победителям и призёрам – это лишь часть причин попробовать свои силы. Участвовать могут студенты любых учреждений высшего и среднего специального образования.

23 мая в 15:00 - 26 мая в 11:00, ОмГТУ (пр-кт Мира, д. 11)

Обязательна регистрация:""",


        "e_3": """Самое масштабное ИТ-мероприятие Омска для школьников и младших студентов. Хакатон, посвящённый разработке веб-приложений, сайтов и ботов. Каждому участнику предоставляется возможность получить опыт решения реальных задач, послушать выступления крутых ребят и познакомиться с активными представителями ИТ-сообщества. Кейсы разработаны таким образом, что принять участие можно не имея навыков программирования.

2 мая в 14:00 - 4 мая в 17:00, Точка кипения Омск (ул. Маршала Жукова, д. 21)

Обязательна регистрация:""",


        "e_4": """Изучим основы Scrum и других методологий управления проектами. Разберёмся, как выстраивать сложные процессы в продуктовой разработке при постоянно изменяющихся требованиях. Уделим внимание психологии командной работы: как мотивировать людей, разрешать конфликты и создавать атмосферу доверия. Прокачаем навыки коммуникации, научимся говорить на одном языке с разработчиками, заказчиками и стейкхолдерами.

17 мая в 15:00 - 18 мая в 20:00, Точка кипения Омск (ул. Маршала Жукова, д. 21)

Обязательна регистрация:""",
    }

    url_dict = {
        "e_1": "https://docs.google.com/forms/d/e/1FAIpQLSfbcCJGJRqBQaNE6YklC4lh7sak_Bx3LKDdyDc62uVtpLEP3w/viewform",
        "e_2": "https://aibi.pmifi.ru/",
        "e_3": "https://leader-id.ru/events/550454",
        "e_4": "https://leader-id.ru/events/542373",
    }

    await bot.send_message(
        chat_id=call.from_user.id,
        text=event_dict[call.data],
        reply_markup=event_info_keyboard("❗️ Регистрация ❗", url_dict[call.data]),
        parse_mode="HTML"
    )





@last_stand_router.message(F.chat.id != admin_group)
async def handle_last_stand(message: Message):
    chat_id = message.chat.id
    await bot.send_message(
        chat_id=chat_id,
        text=LAST_STAND
    )

