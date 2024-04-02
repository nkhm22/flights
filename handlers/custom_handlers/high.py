from loader import bot
from telebot.types import Message
import requests
import json
from config_data import config
from states.variables import Variables


@bot.message_handler(commands=['high'])
def high(message: Message) -> None:
    bot.set_state(message.from_user.id, Variables.max_price, message.chat.id)
    bot.send_message(message.chat.id, 'Введите требуемое количество самых дорогих вариантов:')


@bot.message_handler(state=Variables.max_price)
def get_high(message: Message) -> None:
    res_max = requests.get(
    f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin=VKO&destination=TBS&departure_at=2024-07-11&return_at=2024-07-20&unique=false&sorting=price&direct=false&cy=usd&page=1&one_way=true&token={config.RAPID_API_KEY}")
    json_dict_max = json.loads(res_max.text)
    for elem in json_dict_max['data'][(len(json_dict_max['data']) - int(Variables.max_price)):len(json_dict_max['data'])]:
        price = elem['price']
        departure_at = elem['departure_at']
        return_at = elem['return_at']
        bot.send_message(message.chat.id, f'Дата и время вылета в Тбилиси: {departure_at}\n'
                                          f'Дата и время возврата в Москву (Внуково): {return_at}\n'
                                          f'Стоимость билетов: {price}\n')
