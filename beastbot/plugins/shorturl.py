from telethon import TelegramClient, events
import beastbot.client
client = beastbot.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.shorturl'))
async def sl(event):
  chat = await event.get_chat()
  replied_msg = await event.get_reply_message()
  chat_id = chat.id
  results = await client.inline_query('@URLShortenRobot', replied_msg.message ,entity=chat_id)
  message = await results[0].click(0)
 
 
