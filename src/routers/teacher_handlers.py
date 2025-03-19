from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove

from config import bot, teacher_data_repo, users_data_repo, admin_group, teacher_thread
from phrases import TEACHER_WAIT_CONTACT_DATA, SCHOOL_TYPE, ERROR_SCHOOL, SCHOOL_REQUEST, TEACHER_CHILDREN_COUNT, \
    TEACHER_Q1, TEACHER_Q2, TEACHER_Q3, TEACHER_Q4, TEACHER_Q5, TEACHER_THX
from src.keyboards.pupil_keyboard import pupil_school_type_keyboard, school_buttons, gymnasium_buttons, lyceum_buttons, \
    gymnasium_keyboard, school_types_buttons, lyceum_keyboard, school_keyboard, request_keyboard, answer_buttons
from src.keyboards.user_keyboards import role_buttons
from src.routers.last_stand import db_checker
from src.states.teacher_state import Teacher
from src.states.user_states import User

teacher_router = Router()


@teacher_router.message(StateFilter(User.wait_role), F.text.in_(role_buttons['teacher']))
async def handle_teatcher_router_role(message: Message, state: FSMContext):
    """Обрабатывает роль пользователя - учитель
        Запрашивает контактные данные
    """

    chat_id = message.chat.id
    await state.set_state(Teacher.wait_contact_data)

    try:
        response = teacher_data_repo.get_user_by_chat_id(chat_id)
        if not response.data:
            teacher_data_repo.insert_field(chat_id)
    except:
        pass
    await bot.send_message(
        chat_id=chat_id,
        text=TEACHER_WAIT_CONTACT_DATA,
        reply_markup=ReplyKeyboardRemove()
    )
    await db_checker(message)


@teacher_router.message(StateFilter(Teacher.wait_contact_data))
async def handle_teacher_contact_data(message: Message, state: FSMContext):
    """Обрабатывает контактные данные учителя"""

    chat_id = message.chat.id
    contact = message.text

    await state.set_state(Teacher.wait_school_type)
    teacher_data_repo.update_field(chat_id, "contact_data", contact)

    await bot.send_message(
        chat_id=chat_id,
        text=SCHOOL_TYPE,
        reply_markup=pupil_school_type_keyboard()
    )


@teacher_router.message(StateFilter(Teacher.wait_school_type), F.text.in_(
    [school_types_buttons['school'], school_types_buttons['lyceum'], school_types_buttons['gymnasium']]))
async def handle_teacher_school_type(message: Message, state: FSMContext):
    """Обрабатывает тип школы пользователя"""

    await state.set_state(Teacher.wait_school)

    chat_id = message.chat.id
    school_type = message.text

    if school_type == school_types_buttons['school']:
        await bot.send_message(
            chat_id=chat_id,
            text=SCHOOL_REQUEST,
            reply_markup=school_keyboard()
        )

    elif school_type == school_types_buttons['lyceum']:
        await bot.send_message(
            chat_id=chat_id,
            text=SCHOOL_REQUEST,
            reply_markup=lyceum_keyboard()
        )

    elif school_type == school_types_buttons['gymnasium']:
        await bot.send_message(
            chat_id=chat_id,
            text=SCHOOL_REQUEST,
            reply_markup=gymnasium_keyboard()
        )


@teacher_router.message(StateFilter(Teacher.wait_school))
async def handle_teacher_school(message: Message, state: FSMContext):
    """Обрабатывает учебное заведение пользователя """

    chat_id = message.chat.id
    school = message.text

    if (school in school_buttons) or (school in gymnasium_buttons) or (school in lyceum_buttons):

        await state.set_state(Teacher.wait_q1)
        teacher_data_repo.update_field(chat_id, "school", school)

        await bot.send_message(
            chat_id=chat_id,
            text=TEACHER_Q1,
            reply_markup=request_keyboard()
        )

    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_SCHOOL
        )


@teacher_router.message(StateFilter(Teacher.wait_q1), F.text.in_(answer_buttons))
async def handle_teacher_q1(message: Message, state: FSMContext):
    """Обрабатывает первый вопрос учителя"""

    chat_id = message.chat.id
    answer = message.text
    teacher_data_repo.update_field(chat_id, "interested_child", answer)

    await state.set_state(Teacher.wait_q2)
    await bot.send_message(
        chat_id=chat_id,
        text=TEACHER_Q2,
        reply_markup=request_keyboard()
    )


@teacher_router.message(StateFilter(Teacher.wait_q2), F.text.in_(answer_buttons))
async def handle_teacher_q2(message: Message, state: FSMContext):
    """Обрабатывает второй вопрос учителя"""

    chat_id = message.chat.id
    answer = message.text
    teacher_data_repo.update_field(chat_id, "it_measure", answer)

    await state.set_state(Teacher.wait_q3)
    await bot.send_message(
        chat_id=chat_id,
        text=TEACHER_Q3,
        reply_markup=ReplyKeyboardRemove()
    )


@teacher_router.message(StateFilter(Teacher.wait_q3), F.text)
async def handle_teacher_q3(message: Message, state: FSMContext):
    """Обрабатывает третий вопрос учителя"""

    chat_id = message.chat.id
    answer = message.text
    teacher_data_repo.update_field(chat_id, "equipping_situation", answer)

    await state.set_state(Teacher.wait_q4)
    await bot.send_message(
        chat_id=chat_id,
        text=TEACHER_Q4,
        reply_markup=request_keyboard()
    )


@teacher_router.message(StateFilter(Teacher.wait_q4), F.text.in_(answer_buttons))
async def handle_teacher_q4(message: Message, state: FSMContext):
    """Обрабатывает второй вопрос учителя"""

    chat_id = message.chat.id
    answer = message.text
    teacher_data_repo.update_field(chat_id, "extra_time", answer)

    await state.set_state(Teacher.wait_q5)
    await bot.send_message(
        chat_id=chat_id,
        text=TEACHER_Q5,
        reply_markup=request_keyboard()
    )


@teacher_router.message(StateFilter(Teacher.wait_q5), F.text.in_(answer_buttons))
async def handle_teacher_q5(message: Message, state: FSMContext):
    """Обрабатывает второй вопрос учителя"""

    chat_id = message.from_user.id
    answer = message.text
    teacher_data_repo.update_field(chat_id, "courses", answer)

    await bot.send_message(
        chat_id=chat_id,
        text=TEACHER_THX,
        reply_markup=ReplyKeyboardRemove()
    )

    user_data = users_data_repo.get_user_by_chat_id(chat_id)
    user_data = user_data.data[0]
    teacher_data = teacher_data_repo.get_user_by_chat_id(chat_id)
    teacher_data = teacher_data.data[0]
    try:
        text = (f"Пользователь {message.chat.id} - @{message.from_user.username}"
                f"\nФИО: {user_data['name']}"
                f"\nРоль: {role_buttons['teacher']}"
                f"\nТелефон: +{user_data['tg_phone']}"
                f"\n-------------------"
                f"\nКонтактные данные: {teacher_data['contact_data']}"
                f"\nШкола: {teacher_data['school']}"
                f"\nЗаинтересованные ученики: {teacher_data['interested_child']}"
                f"\nIT мероприятия: {teacher_data['it_measure']}"
                f"\nНаличие оборудывания в школе: {teacher_data['equipping_situation']}"
                f"\nГотов уделять время на доп. занятия: {teacher_data['extra_time']}"
                f"\nПроходил(а) IT курсы: {teacher_data['courses']}")
        await bot.edit_message_text(
            chat_id=admin_group,
            message_id=user_data['message'],
            text=text)
    except Exception as e:
        print(e)
        for line in text.split("\n"):
            await bot.send_message(chat_id=admin_group,
                                   message_thread_id=teacher_thread,
                                   text=line
                                   )
