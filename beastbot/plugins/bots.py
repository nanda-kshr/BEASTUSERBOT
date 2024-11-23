from telethon import TelegramClient, events
import beastbot.client
client = beastbot.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.q'))
async def q(event):
  chat = await event.get_chat()
  replied_msg = await event.get_reply_message()
  await client.edit_message(event.message, "SH*T IN PROCESS")
  x = await replied_msg.forward_to("@QuotLyBot")
  async with client.conversation('@QuotLyBot') as quotoo:
    reply = await quotoo.get_response(x.id)
    await client.send_message(chat, reply)


