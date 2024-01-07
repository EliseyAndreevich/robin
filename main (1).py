# -*- coding: utf8 -*-
import telebot
import datetime
from telebot import types
from settings import TG_TOKEN
from urllib.request import urlopen
# Загружаем список интересных фактов

# Создаем бота
bot = telebot.TeleBot(TG_TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
        current_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=3)))  # Minsk time
        hour = current_time.hour
        if 7 <= hour < 12:
            greeting = "🌞Доброе утро"
        elif 12 <= hour < 18:
            greeting = "🌞Добрый день"
        elif 18 <= hour < 21:
            greeting = "🌚Добрый вечер"
        else:
            greeting = "🌚Доброй ночи"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("👉О чемпионате")
        item2 = types.KeyboardButton("🌐Сайт")
        item3 = types.KeyboardButton("📃Компетенции")
        item4 = types.KeyboardButton("📞Контакты")
        markup.add(item1, item2, item3, item4)
        bot.send_message(message.chat.id, f'😀 | {greeting},\nЭто телеграм бот IT-чемпионата "РобИн"\nНажми: \n👉О чемпионате — для получения подробной информации\n🌍Сайт - для перехода на сайт чемпионата ', reply_markup=markup)
# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == '👉О чемпионате':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item3 = types.KeyboardButton("👈Назад")
            markup.add(item3)
            bot.send_message(message.chat.id, "Республиканский открытый IT-чемпионат «РобИн-2024»\n\nВ эпоху современных технологий огромное внимание уделяется развитию искусственного интеллекта, робототехническим системам, виртуальной и дополненной реальностям. Ни для кого не секрет, что данные IT-сферы повсеместно внедряются в образование. Для того, чтобы подрастающее поколение Беларуси могло продемонстрировать свои достижения в этих областях, в НДЦ «Зубренок» реализуется IT-чемпионат «РобИн».", reply_markup=markup)
    elif message.text.strip() == '/about':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("👈Назад")
        markup.add(item3)
        bot.send_message(message.chat.id,"Республиканский открытый IT-чемпионат «РобИн-2024»\n\nВ эпоху современных технологий огромное внимание уделяется развитию искусственного интеллекта, робототехническим системам, виртуальной и дополненной реальностям. Ни для кого не секрет, что данные IT-сферы повсеместно внедряются в образование. Для того, чтобы подрастающее поколение Беларуси могло продемонстрировать свои достижения в этих областях, в НДЦ «Зубренок» реализуется IT-чемпионат «РобИн».", reply_markup=markup)
    # Если юзер прислал 2, выдаем умную мысль
    elif message.text.strip() == '🌐Сайт':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("👈Назад")
        markup.add(item3)
        markup = types.InlineKeyboardMarkup()
        item4 = types.InlineKeyboardButton("Сайт 'РобИн-2024'", url="https://robin-zubronok.by")
        item5 = types.InlineKeyboardButton("Сайт НДЦ «Зубренок»", url="https://zubronok.by")
        markup.add(item4, item5)
        bot.send_message(message.chat.id, "🌐Ссылки на сайты ниже 👇", reply_markup=markup)

    elif message.text.strip() == '/site':
        answer = "https://robin-zubronok.by"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("👈Назад")
        markup.add(item3)
        markup = types.InlineKeyboardMarkup()
        item4 = types.InlineKeyboardButton("Сайт 'РобИн-2024'", url="https://robin-zubronok.by")
        item5 = types.InlineKeyboardButton("Сайт НДЦ «Зубренок»", url="https://zubronok.by")
        markup.add(item4, item5)
        bot.send_message(message.chat.id, "🌐Ссылки на сайты ниже 👇", reply_markup=markup)

    elif message.text.strip() == '👈Назад':
        start(message)

    elif message.text.strip() == '/help':
        admin_username = 'Sergei_Nikitka'  # Пример юзернейма администратора
        help_text = "Это телеграм бот чемпионата 'РобИн'\n\n" \
                    "Подробнее о чемпионтае - /about или 👉О чемпионате \n" \
                    "Сайты - /site или 🌐Сайт \n\n" \
                    "Контакты - /contacts или 📞Контакты \n\n" \
                    "Компетенции - /competencies или 📃Компетенции \n\n" \
                    f"Для связи с разработчиком обратитесь к @{admin_username}"
        markup = types.InlineKeyboardMarkup()
        item4 = types.InlineKeyboardButton("Сайт 'РобИн-2024'", url="https://robin-zubronok.by")
        item5 = types.InlineKeyboardButton("Сайт НДЦ «Зубренок»", url="https://zubronok.by")
        markup.add(item4, item5)
        bot.send_message(message.chat.id, help_text, reply_markup=markup)

    elif message.text.strip() == '📞Контакты':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("👈Назад")
        markup.add(item3)
        markup = types.InlineKeyboardMarkup()
        item5 = types.InlineKeyboardButton("Telegram канал", url="https://t.me/NCC_Zubronok_by")
        item6 = types.InlineKeyboardButton("Instagram", url="https://intagram.com/@dvorets_zubrenok")
        item7 = types.InlineKeyboardButton("Tik-Tok", url="https://www.tiktok.com/@robolizer_zubrenok")
        markup.add(item5, item6, item7)
        bot.send_message(message.chat.id,"📩Социальные сети и контакты\n\n📧Email - profil@zubronok.by", reply_markup=markup)

    elif message.text.strip() == '📃Компетенции':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("👈Назад")
        markup.add(item3)
        bot.send_message(message.chat.id, "Компетенции:\n\n🥋Интеллектуаальное суммо\n✈️Большое путешествие\n⚽Робофутбол 2х2\n✍Графический дизайн\n🔧Прототипирование сайта\n🌐WEB-разработка\n👨‍🔧Инжинерный дизайн CAD\n🛠️Прототипирование младшая категория\n🛠️Прототипирование старшая категория\n</>Спортивное программирование", reply_markup=markup)
    elif message.text.strip() == '/contacts':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("👈Назад")
        markup.add(item3)
        bot.send_message(message.chat.id,"Социальные сети и контакты\n\nTelegram канал: @NCC_Zubronok_by\nInstagram: @dvorets_zubrenok\nTik-Tok: @robolizer_zubrenok\n\nemail - profil@zubronok.by", reply_markup=markup)

    elif message.text.strip() == '/competencies':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item3 = types.KeyboardButton("👈Назад")
        markup.add(item3)
        bot.send_message(message.chat.id, "Компетенции:\n\n🥋Интеллектуаальное суммо\n✈️Большое путешествие\n⚽Робофутбол 2х2\n✍Графический дизайн\n🔧Прототипирование сайта\n🌐WEB-разработка\n👨‍🔧Инжинерный дизайн CAD\n🛠️Прототипирование младшая категория\n🛠️Прототипирование старшая категория\n</>Спортивное программирование", reply_markup=markup)

    else:

        bot.send_message(message.chat.id, "Команда не найдена\n/help для помощи")


# Запускаем бота
bot.infinity_polling()