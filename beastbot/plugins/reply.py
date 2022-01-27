from telethon import TelegramClient, events
import beastbot.client
client = beastbot.client.client
import os
import beastbot.plugins.pmpermit
import time

approved = beastbot.plugins.pmpermit.approved

m = ("""

𝗛𝗘𝗟𝗟𝗢 𝗧𝗛𝗘𝗥𝗘

𝗪𝗘𝗟𝗟. 𝗖𝗔𝗡 𝗬𝗢𝗨 𝗧𝗬𝗣𝗘 
𝗪𝗛𝗔𝗧 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧
𝗜𝗡𝗦𝗧𝗘𝗔𝗗 𝗢𝗙 𝗧𝗛𝗜𝗦?

𝗠𝗬 𝗠𝗔𝗦𝗧𝗘𝗥 𝗜𝗦 𝗕𝗨𝗦𝗬.
""")

@events.register(events.NewMessage(outgoing=True, pattern=r'\.id'))
async def hmm(event):
  replied = await event.get_reply_message()
  id_ = str(replied.sender.id)
  replied = replied.sender.username
  await client.edit_message(event.message,"YOUR USER ID IS : " + id_ +"\nAND YOUR USERNAME IS @" + replied)
  

@events.register(events.NewMessage(outgoing=True, pattern=r'\.hack'))
async def hack(event):
  chat = await event.get_chat()
  chat1=str(chat)
  event1 =str(event)
  time.sleep(1)
  await client.edit_message(event.message,"𝙷𝙰𝙲𝙺𝙸𝙽𝙶.")
  time.sleep(1)
  await client.edit_message(event.message,"𝙷𝙰𝙲𝙺𝙸𝙽𝙶..")
  time.sleep(1)
  chat1 = chat1.replace(",", "\n")
  event1 = event1.replace(",", "\n")
  await client.edit_message(event.message,"𝙷𝙰𝙲𝙺𝙸𝙽𝙶...")
  time.sleep(1)
  await client.edit_message(event.message,"""
𝙷𝙰𝙲𝙺𝙸𝙽𝙶 𝙸𝙽 𝙿𝚁𝙾𝙲𝙴𝚂𝚂
[               ] 0% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳

𝙷𝙰𝙲𝙺𝙸𝙽𝙶 𝙸𝙽𝚃𝙾 𝙿𝙷𝙾𝙽𝙴
[░░░░░░        ] 50% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙰𝙿𝙿
[               ] 0% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
?𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
[               ] 0% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙱𝚈𝙿𝙰𝚂𝚂𝙸𝙽𝙶 𝙾𝚃𝙿
[               ] 0% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳


""")
  time.sleep(2)
  await client.edit_message(event.message,"""
𝙷𝙰𝙲𝙺𝙸𝙽𝙶 𝙸𝙽 𝙿𝚁𝙾𝙲𝙴𝚂𝚂
[░░░           ] 25% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳

𝙷𝙰𝙲𝙺𝙸𝙽𝙶 𝙸𝙽𝚃𝙾 𝙿𝙷𝙾𝙽𝙴
[░░░░░░░░░░░░░] 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙰𝙿𝙿
[░░░░░░        ] 50% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
[               ] 0% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙱𝚈𝙿𝙰𝚂𝚂𝙸𝙽𝙶 𝙾𝚃𝙿
[               ] 0% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳


""")
  time.sleep(2)
  await client.edit_message(event.message,"""
𝙷𝙰𝙲𝙺𝙸𝙽𝙶 𝙸𝙽 𝙿𝚁𝙾𝙲𝙴𝚂𝚂
[░░░░░░      ] 50% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳

𝙷𝙰𝙲𝙺𝙸𝙽𝙶 𝙸𝙽𝚃𝙾 𝙿𝙷𝙾𝙽𝙴
[░░░░░░░░░░░░░] 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙰𝙿𝙿
[░░░░░░░░░░░░░] 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
[░░░░░░        ] 50% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙱𝚈𝙿𝙰𝚂𝚂𝙸𝙽𝙶 𝙾𝚃𝙿
[               ] 0% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳


""")
  time.sleep(2)
  await client.edit_message(event.message,"""
𝙷𝙰𝙲𝙺𝙸𝙽𝙶 𝙸𝙽 𝙿𝚁𝙾𝙲𝙴𝚂𝚂
[░░░░░░░░░    ] 75% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳

𝙷𝙰𝙲𝙺𝙸𝙽𝙶 𝙸𝙽𝚃𝙾 𝙿𝙷𝙾𝙽𝙴
[░░░░░░░░░░░░░] 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙰𝙿𝙿
[░░░░░░░░░░░░░] 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
[░░░░░░░░░░░░░] 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙱𝚈𝙿𝙰𝚂𝚂𝙸𝙽𝙶 𝙾𝚃𝙿
[░░░░░░        ] 50% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳


""")
  time.sleep(2)
  await client.edit_message(event.message,"""
𝙷𝙰𝙲𝙺𝙸𝙽𝙶 𝙸𝙽 𝙿𝚁𝙾𝙲𝙴𝚂𝚂
[░░░░░░░░░░░░░] 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳

𝙷𝙰𝙲𝙺𝙸𝙽𝙶 𝙸𝙽𝚃𝙾 𝙿𝙷𝙾𝙽𝙴
[░░░░░░░░░░░░░] 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂 𝙰𝙿𝙿
[░░░░░░░░░░░░░] 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
[░░░░░░░░░░░░░] 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳
𝙱𝚈𝙿𝙰𝚂𝚂𝙸𝙽𝙶 𝙾𝚃𝙿
[░░░░░░░░░░░░░] 100% 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳


""")
  time.sleep(1)
  await client.edit_message(event.message,"𝙶𝙴𝚃𝚃𝙸𝙽𝙶 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 𝙳𝙴𝚃𝙰𝙸𝙻𝚂..")
  time.sleep(2)
  await client.edit_message(event.message,"𝙶𝙴𝚃𝚃𝙸𝙽𝙶 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 𝙳𝙴𝚃𝙰𝙸𝙻𝚂..\n𝚂𝚄𝙲𝙲𝙴𝚂𝚂")
  time.sleep(3)
  await client.edit_message(event.message,f"𝙶𝙴𝚃𝚃𝙸𝙽𝙶 𝙰𝙲𝙲𝙾𝚄𝙽𝚃 𝙳𝙴𝚃𝙰𝙸𝙻𝚂..\n𝚂𝚄𝙲𝙲𝙴𝚂𝚂\n𝙿𝚁𝙸𝙽𝚃𝙸𝙽𝙶 𝙳𝙴𝚃𝙰𝙸𝙻𝚂..\n\n\n{chat1}\n\n 𝙶𝙰𝚃𝙷𝙴𝚁𝙸𝙽𝙶 ?𝙾𝚁𝙴 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽𝚂\n\n\n{event1}\n\n𝙷𝙰𝙲𝙺𝙸𝙽𝙶 𝚂𝚄𝙲𝙲𝙴𝚂𝚂𝙵𝚄𝙻𝙻𝚈 𝙲𝙾𝙼𝙿𝙻𝙴𝚃𝙴𝙳")
  time.sleep(30)
  await client.edit_message(event.message,"𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝚂𝙴𝙻𝙵 𝙳𝙴𝚂𝚃𝚁𝚄𝙲𝙴𝙳")
  
  
@events.register(events.NewMessage(incoming=True, pattern='hi'))
async def _(event):
  chat = await event.get_chat()
  chat_id=chat.id
  if chat_id in approved:
    await client.send_message(chat,m)
  
  
  
@events.register(events.NewMessage(incoming=True, pattern='hello'))
async def _3(event):
  chat = await event.get_chat()
  chat_id=chat.id
  if chat_id in approved:
    
    await client.send_message(chat,m)

@events.register(events.NewMessage(incoming=True, pattern='Hi'))
async def _1(event):
  chat = await event.get_chat()
  chat_id=chat.id
  if chat_id in approved:
    
    await client.send_message(chat,m)

@events.register(events.NewMessage(incoming=True, pattern='Hello'))
async def _2(event):
  chat = await event.get_chat()
  chat_id=chat.id
  if chat_id in approved:
    
    await client.send_message(chat,m)

@events.register(events.NewMessage(outgoing=True, pattern=r'\.save'))
async def _4(event):
  if event.is_reply:
    chat = await event.get_chat()
    replied = await event.get_reply_message()
    sender = replied.sender
    photo = await client.download_profile_photo(sender)
    await client.edit_message(event.message, 'Saved your photo {}'.format(sender.username))
    await client.send_file(chat , file=photo , caption="DP OF POOR VOI")
    os.remove(photo)





