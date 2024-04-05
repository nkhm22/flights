from telebot.types import Message
from loader import bot
from handlers.custom_handlers import history
import datetime


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.send_message(message.chat.id,
    f"Привет, {message.from_user.full_name}!"
    f" Я покажу тебе информацию об авиарейсах из Москвы (Внуково) в Тбилиси и обратно /help")
    history.for_history(message.text, datetime.datetime.now(), message.from_user.full_name)
