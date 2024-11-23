from telethon import TelegramClient, events, Button
import beastbot.client


client = beastbot.client.client
bot = beastbot.client.bot

@bot.on(events.InlineQuery)
async def iquery(query):
  if query.text == 'help':
    result = query.builder.article('Help', text="𝗛𝗘𝗟𝗣 𝗠𝗘𝗡𝗨 𝗢𝗙 👹👹𝗕𝗘𝗔𝗦𝗧𝗕𝗢𝗧👹👹", buttons=[
      [Button.inline("Alive",data=b'alv'), Button.inline("Hi",data=b'hi')],
      [Button.inline("Reply",data=b'reply'), Button.inline("animation",data=b'anim')],      [Button.inline("arts"), Button.inline("ascii")],      
      [Button.inline("Spam",data=b'spmm'), Button.inline("Upload to tgraph",data=b'uptg')],
      [Button.url("ABOUT DEVELOPER",url = "http://t.me/beastuserbot_dev")]
      
      
      
      
      
          ])
    await query.answer([result])

@bot.on(events.CallbackQuery)
async def call(event):
  
  if event.original_update.user_id == 945846353:
    if event.data == b'alv':
      await event.edit("𝗗𝗢 .alive 𝗧𝗢 𝗦𝗘𝗘 𝗔𝗟𝗜𝗩𝗘 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗢𝗙 𝗕𝗘𝗔𝗦𝗧 𝗨𝗦𝗘𝗥𝗕𝗢𝗧")
    if event.data == b'spmm':
      await event.edit("𝗗𝗢 .spam [count] [message] 𝗧𝗢 𝗦𝗣𝗔𝗠 𝗜𝗡 𝗔 𝗖𝗛𝗔𝗧. \n\n𝗘𝗫𝗔𝗠𝗣𝗟𝗘 : .spam 10 this is beast userbot\n\n𝗪𝗔𝗥𝗡𝗜𝗡𝗚! 𝗗𝗢𝗡𝗧 𝗗𝗜𝗦𝗧𝗨𝗥𝗕 𝗢𝗧𝗛𝗘𝗥𝗦.\n𝗬𝗢𝗨𝗥 𝗔𝗖𝗖𝗢𝗨𝗡𝗧 𝗖𝗔𝗡 𝗚𝗘𝗧 𝗟𝗜𝗠𝗜𝗧𝗘𝗗")
    if event.data == b'uptg':
      await event.edit("𝗗𝗢 .upload 𝗕𝗬 𝗥𝗘𝗣𝗟𝗬𝗜𝗡𝗚 𝗔 𝗙𝗜𝗟𝗘 \n𝗧𝗢 𝗨𝗣𝗟𝗢𝗔𝗗 𝗜𝗧 𝗜𝗡 𝗧𝗘𝗟𝗘𝗚𝗥𝗔𝗣𝗛")
    if event.data == b'hi':
      await event.edit("𝗗𝗢 .hi 𝗧𝗢 𝗦𝗘𝗘 𝗔𝗟𝗜𝗩𝗘 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗢𝗙 𝗕𝗘𝗔𝗦𝗧 𝗨𝗦𝗘𝗥𝗕𝗢𝗧")
    if event.data == b'reply':
      await event.edit("""
      
      𝗧𝗛𝗜𝗦 𝗛𝗔𝗦 𝗔 𝗟𝗜𝗦𝗧!
      
𝗗𝗼 .id  𝗯𝘆 𝗿𝗲𝗽𝗹𝘆𝗶𝗻𝗴 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲 
              𝘁𝗼 𝗴𝗲𝘁 𝗵𝗶𝘀 𝘂𝘀𝗲𝗿𝗶𝗱
              
𝗗𝗼 .save  𝗯𝘆 𝗿𝗲𝗽𝗹𝘆𝗶𝗻𝗴 𝗮 𝗺𝗲𝘀𝘀𝗮𝗴𝗲
         𝘁𝗼 𝗴𝗲𝘁 𝗵𝗶𝘀 𝗽𝗿𝗼𝗳𝗶𝗹𝗲 𝗽𝗶𝗰𝘁𝘂𝗿𝗲
      """)
    
      
      



  else:
    await event.edit("𝗪𝗔𝗜𝗧 𝗔 𝗠𝗜𝗡𝗨𝗧𝗘\n𝗪𝗛𝗢 𝗔𝗥𝗘 𝗬𝗢𝗨 ???\n\n𝗚𝗢 𝗔𝗪𝗔𝗬 𝗡𝗢𝗢𝗕")
  



@events.register(events.NewMessage(outgoing=True, pattern=r'\.help'))
async def _(event):
  chat = await event.get_chat()
  results = await client.inline_query('@beast_ubot', 'help')
  await results[0].click(entity=chat.id)



