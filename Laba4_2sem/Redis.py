import telebot
import redis

handle = open("token.txt", "r")
token = handle.readline()
r = redis.Redis(host='127.0.0.1', port=6379)
bot = telebot.TeleBot(token)