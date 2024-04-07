from telebot.types import Message
from loader import bot
from handlers.custom_handlers import history
import datetime
from states.variables import Variables
import sqlite3
import os


@bot.message_handler(commands=["start"])
def bot_start(message: Message): #Приветствие бота и запрос даты отправления
    bot.set_state(message.from_user.id, Variables.date_to, message.chat.id)
    bot.send_message(message.chat.id,
    f"Привет, {message.from_user.full_name}!"
    f" Я покажу тебе информацию об "
    f"авиарейсах из Москвы (Внуково) в Тбилиси и обратно. Введите дату вылета в Тбилиси в формате ГГГГ-ММ-ДД /help")
    history.for_history(message.text, datetime.datetime.now(), message.from_user.full_name)


@bot.message_handler(state=Variables.date_to)
def from_tbs(message): #Запрос даты возвращения
    bot.send_message(message.chat.id, 'Введите дату вылета обратно в формате ГГГГ-ММ-ДД')
    bot.set_state(message.from_user.id, Variables.date_from, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['date_to'] = message.text


@bot.message_handler(state=Variables.date_from)
def memory_dates(message): #Внесение в базу данных дат отправления и возвращения
    bot.set_state(message.from_user.id, Variables.date_from, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['date_from'] = message.text
    connection = sqlite3.connect(os.path.join("database", "my_database.db"))
    cur = connection.cursor()
    cur.execute('INSERT INTO dates (to_tbs, from_tbs, user, date_time) VALUES (?, ?, ?, ?)',
               (data['date_to'], data['date_from'], message.from_user.full_name, datetime.datetime.now()))
    connection.commit()
    connection.close()
    bot.delete_state(message.from_user.id, message.chat.id)
