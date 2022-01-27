from telethon import TelegramClient, events 
import os
import beastbot.client
import asyncio
from beastbot.plugins import alive,ping,hi,hhelp,bff,arts,tgph,pmpermit,animation,gban,bots,spam,shorturl,reply,replyraid



client = beastbot.client.client
bot = beastbot.client.bot

with client as client:
  client.add_event_handler(beastbot.plugins.hi._)
with client as client:
  client.add_event_handler(beastbot.plugins.hi._2)

with client as client:
  client.add_event_handler(beastbot.plugins.tgph.telegraphUploadHandler)

with client as client:
  client.add_event_handler(beastbot.plugins.alive.alivee)

with client as client:
  client.add_event_handler(beastbot.plugins.arts.byee)
  
with client as client:
  client.add_event_handler(beastbot.plugins.bff.bffs)

with client as client:
  client.add_event_handler(beastbot.plugins.bots.q)

with client as client:
  client.add_event_handler(beastbot.plugins.arts.family)

with client as client:
  client.add_event_handler(beastbot.plugins.animation.emoji)

with client as client:
  client.add_event_handler(beastbot.plugins.animation.evil)

with client as client:
  client.add_event_handler(beastbot.plugins.animation.brain)

with client as client:
  client.add_event_handler(beastbot.plugins.animation.bombs)

with client as client:
  client.add_event_handler(beastbot.plugins.animation.gm)

with client as client:
  client.add_event_handler(beastbot.plugins.animation.gn)

with client as client:
  client.add_event_handler(beastbot.plugins.animation.call)

with client as client:
  client.add_event_handler(beastbot.plugins.animation.kill)

with client as client:
  client.add_event_handler(beastbot.plugins.replyraid._)

with client as client:
  client.add_event_handler(beastbot.plugins.reply.hack)

with client as client:
  client.add_event_handler(beastbot.plugins.ping.ping)

with client as client:
  client.add_event_handler(beastbot.plugins.reply.hmm)

with client as client:
  client.add_event_handler(beastbot.plugins.reply._)

with client as client:
  client.add_event_handler(beastbot.plugins.reply._1)

with client as client:
  client.add_event_handler(beastbot.plugins.reply._2)

with client as client:
  client.add_event_handler(beastbot.plugins.reply._3)

with client as client:
  client.add_event_handler(beastbot.plugins.reply._4)

with client as client:
  client.add_event_handler(beastbot.plugins.spam.spam)

with client as client:
  client.add_event_handler(beastbot.plugins.shorturl.sl)

with client as client:
  client.add_event_handler(beastbot.plugins.pmpermit._)

with client as client:
  client.add_event_handler(beastbot.plugins.pmpermit._1)

with client as client:
  client.add_event_handler(beastbot.plugins.pmpermit._2)

with client as client:
  client.add_event_handler(beastbot.plugins.hhelp._)

with client as client:
  client.add_event_handler(beastbot.plugins.gban.gban)

with client as client:
  client.add_event_handler(beastbot.plugins.gban.ungban)

with client as client:
  client.add_event_handler(beastbot.plugins.gban.all_gban)

with client as client:
  client.add_event_handler(beastbot.plugins.gban.gmute)

with client as client:
  client.add_event_handler(beastbot.plugins.gban.ungmute)




loop = asyncio.get_event_loop()
client.start()
bot.start()
loop.run_forever()
