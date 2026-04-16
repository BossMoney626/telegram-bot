import telebot

TOKEN = "8619269604:AAEwJc0JAAyN1GoaX1BQnwwodwYWHnZ8veU"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Your bot is working!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

bot.polling()
