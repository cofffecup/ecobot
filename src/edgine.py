import interface
#import telebot

try:
    interface.bot.polling()
except Exception as ex:
    print("err: ", ex)
