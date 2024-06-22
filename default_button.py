from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from db import Database

menu_keyboard = ReplyKeyboardMarkup([
    [KeyboardButton("меню изображений 📸"), KeyboardButton("фильм 🎞"), KeyboardButton("Mansur's | blog💻")],
    [KeyboardButton("музыкальное меню 🎵"), KeyboardButton("меню истории 🔍"), KeyboardButton("меню новостей 📰🗞")],
    [KeyboardButton("Instagram")],
    [KeyboardButton("Tik tok")],
        ],
    resize_keyboard=True)

# menu_detail = ReplyKeyboardMarkup(resize_keyboard=True)
# menu_detail.add(KeyboardButton("изображений 📸"), KeyboardButton("фильм 🎞"), KeyboardButton("Mansur's | blog💻"))
# menu_detail.add(KeyboardButton("музыка 🎵"), KeyboardButton("истории 🔍"), KeyboardButton("новостей 📰🗞"))
# menu_detail.add(KeyboardButton("Instagram"))
# menu_detail.add(KeyboardButton("Tik tok"))
# menu_detail.add(KeyboardButton("назад"))
#
# product_button = ReplyKeyboardMarkup(resize_keyboard=True)
# product_button.add(KeyboardButton("назад"))

menu_photo = ReplyKeyboardMarkup(resize_keyboard=True)
menu_photo.add(KeyboardButton("Природа 🏕"), KeyboardButton("Рабочий стол 💻"))
menu_photo.add(KeyboardButton("Город 🏙"), KeyboardButton("Море 🌊"))
menu_photo.add(KeyboardButton("Космос 🪐"), KeyboardButton("Луна 🌙"))
menu_photo.add(KeyboardButton("назад"))

product_button = ReplyKeyboardMarkup(resize_keyboard=True)
product_button.add(KeyboardButton("назад"))

menu_film = ReplyKeyboardMarkup(resize_keyboard=True)
menu_film.add(KeyboardButton("Комедии 🎭"), KeyboardButton("Фантастика 🪄"))
menu_film.add(KeyboardButton("Мультфильмы 🧸"), KeyboardButton("Ужасы🔞"))
menu_film.add(KeyboardButton("Детективы 🔍"), KeyboardButton("Триллеры 🏿"))
menu_film.add(KeyboardButton("назад"))


menu_music = ReplyKeyboardMarkup(resize_keyboard=True)
menu_music.add(KeyboardButton("Электронная музыка 🎇"), KeyboardButton("Джаз 🎺"))
menu_music.add(KeyboardButton("Ритм-н-блюз "), KeyboardButton("Блюз 🔹"))
menu_music.add(KeyboardButton("назад"))

product_button = ReplyKeyboardMarkup(resize_keyboard=True)
product_button.add(KeyboardButton("назад"))

