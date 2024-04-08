from loader import bot
from telebot.types import Message
from states.variables import Variables
from api import api
import datetime
from handlers.custom_handlers import history


@bot.message_handler(commands=['low'])
def low(message: Message):

    # Запрос требуемого количества самых дешевых вариантов

    bot.set_state(message.from_user.id, Variables.min_price, message.chat.id)
    bot.send_message(message.from_user.id, 'Введите требуемое количество самых дешевых вариантов:')
    datetime.datetime.now()
    history.for_history(message.text, datetime.datetime.now(), message.from_user.full_name)


@bot.message_handler(state=Variables.min_price)
def get_low(message: Message):

    # Вывод требуемого количества самых дешевых вариантов

    if message.text.isdigit():
        json_dict = api.api_date()
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['min_price'] = message.text
        for element in json_dict['data'][0:int(data['min_price'])]:
            price = element['price']
            departure_at = element['departure_at']
            return_at = element['return_at']
            bot.send_message(message.from_user.id, f'Дата и время вылета: {departure_at}\n'
                                                   f'Дата и время возвращения: {return_at}\n'
                                                   f'Стоимость билетов в рублях: {price}\n')
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.from_user.id, 'Количество должно быть числом')
