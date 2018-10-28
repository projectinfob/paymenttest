# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
from telebot import types
from telebot.types import LabeledPrice
from telebot.types import ShippingOption
from pymongo import MongoClient
import threading

   
bot=telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])   

@bot.message_handler()
def handl(m):
   prices=[LabeledPrice(label='За хуй в рот',amount=100),LabeledPrice(label='За залупу в рот',amount=350)]
   bot.send_invoice(m.chat.id, 'Покупай хуету!','Описание к хуете','payload1', '4242 4242 4242 4242','startparametr','RUB',prices)

if True:
   print('bot is working')
   bot.polling(none_stop=True,timeout=600)
