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
   prices1=[LabeledPrice(label='За хуй в рот',amount=100),LabeledPrice(label='За доставку на дом',amount=350)]
   bot.send_invoice(chat_id=m.chat.id, title='Покупай хуй в рот!',description='Описание к хую',\
                    provider_token='381764678:TEST:7232',currency='RUB',prices=prices1,invoice_payload='payload',start_parameter='startp')

if True:
   print('bot is working')
   bot.polling(none_stop=True,timeout=600)
