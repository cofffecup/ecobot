import logic
import telebot
from telebot import types

bot = telebot.TeleBot("5671829224:AAE1b8kEKqrYf4rtGFMCCld3jSJITndJOtw")


@bot.message_handler(commands=['start'])
def give_menu(message):
    kb = logic.menu_buttons()
    bot.send_message(message.chat.id, text="Выбери действие из меню:", reply_markup=kb)


@bot.message_handler(content_types=['text'])
def menu_parser(message):
    if message.text == '♻️ Сбор вторсырья':
        kb = logic.first_chapter_buttons()
    elif message.text == '🌿 Эко-инициативы':
        kb = logic.second_chapter_buttons()
    elif message.text == '🐾 Полезные эко-привычки':
        kb = logic.third_chapter_buttons()
    elif message.text == '❗️ Почему это важно':
        kb = logic.fourth_chapter_buttons()
    bot.send_message(message.chat.id, text="Выберите то, о чем вы хотите узнать подробнее:", reply_markup=kb)


@bot.callback_query_handler(func=lambda message: True)
def callback_parser(call):
    if call.data == 'map':
        pass
    elif call.data == 'ivent':
        pass
    elif call.data == 'trash_info':
        pass
    elif call.data == 'organizations':
        pass
    elif call.data == 'apps':
        pass
    elif call.data == 'markets':
        pass
    elif call.data == 'rejection':
        pass
    elif call.data == 'sorting':
        pass
    elif call.data == 'reuse':
        pass
    elif call.data == 'saving':
        pass

