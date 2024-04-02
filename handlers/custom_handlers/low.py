import pprint

from loader import bot
from telebot.types import Message
import requests
import json
from config_data import config
from states.variables import Variables



@bot.message_handler(commands=['low'])
def low(message: Message):
    bot.set_state(message.from_user.id, Variables.min_price, message.chat.id)
    bot.send_message(message.chat.id, 'Введите требуемое количество самых дешевых вариантов:')


@bot.message_handler(state=Variables.min_price)
def get_low(message: Message):
    with (message.from_user.id, message.chat.id) as data:
        data['min_pr'] = Variables.min_price
    result_minimum = requests.get(
            f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin=VKO&destination=TBS&departure_at=2024-07-11&return_at=2024-07-20&unique=false&sorting=price&direct=false&cy=usd&limit={int(Variables.min_price)}&page=1&one_way=true&token={config.RAPID_API_KEY}")
    json_dict_minimum = json.loads(result_minimum.text)
    pprint.pprint(json_dict_minimum)
    for element in json_dict_minimum['data']:
        price = element['price']
        departure_at = element['departure_at']
        return_at = element['return_at']
        bot.send_message(message.from_user.id, f'Дата и время вылета в Тбилиси: {departure_at}\n'
                                          f'Дата и время возвращения в Москву (Внуково): {return_at}\n'
                                          f'Стоимость билетов в рублях: {price}\n', message.chat.id)
