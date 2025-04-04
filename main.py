from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

import yaml
from yaml.loader import SafeLoader

from parser import forecast
from wether_cases import *

with open('TOKEN.yaml') as f:
    token = yaml.load(f, Loader=SafeLoader)['token']

bot = Bot(token=token) # initialization bot
dp = Dispatcher(bot) # initialization dispatcher

b1 = KeyboardButton("/Прогноз_погоды")
b2 = KeyboardButton('/Одежда')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2)

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    await message.answer("Я готов отвечать на ваши запросы", reply_markup=kb_client)

@dp.message_handler(commands=['Прогноз_погоды'])
async def weather(message : types.Message):
    ans = ""
    for data in forecast:
        ans += f'{data}: {forecast[data]}\n'
    await message.answer(ans)

@dp.message_handler(commands=['Одежда'])
async def weather(message : types.Message):
    ans = "ppp"
    if int(str(forecast["Температура"])[:-1]) <= -20:
        ans = case1()
    elif -10 <= int(str(forecast["Температура"])[:-1]) and int(str(forecast["Температура"])[:-1]) > -20:
        ans = case2()
    elif 0 <= int(str(forecast["Температура"])[:-1]) and int(str(forecast["Температура"])[:-1]) > -10:
        ans = case3()
    elif 10 >= int(str(forecast["Температура"])[:-1]) and int(str(forecast["Температура"])[:-1]) > 0:
        ans = case3()
    await message.answer(ans)

executor.start_polling(dp, skip_updates=True)
