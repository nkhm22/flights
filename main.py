import telebot


token = '7064044877:AAG555RP-syUUpNR4deFkQLl7Z_4qHFfMc4'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет")


@bot.message_handler(commands=['helloworld'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello world')


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == 'привет' or 'Привет':
        bot.send_message(chat_id, 'Здравствуйте!')


bot.polling()
