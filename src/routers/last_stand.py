import asyncio

from aiogram import Router, F
from aiogram.types import Message

from config import bot, admin_group, users_data_repo, teacher_thread, parent_thread, pupil_thread
from phrases import LAST_STAND
from src.keyboards.user_keyboards import role_buttons

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


@last_stand_router.message(F.chat.id != admin_group)
async def handle_last_stand(message: Message):
    chat_id = message.chat.id
    await bot.send_message(
        chat_id=chat_id,
        text=LAST_STAND
    )

