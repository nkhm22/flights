from telebot.types import Message
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.send_message(message,
    f"Привет, {message.from_user.full_name}! Я покажу тебе информацию об авиарейсах из Внуково в Тбилиси и обратно")
