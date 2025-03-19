from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.utils.markdown import hlink

from config import parent_data_repo, pupil_data_repo, bot, pchildren_data_repo, admin_group, parent_thread, \
    users_data_repo
from phrases import PCHILDREN_NAME, ERROR_PCHILDREN, SCHOOL_TYPE, PUPIL_ERROR_AGE, PARENT_SCHOOL_TYPE, SCHOOL_REQUEST, \
    GRADE_REQUEST, ERROR_SCHOOL, EXAM_REQUEST, ERROR_GRADE, UNIVERSITY_REQUEST, ERROR_BUTTON, UNIVERSITY_LIST_REQUEST, \
    GUIDE_UNIVERSITY, PUPIL_Q2, ERROR_UNIVERSITY, PUPIL_Q1, PUPIL_Q6, PUPIL_Q5, PUPIL_Q4, PUPIL_Q3, \
    PCHILDREN_AGE, PARENT_GRADE_REQUEST, PARENTS_Q2, PARENTS_Q3, NEW_CHILDREN, PARENTS_Q5, PARENTS_Q6, PARENTS_Q7, \
    PARENTS_Q9, PARENTS_Q8, THX_PARENTS, REPEAT_PARENTS, PARENT_PRESENT, PARENT_GIVE, THX_PARENTS_END
from src.keyboards.parent_keyboards import new_children_keyboard, new_children_buttons, keyboard_q5_parents, \
    keyboard_q6_parents, parents_answer_q6, keyboard_q7_parents, parents_answer_q9, parents_answer_q8, \
    keyboard_q9_parents, keyboard_q8_parents, parents_answer_q7, keyboard_check_group_parents, check_group_buttons, \
    keyboard_check_present_parents
from src.keyboards.pupil_keyboard import pupil_school_type_keyboard, school_types_buttons, school_keyboard, \
    lyceum_keyboard, gymnasium_keyboard, school_buttons, gymnasium_buttons, lyceum_buttons, grade_keyboard, \
    request_keyboard, answer_buttons, university_keyboard, university_list, answer_q6, keyboard_q6, answer_q5, \
    keyboard_q5, answer_q4, keyboard_q4, answer_q3, keyboard_q3, pupil_age_keyboard
from src.keyboards.user_keyboards import role_buttons
from src.routers.last_stand import db_checker
from src.states.parent_states import Parent
from src.states.user_states import User

parent_router = Router()


@parent_router.message(StateFilter(User.wait_role), F.text.in_(role_buttons['parent']))
async def handle_parent_role(message: Message, state: FSMContext):
    """Обрабатывает роль пользователя - родитель"""

    await state.set_state(Parent.wait_children_name)

    chat_id = message.chat.id

    try:
        response = parent_data_repo.get_user_by_chat_id(chat_id)
        if not response.data:
            parent_data_repo.insert_field(chat_id)
    except:
        pass

    await bot.send_message(
        chat_id=chat_id,
        text=PCHILDREN_NAME,
        reply_markup=ReplyKeyboardRemove()
    )
    await db_checker(message)


@parent_router.message(StateFilter(Parent.wait_children_name))
async def handle_children_name(message: Message, state: FSMContext):
    chat_id = message.chat.id
    name = message.text

    try:
        await state.set_state(Parent.wait_age)
        pchildren_data_repo.insert_field(chat_id, "children_name", name)

        await bot.send_message(
            chat_id=chat_id,
            text=PCHILDREN_AGE,
            reply_markup=pupil_age_keyboard()
        )
    except:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_PCHILDREN
        )


@parent_router.message(StateFilter(Parent.wait_age))
async def handle_parent_age(message: Message, state: FSMContext):
    """Обрабатывает возраст пользователя """

    chat_id = message.chat.id
    age = message.text

    try:
        age = int(age)
        if (age > 3) and (age < 25):
            pchildren_data_repo.update_field(chat_id, "age", age)
        else:
            raise ValueError

        await state.set_state(Parent.wait_school_type)
        await bot.send_message(
            chat_id=chat_id,
            text=PARENT_SCHOOL_TYPE,
            reply_markup=pupil_school_type_keyboard()
        )

    except:
        await bot.send_message(
            chat_id=chat_id,
            text=PUPIL_ERROR_AGE
        )


@parent_router.message(StateFilter(Parent.wait_school_type), F.text.in_([school_types_buttons['school'], school_types_buttons['lyceum'], school_types_buttons['gymnasium']]))
async def handle_parent_school_type(message: Message, state: FSMContext):
    """Обрабатывает тип школы пользователя - ученик"""

    await state.set_state(Parent.wait_school)

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


@parent_router.message(StateFilter(Parent.wait_school), F.text == school_buttons[0])
async def handle_parent_back_school_type(message: Message, state: FSMContext):
    chat_id = message.chat.id
    await state.set_state(Parent.wait_school_type)
    await bot.send_message(
        chat_id=chat_id,
        text=PARENT_SCHOOL_TYPE,
        reply_markup=pupil_school_type_keyboard()
    )


@parent_router.message(StateFilter(Parent.wait_school))
async def handle_parent_school(message: Message, state: FSMContext):
    """Обрабатывает учебное заведение пользователя - ученик"""

    chat_id = message.chat.id
    school = message.text

    if (school in school_buttons) or (school in gymnasium_buttons) or (school in lyceum_buttons):

        await state.set_state(Parent.wait_grade)
        pchildren_data_repo.update_field(chat_id, "school", school)

        await bot.send_message(
            chat_id=chat_id,
            text=PARENT_GRADE_REQUEST,
            reply_markup=grade_keyboard()
        )

    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_SCHOOL
        )


@parent_router.message(StateFilter(Parent.wait_grade))
async def handle_parent_grade(message: Message, state: FSMContext):
    chat_id = message.chat.id
    grade = message.text

    try:
        grade = int(grade)
        if (grade > 0) and (grade < 12):
            pchildren_data_repo.update_field(chat_id, "grade", grade)
        else:
            raise ValueError
        await state.set_state(Parent.wait_exam)
        if grade > 9:
            exam = "ЕГЭ по информатике?"
        else:
            exam = "ОГЭ по информатике?"
        await bot.send_message(
            chat_id=chat_id,
            text=EXAM_REQUEST+exam,
            reply_markup=request_keyboard()
        )
    except:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_GRADE
        )


@parent_router.message(StateFilter(Parent.wait_exam))
async def handle_parent_exam(message: Message, state: FSMContext):
    """Обрабатывает вопрос о сдаче экзамена пользователя"""

    chat_id = message.chat.id
    exam = message.text
    if exam in answer_buttons:
        await state.set_state(Parent.wait_arrival)
        pchildren_data_repo.update_field(chat_id, "exam", exam)
        await bot.send_message(
            chat_id=chat_id,
            text=UNIVERSITY_REQUEST,
            reply_markup=request_keyboard()
        )

    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_BUTTON
        )


@parent_router.message(StateFilter(Parent.wait_arrival))
async def handle_parent_university(message: Message, state: FSMContext):
    """Обрабатывает вопрос о поступлении в ВУЗ"""

    chat_id = message.chat.id
    arrival = message.text
    if arrival in answer_buttons:
        pchildren_data_repo.update_field(chat_id, "arrival", arrival)
        if arrival == answer_buttons[0]:
            await state.set_state(Parent.wait_university)
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
            await state.set_state(Parent.wait_q2)
            await bot.send_message(
                chat_id=chat_id,
                text=PUPIL_Q2,
                reply_markup=request_keyboard()
            )
    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_BUTTON
        )


@parent_router.callback_query(StateFilter(Parent.wait_university), F.data == "next")
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
        await state.set_state(Parent.wait_q1)
        data_base_university = ""
        for i in range(len(university_list)):
            if i in check_list:
                data_base_university += university_list[i]+"; "
        pchildren_data_repo.update_field(chat_id, "university", data_base_university)
        await bot.edit_message_text(
            chat_id=chat_id,
            text="Вы выбрали:\n"+data_base_university,
            message_id=callback.message.message_id,
            reply_markup=None
        )
        await bot.send_message(
            chat_id=chat_id,
            text=PUPIL_Q1,
            reply_markup=request_keyboard()
        )


@parent_router.callback_query(StateFilter(Parent.wait_university))
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
        check_list.add(int(university))
    await state.update_data(check_list=list(check_list))
    await bot.edit_message_reply_markup(
        chat_id=chat_id,
        message_id=callback.message.message_id,
        reply_markup=university_keyboard(check_list)
    )


@parent_router.message(StateFilter(Parent.wait_q1))
async def handle_parent_q1(message: Message, state: FSMContext):
    """Планируете поступление на техническую специальность - ученик"""

    chat_id = message.chat.id
    answer = message.text
    if answer in answer_buttons:
        await state.set_state(Parent.wait_q2)
        pchildren_data_repo.update_field(chat_id, "technical_specialty", answer)
        await bot.send_message(
            chat_id=chat_id,
            text=PARENTS_Q2,
            reply_markup=request_keyboard()
        )

    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_BUTTON
        )


@parent_router.message(StateFilter(Parent.wait_q2))
async def handle_parent_q2(message: Message, state: FSMContext):
    chat_id = message.chat.id
    answer = message.text
    if answer in answer_buttons:
        await state.set_state(Parent.wait_q3)
        pchildren_data_repo.update_field(chat_id, "IT_live", answer)
        await bot.send_message(
            chat_id=chat_id,
            text=PARENTS_Q3,
            reply_markup=request_keyboard()
        )

    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_BUTTON
        )


@parent_router.message(StateFilter(Parent.wait_q3))
async def handle_parent_q3(message: Message, state: FSMContext):
    chat_id = message.chat.id
    answer = message.text
    if answer in answer_buttons:
        await state.set_state(Parent.wait_q4)
        pchildren_data_repo.update_field(chat_id, "training_IT", answer)
        pchildren_data_repo.update_field(chat_id, "check", True)
        await bot.send_message(
            chat_id=chat_id,
            text=NEW_CHILDREN,
            reply_markup=new_children_keyboard()
        )

    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_BUTTON
        )


@parent_router.message(StateFilter(Parent.wait_q4), F.text == new_children_buttons['yes'])
async def handle_parent_q4(message: Message, state: FSMContext):
    await state.set_state(Parent.wait_children_name)

    chat_id = message.chat.id

    try:
        response = parent_data_repo.get_user_by_chat_id(chat_id)
        if not response.data:
            pchildren_data_repo.insert_field(chat_id)
    except:
        pass

    await bot.send_message(
        chat_id=chat_id,
        text=PCHILDREN_NAME,
        reply_markup=ReplyKeyboardRemove()
    )


# =====================================================================================================================


@parent_router.message(StateFilter(Parent.wait_q4), F.text == new_children_buttons['next'])
async def handle_parent_q4(message: Message, state: FSMContext):
    await state.set_state(Parent.wait_q6)

    chat_id = message.chat.id

    await bot.send_message(
        chat_id=chat_id,
        text=PARENTS_Q6,
        reply_markup=keyboard_q6_parents()
    )


@parent_router.message(StateFilter(Parent.wait_q6))
async def handle_parent_q6(message: Message, state: FSMContext):
    chat_id = message.chat.id
    answer = message.text
    if answer in  parents_answer_q6:
        await state.set_state(Parent.wait_q7)
        parent_data_repo.update_field(chat_id, "support_children", answer)
        await bot.send_message(
            chat_id=chat_id,
            text=PARENTS_Q7,
            reply_markup=keyboard_q7_parents()
        )
    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_BUTTON
        )


@parent_router.message(StateFilter(Parent.wait_q7))
async def handle_parent_q7(message: Message, state: FSMContext):
    chat_id = message.chat.id
    answer = message.text
    if answer in  parents_answer_q7:
        await state.set_state(Parent.wait_q8)
        parent_data_repo.update_field(chat_id, "it_experience", answer)
        await bot.send_message(
            chat_id=chat_id,
            text=PARENTS_Q8,
            reply_markup=keyboard_q8_parents()
        )
    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_BUTTON
        )


@parent_router.message(StateFilter(Parent.wait_q8))
async def handle_parent_q8(message: Message, state: FSMContext):
    chat_id = message.chat.id
    answer = message.text
    if answer in parents_answer_q8:
        await state.set_state(Parent.wait_q9)
        parent_data_repo.update_field(chat_id, "child_advantages", answer)
        await bot.send_message(
            chat_id=chat_id,
            text=PARENTS_Q9,
            reply_markup=keyboard_q9_parents()
        )
    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_BUTTON
        )


@parent_router.message(StateFilter(Parent.wait_q9))
async def handle_parent_q9(message: Message, state: FSMContext):
    chat_id = message.chat.id
    answer = message.text
    if answer in parents_answer_q9:
        parent_data_repo.update_field(chat_id, "useful_skills", answer)
        await bot.send_message(
            chat_id=chat_id,
            text=THX_PARENTS_END,
            # reply_markup=keyboard_check_group_parents()
            reply_markup=ReplyKeyboardRemove()
        )

        await state.set_state(Parent.end)

        user_data = users_data_repo.get_user_by_chat_id(chat_id)
        user_data = user_data.data[0]
        parent_data = parent_data_repo.get_user_by_chat_id(chat_id)
        parent_data = parent_data.data[0]
        pchildren_data = pchildren_data_repo.get_user_by_chat_id_all(chat_id)
        pchildren_data = pchildren_data.data
        try:
            await bot.delete_message(
                chat_id=admin_group,
                message_id=user_data['message']
            )
            text = (f"Пользователь {message.chat.id} - @{message.from_user.username}"
                    f"\nФИО: {user_data['name']}"
                    f"\nРоль: {role_buttons['parent']}"
                    f"\nТелефон: +{user_data['tg_phone']}"
                    f"\nПоддержка ребенка в IT: {parent_data['support_children']}"
                    f"\nОпыт в IT: {parent_data['it_experience']}"
                    f"\nПреимущества ребенка в IT: {parent_data['child_advantages']}"
                    f"\nПолезные навыки в IT: {parent_data['useful_skills']}"
                    )
            await bot.send_message(
                chat_id=admin_group,
                message_thread_id=parent_thread,
                text=text
            )
            for pchildren in pchildren_data:
                text = (f"Родитель: {pchildren['chat_id']} - @{message.from_user.username}"
                        f"\nИмя ребенка: {pchildren['children_name']}"
                        f"\nВозраст: {pchildren['age']}"
                        f"\nШкола: {pchildren['school']}"
                        f"\nКласс: {pchildren['grade']}"
                        f"\nЕГЭ/ОГЭ: {pchildren['exam']}"
                        f"\nПоступление в ВУЗ: {pchildren['arrival']}"
                        f"\nУниверситеты: {pchildren['university']}"
                        f"\nТехническая специальность: {pchildren['technical_specialty']}"
                        f"\nСвязать жизнь с IT: {pchildren['IT_live']}"
                        f"\nЗанимается ли ребенок IT: {pchildren['training_IT']}")
                await bot.send_message(chat_id=admin_group,
                                       message_thread_id=parent_thread,
                                       text=text
                                       )

        except Exception as e:
            print(e)
    else:
        await bot.send_message(
            chat_id=chat_id,
            text=ERROR_BUTTON
        )


# @parent_router.message(StateFilter(Parent.wait_group), F.text == check_group_buttons["present"])
# async def handle_parent_wait_group(message: Message, state: FSMContext):
#     chat_id = message.chat.id
#     # Проверяем статус пользователя в канале
#     chat_member = await bot.get_chat_member(chat_id=channel_id, user_id=chat_id)
#
#     if chat_member.status in ['member', 'administrator', 'creator']:
#         try:
#             # Отправка подарка
#             await bot.send_message(
#                 chat_id=chat_id,
#                 text=PARENT_PRESENT,
#                 reply_markup=keyboard_check_present_parents()
#             )
#             await bot.send_message(
#                 chat_id=admin_group,
#                 message_thread_id=group_thread,
#                 text=f"Пользователь {str(chat_id)} - @{message.from_user.username} подписался на группу!"
#             )
#             await state.set_state(Parent.wait_present)
#         except:
#             pass
#     else:
#         try:
#             await bot.send_message(chat_id=chat_id,
#                                    text=REPEAT_PARENTS
#                                    )
#         except:
#             pass
#
#
# @parent_router.message(StateFilter(Parent.wait_present), F.text == check_group_buttons["give_me"])
# async def handle_parent_wait_present(message: Message, state: FSMContext):
#     chat_id = message.chat.id
#     await bot.send_message(
#         chat_id=chat_id,
#         text=PARENT_GIVE,
#         reply_markup=ReplyKeyboardRemove()
#     )
#     await state.clear()
#     parent_data = parent_data_repo.get_user_by_chat_id(chat_id)
#     parent_data = parent_data.data[0]
#     pchildren_data = pchildren_data_repo.get_user_by_chat_id_all(chat_id)
#     pchildren_data = pchildren_data.data
#     text = f"Пользователь {str(chat_id)} - @{message.from_user.username} хочет получить подарок!\n\nДанные пользователя:\n"
#     for key, value in parent_data.items():
#         text += f"{key.replace('_', ' ').capitalize()}: {value}\n"
#     await bot.send_message(
#         chat_id=admin_group,
#         message_thread_id=present_thread,
#         text=text
#     )
#     text = "Дети:\n"
#     for pchildren in pchildren_data:
#         for key, value in pchildren.items():
#             text += f"{key.replace('_', ' ').capitalize()}: {value}\n"
#         await bot.send_message(
#             chat_id=admin_group,
#             message_thread_id=present_thread,
#             text=text
#         )
#         text = ""
