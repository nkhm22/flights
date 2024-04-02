from telebot.handler_backends import State, StatesGroup


class Variables(StatesGroup):
    min_price = State()
    max_price = State()
    custom_price = State()
