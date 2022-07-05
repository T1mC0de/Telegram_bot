from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import yaml
from yaml.loader import SafeLoader


with open('TOKEN.yaml') as f:
    token = yaml.load(f, Loader=SafeLoader)['token']

bot = Bot(token=token) # initialization bot
dp = Dispatcher(bot) # initialization dispatcher

@dp.message_handler()
async def echo_send(message: types.Message): #async echo func
    await message.answer(message.text)




executor.start_polling(dp, skip_updates=True) 