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
    if message.text == 'ecoadminmode':
        admin_panel(message)
    else:
        if message.text == '♻️ Сбор вторсырья':
            kb = logic.first_chapter_buttons()
        elif message.text == '🌿 Эко-инициативы':
            kb = logic.second_chapter_buttons()
        elif message.text == '🐾 Полезные эко-привычки':
            kb = logic.third_chapter_buttons()
        elif message.text == '❗️ Почему это важно':
            kb = logic.fourth_chapter_buttons()
        bot.send_message(message.chat.id, text="Выберите то, о чем вы хотите узнать подробнее:", reply_markup=kb)


def admin_panel(message):
    bot.send_message(message.chat.id, text="Выбер")


@bot.callback_query_handler(func=lambda message: True)

# 1 - Информация о раздельном сборе
# 2 - Мероприятия по массовому сбору мусора
# 3 - Карта пунктов сбора вторсырья
# 4 - Маркеты и магазины эко-товаров
# 5 - Приложения для смартфонов
# 6 - Эко-организации
# 7 - Экономия ресурсов
# 8 - Повторное использование
# 9 - Сортировка мусора
# 10 - Отказ от одноразового
# 11 - Видео
# 12 - Статьи

def callback_parser(call):
    num = 0
    if call.data == 'map':
        num = 3
    elif call.data == 'ivent':
        num = 2
    elif call.data == 'trash_info':
        pass
    elif call.data == 'organizations':
        num = 6
    elif call.data == 'apps':
        num = 5
    elif call.data == 'markets':
        num = 4
    elif call.data == 'rejection':
        num = 7
    elif call.data == 'sorting':
        num = 9
    elif call.data == 'reuse':
        num = 8
    elif call.data == 'saving':
        num = 10
    elif call.data == 'article':
        num = 12
    elif call.data == 'video':
        num = 11
    if num != 0:
        message_text = logic.get_text(num)
        for line in message_text:
            bot.send_message(call.message.chat.id, text=line)

