from telethon import TelegramClient, types, functions, events, Button
import beastbot.client
import beastbot.res
import time

client = beastbot.client.client
bot = beastbot.client.bot
flood = 1
approved = ["945846353"]

photo = './beastbot/res/photo.jpg'

r = f"""
   **━━━━━━━━━━━━━━━━━━━━━━**
   𝗛𝗘𝗟𝗟𝗢 𝗧𝗛𝗘𝗥𝗘,
        𝗜 𝗔𝗠 👹𝗕𝗘𝗔𝗦𝗧 𝗨𝗦𝗘𝗥𝗕𝗢𝗧👹
    𝗠𝗬 𝗢𝗪𝗡𝗘𝗥 𝗔𝗡𝗗 𝗖𝗥𝗘𝗔𝗧𝗘𝗥 𝗜𝗦
       ════ 𝗘𝗩𝗜𝗟 𝗕𝗘𝗔𝗦𝗧 ════
  ╔═══════════════════╗
  ╠ 𝙼𝙰𝚂𝚃𝙴𝚁 𝙸𝚂 𝙱𝚄𝚂𝚈 𝙽𝙾𝚆..
  ╠ 𝙲𝙷𝙾𝙾𝚂𝙴 𝙾𝙿𝚃𝙸𝙾𝙽𝚂 𝙱𝙴𝙻𝙾𝚆 𝙰𝙽𝙳
  ╠ 𝙻𝙴𝙰𝚅𝙴 𝚈𝙾𝚄𝚁 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝙷𝙴𝚁𝙴.
  ╚═══════════════════╝
  
  ⚠️Warning! 
  𝚈𝙾𝚄 𝚆𝙸𝙻𝙻 𝙱𝙴 𝙱𝙻𝙾𝙲𝙺𝙴𝙳 𝙰𝙵𝚃𝙴𝚁
  𝚂𝙴𝙽𝙳𝙸𝙽𝙶 5 𝙼𝙴𝚂𝚂𝙰𝙶𝙴𝚂
 """

 
@bot.on(events.InlineQuery)
async def iquery(query):
  global y
  chat = await query.get_chat()
  if query.text=='pm':
    result1 = await query.builder.photo('./beastbot/res/photo.jpg',
     text =r,buttons=[
       [Button.inline("👺SPAM👺",data=b'spm'), Button.inline("💕CHAT💕",data=b'chat')],
       [Button.inline("👹REQUEST👹",data=b'rqt'), Button.inline("❤WISH❤", data=b'wish')]])
    await query.answer([result1])
   
@bot.on(events.CallbackQuery)
async def call(event):
  chat= await event.get_chat()
  chat_id = await event.get_sender()
  
  if event.data == b'spm':
      await event.edit("𝗚𝗘𝗧 𝗢𝗨𝗧 𝗦𝗛*𝗜!!! \n🤬🤬🤬🤬")      
      await client(functions.contacts.BlockRequest(
        id=chat_id.username
    ))
  if event.data==b'chat':
      await event.edit("""
𝗜𝗙 𝗜𝗧𝗦 𝗔𝗡 𝗨𝗥𝗚𝗘𝗡𝗧 
𝗣𝗟𝗘𝗔𝗦𝗘 𝗟𝗘𝗔𝗩𝗘 𝗬𝗢𝗨𝗥 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗛𝗘𝗥𝗘

𝗪𝗛𝗘𝗡 𝗠𝗬 𝗠𝗔𝗦𝗧𝗘𝗥 𝗕𝗘𝗖𝗢𝗠𝗘𝗦 𝗙𝗥𝗘𝗘
𝗛𝗘 𝗪𝗜𝗟𝗟 𝗥𝗘𝗣𝗟𝗬""")
  if event.data==b'wish':
    await event.edit("Hmm......")
    time.sleep(1)
    await event.edit("Hmmm....")
    time.sleep(1)
    await event.edit("Hmmmm.. 𝗡𝗢")
    time.sleep(1)
    await event.edit("""
𝗜 𝗠 𝗡𝗢𝗧 𝗔 𝗚𝗘𝗡𝗜𝗘!
𝗜 𝗠 𝗝𝗨𝗦𝗧 𝗔 𝗨𝗦𝗘𝗥𝗕𝗢𝗧 
𝗠𝗔𝗗𝗘 𝗕𝗬 𝗘𝗩𝗜𝗟 𝗕𝗘𝗔𝗦𝗧..

𝗚𝗢 𝗧𝗔𝗟𝗞 𝗦𝗢𝗠𝗘𝗪𝗛𝗘𝗥𝗘 𝗘𝗟𝗦𝗘

    """)
  if event.data==b'rqt':
      await event.edit("""
      𝙺𝙸𝙽𝙳𝙻𝚈 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝚃𝙷𝙰𝚃 𝚄 𝙽𝙴𝙴𝙳.
𝙸𝙵 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝙷𝙰𝚅𝙴 𝚃𝙷𝙰𝚃 𝚄 𝙽𝙴𝙴𝙳
𝙰𝙽𝙳 𝙼𝚈 𝙼𝙰𝚂𝚃𝙴𝚁 𝙸𝚂 𝙾𝙺𝙰𝚈 𝚃𝙾 𝙶𝙸𝚅𝙴 𝚈𝙾𝚄

𝙷𝙴 𝚆𝙸𝙻𝙻 𝚁𝙴𝙿𝙻𝚈 𝙿𝙾𝚂𝙸𝚃𝙸𝚅𝙻𝚈

𝙺𝙸𝙽𝙳𝙻𝚈 𝙻𝙴𝙰𝚅𝙴 𝚈𝙾𝚄𝚁 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙷𝙴𝚁𝙴""")
        
        
        
        
@events.register(events.NewMessage(outgoing=True, pattern=r'\.a$'))
async def _(event):
  global approved
  chat = await event.get_chat()
  chat_id = chat.id
  x = False
  if not approved:
    await client.edit_message(event.message, "YOU ARE NOW APPROVED")
    approved.append(chat_id.username)
    
    
  else:
    for i in approved:
      
      if chat_id == i:
       await client.edit_message(event.message,"You are already approved")
       x = True
       
    if x is not True:
      await client.edit_message(event.message,"YOU ARE NOW APPROVED")
      approved.append(chat_id)
      
      x = False
  
@events.register(events.NewMessage(outgoing=True, pattern=r'\.d$'))
async def _1(event):
  global approved
  chat = await event.get_chat()
  chat_id = chat.id
  x = False
  if not approved:
    await client.edit_message(event.message, "YOU ARE NOT APPROVED TO CHAT WITH MY MASTER")
    
    
  else:
    
    if chat_id in approved:
        approved.remove(chat_id)
        await client.edit_message(event.message,"You are Disapproved to chat with my MASTER")
        x = True
    for i in approved:
      if x is not True:
        await client.edit_message(event.message,"You are already Disapproved to chat with my MASTER")
        x = False



@events.register(events.NewMessage(incoming=True))
async def _2(event):
  
  global approved
  global flood
  chat = await event.get_chat()
  chat_id = await event.get_sender()
  if event.is_private:
    if not chat.bot:
      
      if chat_id.id not in approved:
        global flood
        flood = flood + 1
        if flood <= 5:
          results = await client.inline_query('@beast_ubot', 'pm')
          await results[0].click(entity=chat_id)
        else:
          await client(functions.contacts.BlockRequest(
        id=chat_id.username))



