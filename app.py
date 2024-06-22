import logging
from db import Database
from aiogram import Bot, Dispatcher, executor, types
from default_button import menu_keyboard, menu_film, menu_photo, menu_music
from inline_button import InlineKeyboardButton, InlineKeyboardMarkup
import asyncio

API_TOKEN = "7354269085:AAFNP-08_3W6em_VAVgqPIy42gq487RgUBM"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    ful_name = message.from_user.full_name
    user_id = message.from_user.id
    username = message.from_user.username
    query = f"INSERT INTO users_2 (username, full_name, user_id) VALUES ('{username}', '{ful_name}', {user_id})"
    if await Database.check_user_id(user_id):
        await message.reply(f"Я рад вас видеть  |😈😈 @{username}😈😈", reply_markup=menu_keyboard)

    else:
        await Database.connect(query, "insert")
        await message.reply(f"Добро пожаловать в бот mans 🤖 |😈😈 @{username}😈😈", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "меню изображений 📸")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("1- отделение. Выберите одну из категорий:", reply_markup=menu_photo)


@dp.message_handler(lambda message: message.text == "фильм 🎞")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("2- отделение. Выберите одну из категорий:", reply_markup=menu_film)


@dp.message_handler(lambda message: message.text == "Mansur's | blog💻")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("3- отделение. https://t.me/mansur_blog_uz", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "музыкальное меню 🎵")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("4- отделение. Выберите одну из категорий:", reply_markup=menu_music)


@dp.message_handler(lambda message: message.text == "меню истории 🔍")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("5- отделение. https://t.me/Tarix", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "меню новостей 📰🗞")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("6- отделение. https://t.me/daryouz_dunyo_yangilillar_uzbek", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Instagram")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("7- отделение.  https://www.instagram.com/", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Tik tok")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("8- отделение.  https://www.tiktok.com/", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "назад")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("🤬Выберите одну из категорий 🤬", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "изображений 📸")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фотография", reply_markup=menu_photo)


@dp.message_handler(lambda message: message.text == "Природа 🏕")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фотография", reply_markup=menu_photo)


@dp.message_handler(lambda message: message.text == "Рабочий стол 💻")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фотография", reply_markup=menu_photo)


@dp.message_handler(lambda message: message.text == "Город 🏙")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фотография", reply_markup=menu_photo)


@dp.message_handler(lambda message: message.text == "Море 🌊")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фотография", reply_markup=menu_photo)


@dp.message_handler(lambda message: message.text == "Космос 🪐")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фотография", reply_markup=menu_photo)


@dp.message_handler(lambda message: message.text == "Луна 🌙")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фотография", reply_markup=menu_photo)


@dp.message_handler(lambda message: message.text == "назад")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("🤬Выберите одну из категорий 🤬", reply_markup=menu_photo)


@dp.message_handler(lambda message: message.text == "Комедии 🎭")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фильм", reply_markup=menu_film)


@dp.message_handler(lambda message: message.text == "Фантастика 🪄")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фильм", reply_markup=menu_film)


@dp.message_handler(lambda message: message.text == "Мультфильмы 🧸")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фильм", reply_markup=menu_film)


@dp.message_handler(lambda message: message.text == "Ужасы🔞")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фильм", reply_markup=menu_film)


@dp.message_handler(lambda message: message.text == "Детективы 🔍")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фильм", reply_markup=menu_film)


@dp.message_handler(lambda message: message.text == "Триллеры 🏿")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша фильм", reply_markup=menu_film)


@dp.message_handler(lambda message: message.text == "назад")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("🤬Выберите одну из категорий 🤬", reply_markup=menu_keyboard)


@dp.message_handler(lambda message: message.text == "Электронная музыка 🎇")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша музыка", reply_markup=menu_music)


@dp.message_handler(lambda message: message.text == "Джаз 🎺")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша музыка", reply_markup=menu_music)


@dp.message_handler(lambda message: message.text == "Ритм-н-блюз ")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша музыка", reply_markup=menu_music)


@dp.message_handler(lambda message: message.text == "Блюз 🔹")
async def show_menu(message: types.Message):
    # action = button_callback_menu.new(action=message.text)
    await message.answer("Ваша музыка", reply_markup=menu_music)

# @dp.message_handler(lambda message: message.text == "изображений 📸")
# async def show_menu(message: types.Message):
#     keyboard = types.InlineKeyboardMarkup()
#     keyboard = InlineKeyboardMarkup()
#     button1 = InlineKeyboardButton(text="➖", callback_data="option1")
#     button2 = InlineKeyboardButton(text="1", callback_data="option2")
#     button3 = InlineKeyboardButton(text="➕", callback_data="option3")
#     # button4 = InlineKeyboardButton(text="Back", callback_data="option3")
#     keyboard.add(button1, button2, button3)
#     await bot.send_message(message.chat.id, "select", reply_markup=keyboard)


@dp.message_handler(commands=['image'])
async def send_image(message: types.Message):
    photo_url = 'https://images.pexels.com/photos/3680219/pexels-photo-3680219.jpeg?cs=srgb&dl=pexels-lukas-rodriguez-1845331-3680219.jpg&fm=jpg'
    caption = 'Ваша фотография'
    await bot.send_photo(message.chat.id, photo=photo_url, caption=caption)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
