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
   prices1=[LabeledPrice(label='За хуй в рот',amount=100),LabeledPrice(label='За залупу в рот',amount=350)]
   bot.send_invoice(m.chat.id, title='Покупай хуету!',description='Описание к хуете',payload='payload1',\
                    provider_token='4242 4242 4242 4242',start_parametr='startparametr',currency='RUB',prices=prices1)

if True:
   print('bot is working')
   bot.polling(none_stop=True,timeout=600)
