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
   prices1=[LabeledPrice(label='Тест',amount=10000),LabeledPrice(label='За доставку на дом',amount=35000)]
   bot.send_invoice(chat_id=m.chat.id, title='Покупай!',description='Покупка тест',is_flexible=False,\
                    invoice_payload='payload',provider_token='381764678:TEST:7232',start_parameter='startp',\
                    currency="RUB",prices=prices1)
   

@bot.pre_checkout_query_handler(func=lambda call: True)
def handlcheckout(c):
   if random.randint(0,1)==1:
      x=bot.answer_pre_checkout_query(c.id,True)
   else:
      x=bot.answer_pre_checkout_query(c.id,False, 'Неудача. Не знаю, почему.')
   

if True:
   print('bot is working')
   bot.polling(none_stop=True,timeout=600)
