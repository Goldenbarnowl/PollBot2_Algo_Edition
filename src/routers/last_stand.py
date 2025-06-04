import asyncio

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message

from config import bot, admin_group, users_data_repo, teacher_thread, parent_thread, pupil_thread, supabase
from phrases import LAST_STAND
from src.keyboards.pupil_keyboard import event_info_keyboard, events_keyboard
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


        "e_2": """🔥 Привет, будущий мастер общения с ИИ!
        
🤖 Мы разберём, как правильно формулировать запросы (промпты), чтобы искусственный интеллект делал именно то, что ты хочешь. Тексты, изображения, задачи — всё будет тебе по плечу!

📚 10 занятий по 2 ак. часа, 2 раза в неделю — и ты прокачаешься по полной.

🚀 Стартуем 2 июня, финалим 6 июля. Подключайся — впереди только полезное!""",


        "e_3": """🔥 Халоу боиз энд гёрлз!
Курс по созданию сайтов с помощью No/Low-код инструментов а-ля Tilda, Figma и всякие разные ИИшки — здесь будет всё: расписание, полезные материалы, советы и примеры и, главное, прямой контакт с препом курса!

📚 10 занятий по 2 ак. часа (это 90 минут), 2 раза в неделю — и ты прокачаешься по полной. Даже можно будет пойти зарабатывать на этом. Но это если хорошо научишься.

🚀 Стартуем 2 июня, финалим 6 июля. Подключайся — впереди только полезное!""",


        "e_4": """💻 Привет!
Канал с серией вебинаров «Готовимся стать программистом» — отличное место, чтобы сделать уверенный шаг в мир IT!

📚 Мы поговорим про основы программирования, узнаем, как выбрать направление, какие навыки востребованы и как начать учиться уже сейчас.

🧠 Впереди 10 вебинаров по 2 ак. часа, по 2 занятия в неделю — онлайн, удобно, по делу.

📅 Встречаемся с 16 июня по 20 июля — оставайся на связи, будет полезно! """,


        "e_5": """Marketing Yard: конференция для продуктовых маркетологов

Узнаем, как продвигать ИТ-решения, и какие стратегии работают в 2025 году. Разберём успешные кейсы: от запуска стартапов до масштабирования их на международный рынок. Познакомимся с функциональными инструментами аналитики, автоматизации и управления продуктом, в том числе на базе генеративного ИИ.

14 июня в 15:00 - 15 июня в 20:00, Точка кипения Омск (ул. Маршала Жукова, д. 21)"""
    }

    url_dict = {
        "e_1": "https://docs.google.com/forms/d/e/1FAIpQLSfbcCJGJRqBQaNE6YklC4lh7sak_Bx3LKDdyDc62uVtpLEP3w/viewform",
        "e_2": "https://t.me/promptmaster_algo",
        "e_3": "https://t.me/nolowcode4web",
        "e_4": "https://t.me/prepare2prog",
        "e_5": "https://leader-id.ru/events/542377"
    }

    await bot.send_message(
        chat_id=call.from_user.id,
        text=event_dict[call.data],
        reply_markup=event_info_keyboard("❗️ Участвовать ❗", url_dict[call.data]),
        parse_mode="HTML"
    )


@last_stand_router.message(Command('spamtest'), F.chat.id == 820176381)
async def spam_attack(message: Message):
    text = """🎉 Новые мероприятия в Омске!
Мы обновили список событий — теперь в боте доступны свежие мероприятия, которые пройдут в Омске в ближайшее время!"""
    response = supabase.table('UserData').select('*').execute()
    data = response.data
    counter = 0
    await bot.send_message(chat_id=message.chat.id,
                           text=text,
                           parse_mode='HTML')

    for userdata in data:
        try:
            await bot.send_photo(chat_id=userdata['chat_id'],
                                 text=text,
                                 parse_mode='HTML',
                                 reply_markup=events_keyboard())
            counter += 1
        except Exception as e:
            await bot.send_message(chat_id=message.chat.id,
                                   text=f"{counter} {userdata['chat_id']} - не отправлено\n {str(e)})",
                                   parse_mode='HTML')

    print('Отправлено:', counter)


@last_stand_router.message(Command('spam'), F.chat.id == 820176381)
async def spam_attack(message: Message):
    text = """🎉 Новые мероприятия в Омске!
Мы обновили список событий — теперь в боте доступны свежие мероприятия, которые пройдут в Омске в ближайшее время!"""
    response = supabase.table('UserData').select('*').execute()
    data = response.data
    counter = 0
    await bot.send_message(chat_id=message.chat.id,
                           text=text,
                           parse_mode='HTML')

    for userdata in data:
        try:
            await bot.send_photo(chat_id=userdata['chat_id'],
                                 text=text,
                                 parse_mode='HTML',
                                 reply_markup=events_keyboard())
            counter += 1
        except Exception as e:
            await bot.send_message(chat_id=message.chat.id,
                                   text=f"{counter} {userdata['chat_id']} - не отправлено\n {str(e)})",
                                   parse_mode='HTML')

    print('Отправлено:', counter)


@last_stand_router.message(F.chat.id != admin_group)
async def handle_last_stand(message: Message):
    chat_id = message.chat.id
    await bot.send_message(
        chat_id=chat_id,
        text=LAST_STAND
    )


