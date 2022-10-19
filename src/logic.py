import db
from telebot import types


def menu_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton('♻️ Сбор вторсырья')
    btn2 = types.KeyboardButton('🌿 Эко-инициативы')
    btn3 = types.KeyboardButton('🐾 Полезные эко-привычки')
    btn4 = types.KeyboardButton('❗️ Почему это важно')
    kb.add(btn1, btn2, btn3, btn4)
    return kb


def first_chapter_buttons():
    btn1 = types.InlineKeyboardButton(text='Карта пунктов сбора вторсырья', callback_data='map')
    btn2 = types.InlineKeyboardButton(text='Мероприятия по массовому сбору мусора', callback_data='ivent')
    btn3 = types.InlineKeyboardButton(text='Информация о раздельном сборе мусора', callback_data='trash_info')
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(btn1, btn2, btn3)
    return kb


def second_chapter_buttons():
    btn1 = types.InlineKeyboardButton(text='Эко-организации', callback_data='organizations')
    btn2 = types.InlineKeyboardButton(text='Приложения для смартфонов', callback_data='apps')
    btn3 = types.InlineKeyboardButton(text='Маркеты и магазины эко-товаров', callback_data='markets')
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(btn1, btn2, btn3)
    return kb


def third_chapter_buttons():
    btn1 = types.InlineKeyboardButton(text='Отказ от одноразового', callback_data='rejection')
    btn2 = types.InlineKeyboardButton(text='Сортировка мусора', callback_data='sorting')
    btn3 = types.InlineKeyboardButton(text='Повторное использование', callback_data='reuse')
    btn4 = types.InlineKeyboardButton(text='Экономия ресурсов', callback_data='saving')
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(btn1, btn2, btn3, btn4)
    return kb


def fourth_chapter_buttons():
    btn1 = types.InlineKeyboardButton(text='Статьи', callback_data='article')
    btn2 = types.InlineKeyboardButton(text='Видео', callback_data='video')
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(btn1, btn2)
    return kb


