from telebot.types import Message
from loader import bot
from handlers.custom_handlers import history
import datetime
from states.variables import Variables
import sqlite3
import os


@bot.message_handler(commands=["start"])
def bot_start(message: Message):

    # Приветствие бота и запрос даты отправления

    bot.set_state(message.from_user.id, Variables.date_to, message.chat.id)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.full_name}!"
                                      f" Я покажу тебе информацию об "
                                      f"авиарейсах на заданные даты. Введите дату вылета в формате ГГГГ-ММ-ДД:")
    history.for_history(message.text, datetime.datetime.now(), message.from_user.full_name)


@bot.message_handler(state=Variables.date_to)
def from_tbs(message):

    # Запрос даты возвращения

    try:
        datetime.datetime.strptime(message.text, "%Y-%m-%d")
        bot.send_message(message.chat.id, 'Введите дату вылета обратно в формате ГГГГ-ММ-ДД')
        bot.set_state(message.from_user.id, Variables.date_from, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['date_to'] = message.text
    except ValueError:
        bot.send_message(message.chat.id, "Дата некорректна")


@bot.message_handler(state=Variables.date_from)
def memory_dates(message):

    # Запрос аэропорта отправления

    try:
        datetime.datetime.strptime(message.text, "%Y-%m-%d")
        bot.send_message(message.chat.id, 'Введите код аэропорта отправления ИАТА:')
        bot.set_state(message.from_user.id, Variables.aero_from, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['date_from'] = message.text
    except ValueError:
        bot.send_message(message.chat.id, "Дата некорректна")


@bot.message_handler(state=Variables.aero_from)
def memory_dates(message):

    # Запрос аэропорта назначения

    if len(message.text) == 3:
        bot.send_message(message.chat.id, 'Введите код аэропорта назначения ИАТА:')
        bot.set_state(message.from_user.id, Variables.aero_to, message.chat.id)
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['aero_from'] = message.text
    else:
        bot.send_message(message.chat.id, "Код некорректeн")


@bot.message_handler(state=Variables.aero_to)
def memory_dates(message):

    # Запрос аэропорта назначения и внесение в базу

    if len(message.text) == 3:
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['aero_to'] = message.text
        connection = sqlite3.connect(os.path.join("database", "my_database.db"))
        cur = connection.cursor()
        cur.execute('INSERT INTO dates '
                    '(to_tbs, from_tbs, user, date_time, city_from, city_to) VALUES (?, ?, ?, ?, ?, ?)',
                    (data['date_to'], data['date_from'], message.from_user.full_name, datetime.datetime.now(),
                     data['aero_from'], data['aero_to']))
        connection.commit()
        connection.close()
        bot.send_message(message.chat.id, '/help')
        bot.delete_state(message.from_user.id, message.chat.id)
    else:
        bot.send_message(message.chat.id, "Код некорректeн")
