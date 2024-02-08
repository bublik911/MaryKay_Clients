from aiogram.fsm.state import StatesGroup, State


class Transition(StatesGroup):
    transition = State()


class Start(Transition):
    client = State()
