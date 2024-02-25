import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
STRMSG = '''
Hello, I am a bot!

Я был создан Анатолием White. 
Для того создан что бы передавать ваше эхо.
Напиши мне что нибудь.

I was created by Anatoly White. 
I was created to transmit your echo.
*Write me something.*
'''

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(STRMSG)

@dp.message()
async def file_handler(message: types.Message):
    await message.answer_photo(message.photo[0].file_id)
@dp.message()
async def stik_handler(message: types.Message):
    await message.answer_sticker(message.sticker.file_id)
@dp.message()
async def echo_handler(message: types.Message):
    await message.answer(message.text)


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())