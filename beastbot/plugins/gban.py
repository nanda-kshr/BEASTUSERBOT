from telethon import events
import beastbot.client
import os
import beastbot.resources
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
import asyncio
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantAdmin
from telethon.tl.functions.channels import GetParticipantRequest
import random


gbanned = []
client = beastbot.client.client
DEVLIST = [5009604489,5004021105,945846353]
FRNDLIST = [2077699752,5029218505,5032100535]
import time

chats = 94
r = {}

@events.register(events.NewMessage(outgoing=True, pattern=r'\.gban'))
async def gban(event):
  global r
  chat = await event.get_chat()
  chats = 94
  userid=chat.id
  m = True
  c = True
  strg = ""
  split = event.text.split(" ")
  try:
    tezt = event.text[6]
    c = False
  except:
    pass
  if userid in r:
    await client.edit_message(event.message,"𝚅𝚁𝙾 𝙷𝙴 𝙰𝙻𝚁𝙴𝙰𝙳𝚈 𝙶 𝙱𝙰𝙽𝙽𝙴𝙳")
    m = False
  if not event.text[0].isalpha() and c and m:
    reason = event.text[6:1000]
    f = r[userid] = reason
    
  else:
    m = split[3]
    x = True
    if x:
      e=split[2:100]
      for i in e:
        strg+=i
      
      reason = strg
      
      e = split[1]
      f = r[e] = reason
      
    
  if event.text[6] == '@':
    e = split
    x = False
    
    chats = random.randint(130,150)
    e = e[1]
    
    await client.edit_message(event.message, f"𝙶𝙱𝙰𝙽𝙽𝙸𝙽𝙶..  {e}") 
    async for gfuck in event.client.iter_dialogs():
      if gfuck.is_group or gfuck.is_channel:
        try:
          await event.client.edit_permissions(gfuck.id, e, view_messages=False)
          chats += 1
          
        except:
          pass
    await client.edit_message(event.message,f"""
          
           
  𝙲𝙾𝙽𝙶𝚁𝙰𝚃𝚄𝙻𝙰𝚃𝙸𝙾𝙽𝚂 🥳 {e} 🥳
  
  𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙱𝙴𝙴𝙽 𝙱𝙰𝙽𝙽𝙴𝙳 𝙸𝙽
  {𝚌𝚑𝚊𝚝𝚜} 𝙲𝙷𝙰𝚃𝚂 𝙰𝙽𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂
   𝙱𝚈 👹𝙱𝙴𝙰𝚂𝚃 𝙱𝙾𝚃👹..
  
  𝙸𝙵 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙰𝙽𝚈 𝙲𝙾𝙼𝙿𝙻𝙰𝙸𝙽𝚃𝚂 
  𝚂𝙿𝙴𝙰𝙺 𝚆𝙸𝚃𝙷 𝙼𝚈 𝙲𝚁𝙴𝙰𝚃𝙾𝚁
  𝙷𝙰𝙿𝙿𝚈 𝙶𝙾𝚃 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝙳𝙰𝚈
  
  """)
  
    
  elif event.is_reply and m:
    chats = 94
    chat = await event.get_reply_message()
    chat_id = chat.sender.username
    userid = "@" + chat_id
    await client.edit_message(event.message, f"𝙶𝙱𝙰𝙽𝙽𝙸𝙽𝙶..  {userid}") 
    time.sleep(2)
    async for gfuck in event.client.iter_dialogs():
      if gfuck.is_group or gfuck.is_channel:
        try:
          await event.client.edit_permissions(gfuck.id, userid, view_messages=False)
          chats += 1
          
        except:
          pass
    await client.edit_message(event.message,f"""
          
           
  𝙲𝙾𝙽𝙶𝚁𝙰𝚃𝚄𝙻𝙰𝚃𝙸𝙾𝙽𝚂 🥳 {userid} 🥳
  
  𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙱𝙴𝙴𝙽 𝙱𝙰𝙽𝙽𝙴𝙳 𝙸𝙽
  {𝚌𝚑𝚊𝚝𝚜} 𝙲𝙷𝙰𝚃𝚂 𝙰𝙽𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂
   𝙱𝚈 👹𝙱𝙴𝙰𝚂𝚃 𝙱𝙾𝚃👹..
  
  𝙸𝙵 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙰𝙽𝚈 𝙲𝙾𝙼𝙿𝙻𝙰𝙸𝙽𝚃𝚂 
  𝚂𝙿𝙴𝙰𝙺 𝚆𝙸𝚃𝙷 𝙼𝚈 𝙲𝚁𝙴𝙰𝚃𝙾𝚁
  𝙷𝙰𝙿𝙿𝚈 𝙶𝙾𝚃 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝙳𝙰𝚈
  
  """)
  elif event.is_private and m:
    if not chat.bot:
      chats = 94
      chat = await event.get_chat()
      chat_id = chat.username
      userid = "@" + chat_id
      await client.edit_message(event.message, f"𝙶𝙱𝙰𝙽𝙽𝙸𝙽𝙶..  {userid}") 
      time.sleep(2)
      async for gfuck in event.client.iter_dialogs():
        if gfuck.is_group or gfuck.is_channel:
          try:
            await event.client.edit_permissions(gfuck.id, userid, view_messages=False)
            chats += 1
            
          except:
            pass
            
            
      
      await client.edit_message(event.message,f"""
          
           
  𝙲𝙾𝙽𝙶𝚁𝙰𝚃𝚄𝙻𝙰𝚃𝙸𝙾𝙽𝚂 🥳 {userid} 🥳
  
  𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙱𝙴𝙴𝙽 𝙱𝙰𝙽𝙽𝙴𝙳 𝙸𝙽
  {𝚌𝚑𝚊𝚝𝚜} 𝙲𝙷𝙰𝚃𝚂 𝙰𝙽𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂
   𝙱𝚈 👹𝙱𝙴𝙰𝚂𝚃 𝙱𝙾𝚃👹..
  
  𝙸𝙵 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙰𝙽𝚈 𝙲𝙾𝙼𝙿𝙻𝙰𝙸𝙽𝚃𝚂 
  𝚂𝙿𝙴𝙰𝙺 𝚆𝙸𝚃𝙷 𝙼𝚈 𝙲𝚁𝙴𝙰𝚃𝙾𝚁
  𝙷𝙰𝙿𝙿𝚈 𝙶𝙾𝚃 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝙳𝙰𝚈
  
  """)
        
         
          
            
  elif not event.is_reply and m:
    await event.reply("𝙶𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁 𝙱𝚈 𝚁𝙴𝙿𝙻𝚈𝙸𝙽𝙶 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴")
    
  
  
  
  
  
  
@events.register(events.NewMessage(outgoing=True, pattern=r'\.ungban'))
async def ungban(event):
  chat = await event.get_chat()
  userid=chat.id
  
  global r
  print(r)
  m = False
  if not userid in r:
        m = True
       
  if not userid in r :
    await client.edit_message(event.message, "𝚈𝙾𝚄 𝙰𝚁𝙴 𝙽𝙾𝚃 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝚃𝙾 𝚄𝙽𝙶𝙱𝙰𝙽")
  
  if m ==False and userid in r:
    del r[userid]
    
  if event.is_reply and m == False:
    chats = 94
    chat = await event.get_reply_message()
    userid = "@" + chat.sender.username
    await client.edit_message(event.message, f"𝚄𝙽𝙶𝙱𝙰𝙽𝙽𝙸𝙽𝙶..  {userid}") 
    time.sleep(2)
    async for gfuck in event.client.iter_dialogs():
      if gfuck.is_group or gfuck.is_channel:
        try:
          await event.client.edit_permissions(gfuck.id, userid, view_messages=True)
          chats += 1
          
        except:
          pass
    await client.edit_message(event.message, f"""
          
  𝙲𝙾𝙽𝙶𝚁𝙰𝚃𝚄𝙻𝙰𝚃𝙸𝙾𝙽𝚂 🥳 {userid} 🥳
  
  𝚈𝙾𝚄 𝙰𝚁𝙴 𝚄𝙽𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝙸𝙽
  {𝚌𝚑𝚊𝚝𝚜} 𝙲𝙷𝙰𝚃𝚂 𝙰𝙽𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂
   𝙱𝚈 👹𝙱𝙴𝙰𝚂𝚃 𝙱𝙾𝚃👹..
  
  𝙸𝙵 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙰𝙽𝚈 𝙲𝙾𝙼𝙿𝙻𝙰𝙸𝙽𝚃𝚂 
  𝚂𝙿𝙴𝙰𝙺 𝚆𝙸𝚃𝙷 𝙼𝚈 𝙲𝚁𝙴𝙰𝚃𝙾𝚁
  𝙷𝙰𝙿𝙿𝚈 𝙶𝙾𝚃 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝙳𝙰𝚈
  
  """)
          
  elif event.is_private and m == False:
    
    if not chat.bot:
      
      chats = 94
      chat = await event.get_chat()
      chat_id = chat.username
      userid = "@" + chat_id
      await client.edit_message(event.message, f"𝚄𝙽𝙶𝙱𝙰𝙽𝙽𝙸𝙽𝙶..  {userid}") 
      time.sleep(2)
      async for gfuck in event.client.iter_dialogs():
        if gfuck.is_group or gfuck.is_channel:
          try:
            await event.client.edit_permissions(gfuck.id, userid, view_messages=True)
            chats += 1
            
          except:
            pass
            
      await client.edit_message(event.message,f"""
          
           
  𝙲𝙾𝙽𝙶𝚁𝙰𝚃𝚄𝙻𝙰𝚃𝙸𝙾𝙽𝚂 🥳 {userid} 🥳
  
  𝚈𝙾𝚄 𝙰𝚁𝙴 𝚄𝙽𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝙸𝙽
  {𝚌𝚑𝚊𝚝𝚜} 𝙲𝙷𝙰𝚃𝚂 𝙰𝙽𝙳 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂
   𝙱𝚈 👹𝙱𝙴𝙰𝚂𝚃 𝙱𝙾𝚃👹..
  
  𝙸𝙵 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝙰𝙽𝚈 𝙲𝙾𝙼𝙿𝙻𝙰𝙸𝙽𝚃𝚂 
  𝚂𝙿𝙴𝙰𝙺 𝚆𝙸𝚃𝙷 𝙼𝚈 𝙲𝚁𝙴𝙰𝚃𝙾𝚁
  𝙷𝙰𝙿𝙿𝚈 𝙶𝙾𝚃 𝙶𝙱𝙰𝙽𝙽𝙴𝙳 𝙳𝙰𝚈
  
  """)
         
         
         
  elif not event.is_reply and not event.is_private:
    await event.reply("𝚄𝙽𝙶𝙱𝙰𝙽 𝙰 𝚄𝚂𝙴𝚁 𝙱𝚈 𝚁𝙴𝙿𝙻𝚈𝙸𝙽𝙶 𝙰 𝙼𝙴𝚂𝚂𝙰𝙶𝙴")
    

agb = {}

@events.register(events.NewMessage(outgoing=True, pattern=r'\.allgban'))
async def all_gban(event):
  chat = event.get_chat
  b=""
  x=0
  for i in r:
    chats = random.randint(120,160)
    z = await client.get_entity(i)
    y = "@" + z.username  
    x+= 1  
    a = f"𝙶𝙱𝙰𝙽 𝙸𝙽𝙵𝙾 {𝚡} \n\n𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {y}\n𝚁𝙴𝙰𝚂𝙾𝙽 : {r[i]}\n𝙲𝙷𝙰𝚃𝚂 : {chats}\n\n"
    p = "\n"
    b = b + p + a
    await client.edit_message(event.message,b)

@events.register(events.NewMessage(outgoing = True,pattern = r"\.gmute"))
async def gmute(event):
  private = False
  gsql = []
  chat=await event.get_reply_message()
  userid=(chat.sender.id)
  async for gfuck in event.client.iter_dialogs():
    if gfuck.is_group or gfuck.is_channel:
      try:
        await event.client.edit_permissions(gfuck.id, userid, send_messages=False)
        chats += 1      
      except Exception as e:
        
        pass
  gsql.append(userid)
  await client.edit_message(event.message, "Shhh.... Now keep quiet !!")
    
    
        
@events.register(events.NewMessage(outgoing = True,pattern = r"\.ungmute"))
async def ungmute(event):
  private = False
  gsql = []
  chat=await event.get_reply_message()
  userid=(chat.sender.id)
  async for gfuck in event.client.iter_dialogs():
    if gfuck.is_group or gfuck.is_channel:
      try:
        await event.client.edit_permissions(gfuck.id, userid, send_messages=True)
        chats += 1      
      except Exception as e:
        
        pass
  gsql.append(userid)
  await client.edit_message(event.message, "NOW YOU CAN TALK AS A FREE BIRD")






