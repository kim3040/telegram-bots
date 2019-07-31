# -*- coding: utf-8 -*-
import amanobot
from amanobot.loop import MessageLoop
import time
from amanobot.exception import TelegramError, TooManyRequestsError, NotEnoughRightsError

bot = amanobot.Bot('SEUTOKEN')

def handle(msg):
#Definimos o comando /link 
 if msg['text'].lower() == '/link':
#Verificamos se o id do grupo ou canal possui Mais De 9 Digitos Normalmente grupos e canais possuem 10 ou mais Dígitos Ja o id de um usuario chega a ter somente 9 dígitos
  if len(str(msg['chat']['id'])) > 9:
   try:
#o bot tentará pegar o link do grupo
    exportar = bot.exportChatInviteLink(msg['chat']['id'])
    bot.sendMessage(msg['chat']['id'], exportar) 
   except NotEnoughRightsError:
#se der um erro o bot enviará uma mensagem dizendo que não possui adm
    bot.sendMessage(msg['chat']['id'], "não tenho adm para pegar o link do grupo") 
    
MessageLoop(bot, handle).run_as_thread()
while 1:
  time.sleep(10)
