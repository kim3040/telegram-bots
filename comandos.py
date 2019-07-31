# -*- coding: utf-8 -*-
import amanobot
from amanobot.loop import MessageLoop
import time

bot = amanobot.Bot('826276252:AAHVOOOLswpggSeAOPet9fIl1VQvRBQRXAI')

def handle(msg):
 if msg['text'] == '/start':
  bot.sendMessage(msg['chat']['id'], 'Olá')
# toda vez que um usuário digitar /start uma mensagem sera enviada para o mesmo no caso a mensagem enviada sera Olá
 elif msg['text'] == '/help':
  bot.sendMessage(msg['chat']['id'], 'em que posso ajudar')

MessageLoop(bot, handle).run_as_thread()
while 1:
  time.sleep(10)
