import logic
import telebot
from telebot import types

bot = telebot.TeleBot("5671829224:AAE1b8kEKqrYf4rtGFMCCld3jSJITndJOtw")

@bot.message_handler(commands=['start'])
def give_menu(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('♻️ Сбор вторсырья')
    btn2 = types.KeyboardButton('🌿 Эко-инициативы')
    btn3 = types.KeyboardButton('🐾 Полезные эко-привычки')
    btn4 = types.KeyboardButton('❗️ Почему это важно')
    kb.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, text="Выбери действие из меню ниже:", reply_markup=kb)
