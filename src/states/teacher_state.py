from aiogram.fsm.state import State, StatesGroup


class Teacher(StatesGroup):
    wait_contact_data = State()
    wait_school_type = State()
    wait_school = State()
    wait_children_count = State()
    wait_q1 = State()
    wait_q2 = State()
    wait_q3 = State()
    wait_q4 = State()
    wait_q5 = State()
    wait_q6 = State()

