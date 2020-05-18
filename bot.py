import telebot
import config

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])  #Отвечает на команду старт
def welcome(massage):
    bot.send_message(massage.chat.id,'Добро пожаловать, рада что ты решил выбрать этот курс, но перед началом нужно познакомиться!')


#RUN
bot.polling(none_stop=True)