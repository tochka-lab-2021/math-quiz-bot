import telebot

f = open("token.txt", "r")
token = f.read()
bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


if __name__ == "__main__":
    bot.polling()
