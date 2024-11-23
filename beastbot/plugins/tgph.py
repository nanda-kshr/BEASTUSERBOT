from telethon import TelegramClient, events
import beastbot.client
import os
from html_telegraph_poster import TelegraphPoster
from html_telegraph_poster.upload_images import upload_image


client = beastbot.client.client








tumsg = "✓ 𝗙𝗶𝗹𝗲 𝗨𝗽𝗹𝗼𝗮𝗱𝗲𝗱 𝗧𝗼 : "
tumsg2 =( "\n✓ 𝗧𝗶𝗺𝗲 𝗧𝗮𝗸𝗲𝗻 :- 𝟭 𝗦𝗲𝗰 "
  "\n✓ 𝗕𝗬 :- [𝗘𝗩𝗜𝗟 𝗕𝗘𝗔𝗦𝗧](http://t.me/elbeastz)") 
 

noob = "𝗔𝗘𝗘𝗘 𝗬𝗔𝗔𝗥!\𝗘𝗘𝗞 𝗜𝗠𝗔𝗚𝗘 𝗞𝗢 𝗥𝗘𝗣𝗟𝗬 𝗞𝗔𝗥𝗡𝗔. \n𝗡𝗢𝗢𝗕𝗗𝗘 𝗢𝗪𝗡𝗘𝗥🤦‍♂️🤦‍♂️"




@events.register(events.NewMessage(outgoing=True, pattern=r'\.upload'))
async def telegraphUploadHandler(event):
  chat = await event.get_chat()
  replied = await event.get_reply_message()
  try:
    image = await replied.download_media()
    x = upload_image(image)
  except:
    return await client.edit_message(event.message,noob ) 
  await client.send_message(chat, tumsg + x + tumsg2)
  os.remove(image)
