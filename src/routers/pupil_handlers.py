import re

from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery

from config import pupil_data_repo, bot, admin_group, pupil_thread, users_data_repo
from phrases import PUPIL_AGE, PUPIL_ERROR_AGE, SCHOOL_TYPE, SCHOOL_REQUEST, ERROR_SCHOOL, GRADE_REQUEST, ERROR_GRADE, \
    EXAM_REQUEST, UNIVERSITY_REQUEST, ERROR_BUTTON, UNIVERSITY_LIST_REQUEST, GUIDE_UNIVERSITY, ERROR_UNIVERSITY, \
    PUPIL_Q1, PUPIL_Q2, PUPIL_Q3, PUPIL_Q4, PUPIL_Q5, PUPIL_Q6, PUPIL_THX_7, PUPIL_THX_9, PUPIL_THX
from src.keyboards.parent_keyboards import keyboard_check_group_parents, check_group_buttons
from src.keyboards.pupil_keyboard import pupil_age_keyboard, pupil_school_type_keyboard, school_types_buttons, \
    lyceum_keyboard, gymnasium_keyboard, school_keyboard, school_buttons, gymnasium_buttons, lyceum_buttons, \
    grade_keyboard, request_keyboard, answer_buttons, university_keyboard, university_list, keyboard_q3, keyboard_q5, \
    keyboard_q6, answer_q3, keyboard_q4, answer_q4, answer_q5, answer_q6, collage_keyboard, collage_buttons
from src.keyboards.user_keyboards import role_buttons
from src.routers.last_stand import db_checker
from src.states.pupil_states import Pupil
from src.states.user_states import User

pupil_router = Router()


@pupil_router.message(StateFilter(User.wait_role), F.text.in_(role_buttons['pupil']))
async def handle_pupil_role(message: Message, state: FSMContext):
    """Обрабатывает роль пользователя - ученик"""

    await state.set_state(Pupil.wait_age)

    chat_id = message.chat.id

    try:
        response = pupil_data_repo.get_user_by_chat_id(chat_id)
        if not response.data:
            pupil_data_repo.insert_field(chat_id)
    except:
        pass

    await bot.send_message(
        chat_id=chat_id,
        text=PUPIL_AGE,
        reply_markup=pupil_age_keyboard()
    )
    await db_checker(message)


@pupil_router.message(StateFilter(Pupil.wait_age))
async def handle_pupil_age(message: Message, state: FSMContext):
    """Обрабатывает возраст пользователя - ученик"""

    chat_id = message.chat.id
    age = message.text

    try:
        age = int(age)
        if (age > 3) and (age < 25):
            pupil_data_repo.update_field(chat_id, "age", age)
        else:
            raise ValueError

        await state.set_state(Pupil.wait_school_type)
        await bot.send_message(
            chat_id=chat_id,
            text=SCHOOL_TYPE,
            reply_markup=pupil_school_type_keyboard()
        )

    except:
        await bot.send_message(
            chat_id=chat_id,
            text=PUPIL_ERROR_AGE
        )


@pupil_router.message(StateFilter(Pupil.wait_school_type), F.text.in_([school_types_buttons['school'], school_types_buttons['lyceum'], school_types_buttons['gymnasium'], school_types_buttons['collage']]))
async def handle_pupil_school_type(message: Message, state: FSMContext):
    """Обрабатывает тип школы пользователя - ученик"""

    await state.set_state(Pupil.wait_school)

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

    elif school_type == school_types_buttons['collage']:
        await bot.send_message(
            chat_id=chat_id,
            text=SCHOOL_REQUEST,
            reply_markup=collage_keyboard()
        )


@pupil_router.message(StateFilter(Pupil.wait_school), F.text == school_buttons[0])
async def handle_parent_back_school_type(message: Message, state: FSMContext):
    chat_id = message.chat.id
    await state.set_state(Pupil.wait_school_type)
    await bot.send_message(
        chat_id=chat_id,
        text=SCHOOL_TYPE,
        reply_markup=pupil_school_type_keyboard()
    )


@pupil_router.message(StateFilter(Pupil.wait_school))
async def handle_pupil_school(message: Message, state: FSMContext):
    """Обрабатывает учебное заведение пользователя - ученик"""

    chat_id = message.chat.id
    school = message.text

    if (school in school_buttons) or (school in gymnasium_buttons) or (school in lyceum_buttons) or (school in collage_buttons):

        await state.set_state(Pupil.wait_grade)
        pupil_data_repo.update_field(chat_id, "school", school)

        if school in collage_buttons:
            await bot.send_message(
                chat_id=chat_id,
                text="Укажите, на каком Вы учебном курсе.",
                reply_markup=grade_keyboard(5)
            )
        else:
            await bot.send_message(
                chat_id=chat_id,
                text=GRADE_REQUEST,
                reply_markup=grade_keyboard(12)
            )

    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_SCHOOL
        )


@pupil_router.message(StateFilter(Pupil.wait_grade))
async def handle_pupil_grade(message: Message, state: FSMContext):
    """Обрабатывает класс в школе пользователя - ученик"""

    chat_id = message.chat.id
    grade = message.text

    try:
        grade = int(grade)
        if (grade > 0) and (grade < 12):
            pupil_data_repo.update_field(chat_id, "grade", grade)
        else:
            raise ValueError
        await state.set_state(Pupil.wait_exam)
        await bot.send_message(
            chat_id=chat_id,
            text=PUPIL_Q2,
            reply_markup=request_keyboard()
        )
    except:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_GRADE
        )


@pupil_router.message(StateFilter(Pupil.wait_exam))
async def handle_pupil_exam(message: Message, state: FSMContext):
    """Обрабатывает вопрос о сдаче экзамена пользователя - ученик"""

    chat_id = message.chat.id
    exam = message.text
    if exam in answer_buttons:
        pupil_data_repo.update_field(chat_id, "IT_live", exam)
        await state.set_state(Pupil.wait_university)
        await state.update_data(check_list=list())
        await bot.send_message(
            chat_id=chat_id,
            text=UNIVERSITY_LIST_REQUEST,
            reply_markup=ReplyKeyboardRemove()
        )
        await bot.send_message(
            chat_id=chat_id,
            text=GUIDE_UNIVERSITY,
            reply_markup=university_keyboard(set())
        )

    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_BUTTON
        )


# @pupil_router.message(StateFilter(Pupil.wait_arrival))
# async def handle_pupil_university(message: Message, state: FSMContext):
#     """Обрабатывает вопрос о поступлении в ВУЗ - ученик"""
#
#     chat_id = message.chat.id
#     arrival = message.text
#     if arrival in answer_buttons:
#         pupil_data_repo.update_field(chat_id, "arrival", arrival)
#         if arrival == answer_buttons[0]:
#             await state.set_state(Pupil.wait_university)
#             await state.update_data(check_list=list())
#             await bot.send_message(
#                 chat_id=chat_id,
#                 text=UNIVERSITY_LIST_REQUEST,
#                 reply_markup=ReplyKeyboardRemove()
#             )
#             await bot.send_message(
#                 chat_id=chat_id,
#                 text=GUIDE_UNIVERSITY,
#                 reply_markup=university_keyboard(set())
#             )
#         else:
#             await state.set_state(Pupil.wait_q2)
#             await bot.send_message(
#                 chat_id=chat_id,
#                 text=PUPIL_Q2,
#                 reply_markup=request_keyboard()
#             )
#     else:
#         await bot.send_message(
#             chat_id=chat_id,
#             text=ERROR_BUTTON
#         )


@pupil_router.callback_query(StateFilter(Pupil.wait_university), F.data == "next")
async def handle_check_university_next(callback: CallbackQuery, state: FSMContext):
    chat_id = callback.message.chat.id
    try:
        state_data = await state.get_data()
        check_list = set(state_data['check_list'])
    except:
        check_list = set()
    if len(check_list) == 0:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_UNIVERSITY
        )
    else:
        await state.set_state(Pupil.wait_q1)
        data_base_university = ""
        for i in range(len(university_list)):
            if i in check_list:
                data_base_university += university_list[i]+"; "
        pupil_data_repo.update_field(chat_id, "university", data_base_university)
        await bot.edit_message_text(
            chat_id=chat_id,
            text="Вы выбрали:\n"+data_base_university,
            message_id=callback.message.message_id,
            reply_markup=None
        )
        await bot.send_message(
            chat_id=chat_id,
            text="Напишите ФИО родителя:",
            reply_markup=ReplyKeyboardRemove()
        )


@pupil_router.callback_query(StateFilter(Pupil.wait_university))
async def handle_check_university(callback: CallbackQuery, state: FSMContext):
    chat_id = callback.message.chat.id
    university = callback.data
    try:
        state_data = await state.get_data()
        check_list = set(state_data['check_list'])
    except:
        check_list = set()
    if int(university) in check_list:
        check_list.remove(int(university))
    else:
        if len(check_list) < 3:
            check_list.add(int(university))
        else:
            await callback.answer("❗️ Можно выбрать не более 3 учебных заведений", show_alert=True)
    await state.update_data(check_list=list(check_list))
    await bot.edit_message_reply_markup(
        chat_id=chat_id,
        message_id=callback.message.message_id,
        reply_markup=university_keyboard(check_list)
    )


@pupil_router.message(StateFilter(Pupil.wait_q1))
async def handle_pupil_q1(message: Message, state: FSMContext):
    """Планируете поступление на техническую специальность - ученик"""

    chat_id = message.chat.id
    answer = message.text
    pupil_data_repo.update_field(chat_id, "parent_name", answer)
    await state.set_state(Pupil.wait_q2)
    await bot.send_message(
        chat_id=chat_id,
        text="Введите номер телефона родителя (в формате 7XXXXXXXXXX):",
    )

def validate_phone_number(phone):
    pattern = r"^7\d{10}$"
    return bool(re.fullmatch(pattern, phone))

@pupil_router.message(StateFilter(Pupil.wait_q2))
async def handle_pupil_q2(message: Message, state: FSMContext):
    chat_id = message.chat.id
    answer = message.text

    if validate_phone_number(answer):
        pupil_data_repo.update_field(chat_id, "parent_phone", answer)
        await state.set_state(Pupil.end)
        await bot.send_message(
            chat_id=chat_id,
            text=PUPIL_THX,
            reply_markup=ReplyKeyboardRemove()
        )

        user_data = users_data_repo.get_user_by_chat_id(chat_id)
        user_data = user_data.data[0]
        pupil_data = pupil_data_repo.get_user_by_chat_id(chat_id)
        pupil_data = pupil_data.data[0]
        try:
            text = (f"Пользователь {message.chat.id} - @{message.from_user.username}"
                    f"\nФИО: {user_data['name']}"
                    f"\nРоль: {role_buttons['pupil']}"
                    f"\nТелефон: +{user_data['tg_phone']}"
                    f"\n-------------------"
                    f"\nВозраст {pupil_data['age']}"
                    f"\nШкола: {pupil_data['school']}"
                    f"\nКласс/Курс: {pupil_data['grade']}"
                    f"\nУниверситеты: {pupil_data['university']}"
                    f"\nСвязать жизнь с IT: {pupil_data['IT_live']}"
                    f"\nФИО родителя: {pupil_data['parent_name']}"
                    f"\nТелефон Родителя: +{pupil_data['parent_phone']}")
            await bot.edit_message_text(
                chat_id=admin_group,
                message_id=user_data['message'],
                text=text)
        except Exception as e:
            print(e)
            for line in text.split("\n"):
                await bot.send_message(chat_id=admin_group,
                                       message_thread_id=pupil_thread,
                                       text=line
                                       )
    else:
        await bot.send_message(
            chat_id=chat_id,
            text="Неправильный формат номера. Попробуйте ещё раз. (в формате 7XXXXXXXXXX)"
        )




# @pupil_router.message(StateFilter(Pupil.wait_q3))
# async def handle_pupil_q3(message: Message, state: FSMContext):
#     chat_id = message.chat.id
#     answer = message.text
#     if answer in answer_q3:
#         await state.set_state(Pupil.wait_q4)
#         pupil_data_repo.update_field(chat_id, "interested_IT", answer)
#         await bot.send_message(
#             chat_id=chat_id,
#             text=PUPIL_Q4,
#             reply_markup=keyboard_q4()
#         )
#
#     else:
#         await bot.send_message(
#             chat_id=chat_id,
#             text=ERROR_BUTTON
#         )
#
#
# @pupil_router.message(StateFilter(Pupil.wait_q4))
# async def handle_pupil_q4(message: Message, state: FSMContext):
#     chat_id = message.chat.id
#     answer = message.text
#     if answer in answer_q4:
#         await state.set_state(Pupil.wait_q5)
#         pupil_data_repo.update_field(chat_id, "learn_IT", answer)
#         await bot.send_message(
#             chat_id=chat_id,
#             text=PUPIL_Q5,
#             reply_markup=keyboard_q5()
#         )
#
#     else:
#         await bot.send_message(
#             chat_id=chat_id,
#             text=ERROR_BUTTON
#         )
#
#
# @pupil_router.message(StateFilter(Pupil.wait_q5))
# async def handle_pupil_q5(message: Message, state: FSMContext):
#     chat_id = message.chat.id
#     answer = message.text
#     if answer in answer_q5:
#         await state.set_state(Pupil.wait_q6)
#         pupil_data_repo.update_field(chat_id, "make_IT", answer)
#         await bot.send_message(
#             chat_id=chat_id,
#             text=PUPIL_Q6,
#             reply_markup=keyboard_q6()
#         )
#
#     else:
#         await bot.send_message(
#             chat_id=chat_id,
#             text=ERROR_BUTTON
#         )


# @pupil_router.message(StateFilter(Pupil.wait_q3))
# async def handle_pupil_q5(message: Message, state: FSMContext):
#     chat_id = message.chat.id
#     answer = message.text
#     if answer in answer_q6:
#         pupil_data_repo.update_field(chat_id, "project_IT", answer)
#         await state.set_state(Pupil.end)
#         await bot.send_message(
#             chat_id=chat_id,
#             text=PUPIL_THX,
#             reply_markup=ReplyKeyboardRemove()
#         )
#
#         user_data = users_data_repo.get_user_by_chat_id(chat_id)
#         user_data = user_data.data[0]
#         pupil_data = pupil_data_repo.get_user_by_chat_id(chat_id)
#         pupil_data = pupil_data.data[0]
#         try:
#             text = (f"Пользователь {message.chat.id} - @{message.from_user.username}"
#                     f"\nФИО: {user_data['name']}"
#                     f"\nРоль: {role_buttons['pupil']}"
#                     f"\nТелефон: +{user_data['tg_phone']}"
#                     f"\n-------------------"
#                     f"\nВозраст {pupil_data['age']}"
#                     f"\nШкола: {pupil_data['school']}"
#                     f"\nКласс: {pupil_data['grade']}"
#                     f"\nЕГЭ/ОГЭ {pupil_data['exam']}"
#                     f"\nПостуление в ВУЗ: {pupil_data['arrival']}"
#                     f"\nУниверситеты: {pupil_data['university']}"
#                     f"\nТехническая специальность: {pupil_data['technical_specialty']}"
#                     f"\nСвязать жизнь с IT: {pupil_data['IT_live']}"
#                     f"\nИнтерес к IT: {pupil_data['interested_IT']}"
#                     f"\nИнтерес к IT новостям: {pupil_data['learn_IT']}"
#                     f"\nЛюбимый язык: {pupil_data['make_IT']}"
#                     f"\nХочет создать: {pupil_data['project_IT']}")
#             await bot.edit_message_text(
#                 chat_id=admin_group,
#                 message_id=user_data['message'],
#                 text=text)
#         except Exception as e:
#             print(e)
#             for line in text.split("\n"):
#                 await bot.send_message(chat_id=admin_group,
#                                        message_thread_id=pupil_thread,
#                                        text=line
#                                        )
#
#
#     else:
#         await bot.send_message(
#             chat_id=chat_id,
#             text=ERROR_BUTTON
#         )

