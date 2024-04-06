from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import logging


load_dotenv()
API_TOKEN = os.getenv("TOKEN")

#print(API_TOKEN)

logging.basicConfig(level=logging.INFO)

#Initialize bot
bot = Bot(token = API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=['start','help'])
async def command_start_handler(message: types.Message):
    
    await message.reply("Hello! I'm a bot that can help you to find the best restaurants")

    
dp.message_handler()
async def echo(message: types.Message):
    """This will return an echo of the message."""
    await message.reply(message.text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)