from loader import bot
from telebot.types import Message
import requests
import json
from config_data import config
from states.variables import Variables


@bot.message_handler(commands=['custom'])
def custom(message: Message) -> None:
    bot.send_message(message.from_user.id, 'Введите диапазон вариантов цен через пробел:')
    bot.set_state(message.from_user.id, Variables.custom_price, message.chat.id)


@bot.message_handler(state=Variables.custom_price)
def get_custom(message: Message) -> None:
    res_max = requests.get(
    f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin=VKO&destination=TBS&departure_at=2024-07-11&return_at=2024-07-20&unique=false&sorting=price&direct=false&cy=usd&page=1&one_way=true&token={config.RAPID_API_KEY}")
    json_dict_max = json.loads(res_max.text)
    for elem in json_dict_max['data'][(int(Variables.custom_price.split()[0])):(int(Variables.custom_price.split()[1]))]:
        price = elem['price']
        departure_at = elem['departure_at']
        return_at = elem['return_at']
        bot.send_message(message.chat.id, f'Дата и время вылета в Тбилиси: {departure_at}\n'
                                          f'Дата и время возврата в Москву (Внуково): {return_at}\n'
                                          f'Стоимость билетов: {price}\n')