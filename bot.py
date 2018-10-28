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
   bot.send_invoice(m.chat.id, title='Покупай хуету!',description='Описание к хуете',\
                    provider_token='381764678:TEST:4376',currency='RUB',prices=prices1,invoice_payload='payload',start_parameter='startp')

if True:
   print('bot is working')
   bot.polling(none_stop=True,timeout=600)
