from telebot.types import Message
from handlers.custom_handlers import history
import datetime
from config_data.config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message_help: Message):
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message_help, "\n".join(text))
    history.for_history(message_help.text, datetime.datetime.now(), message_help.from_user.full_name)
