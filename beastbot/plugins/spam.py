from telethon import TelegramClient, events
import beastbot.client
import asyncio
client = beastbot.client.client



@events.register(events.NewMessage(outgoing=True, pattern=r'\.spam'))
async def spam(e):
  if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
    message = e.text
    counter = int(message[6:9])
    spam_message = str(e.text[8:])
    await asyncio.wait([e.respond(spam_message) for i in range(counter)])
    await e.delete()
    await client.send_message(f"#SPAM \n\nSpammed  `{counter}`  messages!!")


