from aiogram.fsm.state import State, StatesGroup


class Pupil(StatesGroup):
    wait_age = State()
    wait_school_type = State()
    wait_school = State()
    wait_grade = State()
    wait_exam = State()
    wait_arrival = State()
    wait_university = State()
    wait_q1 = State()
    wait_q2 = State()
    wait_q3 = State()
    wait_q4 = State()
    wait_q5 = State()
    wait_q6 = State()
    wait_group = State()
    wait_present = State()
    test = State()
    end = State()
