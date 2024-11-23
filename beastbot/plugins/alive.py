from telethon import events
import beastbot.client
import os


client = beastbot.client.client
alivemsg = "𝗗𝗢𝗡𝗧 𝗪𝗢𝗥𝗥𝗬 𝗠𝗬 𝗗𝗘𝗔𝗥👹\n👹𝗘𝗩𝗜𝗟 𝗕𝗘𝗔𝗦𝗧👹\n👹𝗜 𝗠 𝗔𝗟𝗜𝗩𝗘👹\n"
  
#beastub = beastbot.resources.beastub
r=(
  
  
  f"👹{alivemsg}\n\n"
"**━━━━━━━━━━━━━━━━━━━━**\n\n"
"↼𝗠𝗔𝗦𝗧𝗘𝗥⇀𝗘𝗩𝗜𝗟 𝗕𝗘𝗔𝗦𝗧\n"
"╔══════════════════╗\n"
"╠•➳➠ 𝗧𝗲𝗹𝗲𝘁𝗵𝗼𝗻 𝗕𝗼𝘁 \n"
"╠•➳➠ 𝗩𝗲𝗿𝘀𝗶𝗼𝗻 - 𝟭.𝟬\n"
"╠•➳➠ `𝗖𝗵𝗮𝗻𝗻𝗲𝗹:` [𝗝𝗢𝗜𝗡](http://t.me/elbeastz_arts)\n"
"╠•➳➠ `𝗖𝗿𝗲𝗮𝘁𝗼𝗿:` [𝗘𝗩𝗜𝗟 𝗕𝗘𝗔𝗦𝗧](http://t.me/elbeastz)\n"
"╚══════════════════╝\n"
" [⚡Show Power Here⚡](http://t.me/elbeastz)"
  
)

@events.register(events.NewMessage(outgoing=True, pattern=r'\.alive'))

async def alivee(event):
  chat = await event.get_chat()
  await client.delete_messages(chat, event.message)
  photo = 'http://telegra.ph/file/f4c165c958ff3fbbab31b.jpg'
  #photo = await client.download_profile_photo('me')
  #await client.send_file(chat , file=photo , pmcaption=r)   
  await client.send_file(chat , file=photo , caption=r) 
  #os.remove(photo)
