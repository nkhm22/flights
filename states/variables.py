from telebot.handler_backends import State, StatesGroup


class Variables(StatesGroup):
    min_price = State()
    max_price = State()
    start_price = State()
    end_price = State()
