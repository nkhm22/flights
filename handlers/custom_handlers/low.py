from loader import bot
from states.cont import Usinfo
from telebot.types import Message
import requests
import json
import os


@bot.message_handler(commands=['low'])
def low(message: Message) -> None:
    bot.set_state(message.from_user.id, Usinfo.min_pr, message.chat.id)
    bot.send_message(message.chat.id, 'Введите требуемое количество самых дешевых вариантов:')


@bot.message_handler(state=Usinfo.min_pr)
def get_low(message: Message) -> None:
    #key_api = os.getenv("RAPID_API_KEY")
    res_min = requests.get(
        f"https://api.travelpayouts.com/aviasales/v3/prices_for_dates?origin=VKO&destination=TBS&departure_at=2024-07-11&return_at=2024-07-20&unique=false&sorting=price&direct=false&cy=usd&limit={Usinfo.min_pr}&page=1&one_way=true&token=f7b597efadfaf8287ec2a27842a00b76")
    json_dict_min = json.loads(res_min.text)
    for elem in json_dict_min['data']:
        datetime_ = elem['airline']
        bot.send_message(message.chat.id, f'Дата и время отправления: {datetime_}')
        bot.set_state(message.from_user.id, Usinfo.min_pr, message.from_user.id)