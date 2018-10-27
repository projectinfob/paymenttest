# -*- coding: utf-8 -*-
import os
import telebot
import time
import telebot
import random
from telebot import types
from pymongo import MongoClient
import threading

   
bot=telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])   

@bot.message_handler()
def handl(m):
   bot.sendInvoice(m.chat.id, 'Покупай хуету!','Описание к хуете','payload1', '4242 4242 4242 4242',[145])

if True:
   print('bot is working')
   bot.polling(none_stop=True,timeout=600)
