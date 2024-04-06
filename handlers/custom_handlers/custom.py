from loader import bot
from telebot.types import Message
from api import api
from states.variables import Variables
from handlers.custom_handlers import history
import datetime


@bot.message_handler(commands=['custom'])
def custom_start(message: Message) -> None:
    bot.set_state(message.from_user.id, Variables.start_price, message.chat.id)
    bot.send_message(message.chat.id, 'Задайте диапазон цен(введите нижнюю границу):')
    history.for_history(message.text, datetime.datetime.now(), message.from_user.full_name)


@bot.message_handler(state=Variables.start_price)
def custom_end(message: Message) -> None:
    if message.text.isdigit():
        bot.set_state(message.from_user.id, Variables.end_price, message.chat.id)
        bot.send_message(message.chat.id, "Введите верхнюю границу")
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['start_price'] = message.text
    else:
        bot.send_message(message.from_user.id, 'Введите цену в рублях')


@bot.message_handler(state=Variables.end_price)
def get_custom(message: Message) -> None:
    if message.text.isdigit():
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['end_price'] = message.text
            for elem in api.json_dict['data']:
                if elem['price'] <= int(data['end_price']) and elem['price'] >= int(data['start_price']):
                    price = elem['price']
                    departure_at = elem['departure_at']
                    return_at = elem['return_at']
                    bot.send_message(message.chat.id, f'Дата и время вылета в Тбилиси: {departure_at}\n'
                                                      f'Дата и время возврата в Москву (Внуково): {return_at}\n'
                                                      f'Стоимость билетов: {price}\n')

    else:
        bot.send_message(message.from_user.id, 'Введите цену в рублях')
    bot.delete_state(message.from_user.id, message.chat.id)
