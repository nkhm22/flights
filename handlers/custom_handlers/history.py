import sqlite3
from loader import bot


def for_history(text, date_time, user):
    connection = sqlite3.connect('my_database.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Commands (text, date_time, user) VALUES (?, ?, ?)',
                   (text, date_time, user))
    connection.commit()
    connection.close()


@bot.message_handler(commands=["history"])
def get_users(message):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Commands ORDER BY date_time DESC LIMIT 10')
    users = cursor.fetchall()
    users_str = "\n".join([str(user[0]) for user in users])
    bot.send_message(message.chat.id, users_str)
    conn.close()

