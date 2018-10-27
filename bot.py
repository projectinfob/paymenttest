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
   labeledprice1=['За хуй в рот','За залупу в рот']
   bot.send_invoice(m.chat.id, 'Покупай хуету!','Описание к хуете','payload1', '4242 4242 4242 4242','startparametr','RUB',labeledprice1)

if True:
   print('bot is working')
   bot.polling(none_stop=True,timeout=600)
