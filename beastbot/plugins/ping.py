
from telethon import TelegramClient, events
import beastbot.client
import asyncio
import os


client = beastbot.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.ping'))




async def ping(event):
  
    # Say "!pong" whenever you send "!ping", then delete both messages
  chat = await event.get_chat()
  await client.delete_messages(chat, event.message)   
  m = await event.reply('!𝗣𝗢𝗡𝗚 𝗕𝗛𝗔𝗜')
  await asyncio.sleep(5)
#  await client.delete_messages(event.chat_id, [event.id, m.id])
