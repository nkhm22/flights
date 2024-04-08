import sqlite3
from loader import bot
import os


def for_history(text, date_time, user):

    # Функция для добавления в базу данных команд от пользователя для вывода истории

    connection = sqlite3.connect(os.path.join("database", "my_database.db"))
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Commands (text, date_time, user) VALUES (?, ?, ?)',
                   (text, date_time, user))
    connection.commit()
    connection.close()


@bot.message_handler(commands=["history"])
def history(message):

    # Функция для вывода истории

    conn = sqlite3.connect(os.path.join("database", "my_database.db"))
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Commands ORDER BY date_time DESC')
    users = cursor.fetchall()
    count = 0
    for user in users:
        if str(user[3]) == str(message.from_user.full_name):
            count += 1
            bot.send_message(message.chat.id, f'Команда: {str(user[1])}, дата и время запроса: {str(user[2])}')
            if count == 10:
                break
    conn.commit()
    conn.close()
    bot.send_message(message.chat.id, '/help')
