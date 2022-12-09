# encoding=utf-8

from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from commands_ import commands
from TOKEN_FILE import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=commands)
async def send_welcome(message: types.Message):
    await message.reply('''Hi! I'm Bot.!\nTo see my commands text "/help"''')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
