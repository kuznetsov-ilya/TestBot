# encoding=utf-8

from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from lists import texts_of_messages
from TOKEN_FILE import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply('''Hi! I'm Bot.!\nTo see my commands text "/help".''')


@dp.message_handler(commands=['help'])
async def send_list_of_commands(message: types.Message):
    message_text = texts_of_messages.get('commands')
    await message.reply(message_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

