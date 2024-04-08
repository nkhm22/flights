from loader import bot
import handlers  # noqa
from utils.set_bot_commands import set_default_commands
from telebot.custom_filters import StateFilter
import sqlite3
import os


if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.polling()
con = sqlite3.connect(os.path.join('database', 'my_database.db'))
with con:
    con.execute("""
        CREATE TABLE Commands (
           text TEXT,
           date_time TEXT,
           user TEXT

);
    """),
con.execute("""
        CREATE TABLE dates (
           to_tbs TEXT,
           from_tbs TEXT,
           date_time TEXT,
           user TEXT,
           city_from,
           city_to

);
    """)
