from telebot.handler_backends import State, StatesGroup


class Variables(StatesGroup):
    min_pr = State()
    max_pr = State()
    custom_pr = State()
