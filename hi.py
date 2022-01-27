
from telethon import TelegramClient, events
import beastbot.client
client = beastbot.client.client

@events.register(events.NewMessage(outgoing=True, pattern='hi$'))
async def _(event):
  chat = await event.get_chat()
  await client.edit_message(event.message, "𝗛𝗲𝗹𝗹𝗼! 𝗛𝗼𝘄 𝗮𝗿𝗲 𝘆𝗼𝘂.")
  
@events.register(events.NewMessage(outgoing=True, pattern='hey$'))
async def _2(event):
  chat = await event.get_chat()
  await client.edit_message(event.message, "𝗛𝗲𝗹𝗹𝗼?\n𝗛𝗘𝗟𝗟𝗢 𝗩𝗥𝗢?\n𝗔𝗥𝗘 𝗬𝗢𝗨 𝗢𝗡𝗟𝗜𝗡𝗘?")
  

