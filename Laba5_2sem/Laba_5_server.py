from telebot import types
from requests import get
from PIL import Image
from numpy import array
from math import sqrt
from redis import Redis
import redis
import time
import os

handle = open("token.txt", "r")
token = handle.readline()
bot = telebot.TeleBot(token)
r = Redis(host='127.0.0.1', port=6379)
r = Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'])
#os.environ['REDIS_HOST'] = '127.0.0.1'
#os.environ['REDIS_PORT'] = '6379'
redis.REDIS_PORT=6379
figure_chose_markup = telebot.types.ReplyKeyboardMarkup(True, True)
figure_chose_markup.row('Треугольник')
figure_chose_markup.row('Круг')
@@ -91,7 +95,6 @@ def circle_choose_known_param(message):
        bot.send_message(message.chat.id, 'Что-то пошло не так, начни со /start')

def circle_radius_by_smth(message):
    one_time_keyboard = False
    if message.text == 'Длина, неизвестен радиус':
        bot.send_message(message.chat.id, 'Введите длину(см):')
        bot.register_next_step_handler(message, circle_radius_by_length)