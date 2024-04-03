from loader import bot
from telebot.types import Message
from states.variables import Variables
from api import api


@bot.message_handler(commands=['low'])
def low(message: Message):
    bot.set_state(message.from_user.id, Variables.min_price, message.chat.id)
    bot.send_message(message.from_user.id, 'Введите требуемое количество самых дешевых вариантов:')


@bot.message_handler(state=Variables.min_price)
def get_low(message: Message):
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['min_price'] = message.text
    for element in api.json_dict['data'][0:int(data['min_price'])]:
        price = element['price']
        departure_at = element['departure_at']
        return_at = element['return_at']
        bot.send_message(message.from_user.id, f'Дата и время вылета в Тбилиси: {departure_at}\n'
                                               f'Дата и время возвращения в Москву (Внуково): {return_at}\n'
                                               f'Стоимость билетов в рублях: {price}\n')
    bot.delete_state(message.from_user.id, message.chat.id)
