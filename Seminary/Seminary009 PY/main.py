import telebot


bot = telebot.TeleBot("5767655379:AAHv9qumtFLr4xfBxAew2gQqNPiNa2gbe1E")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


def deleting(text):
    while text.find('абв') != -1:
        text = text.replace('абв', '')
    if len(text) == 0:
        text = '¯\_(ツ)_/¯'
    return text


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, deleting(message.text))


bot.infinity_polling()
