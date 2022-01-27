from telethon import TelegramClient, events
import beastbot.client


client = beastbot.client.client











q = (
  
  "────██──────▀▀▀██\n"
    "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
    "▄▀──█▄▄──────█─█▄▄\n"
    "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
    "─▀───────▀▀─▀───────▀▀\n🚶🏻‍♂️🚶🏻‍♂️ɮʏɛ ʄʀɨɛռɖֆ.."

  
)

famiily = ("""
𝗗𝗘𝗔𝗥 𝗙𝗖𝗞𝗘𝗥 𝗢𝗪𝗡𝗘𝗥 𝗕𝗘𝗔𝗦𝗧

𝗬𝗢𝗨𝗥 𝗙𝗔𝗠𝗜𝗟𝗬 𝗜𝗦 𝗙𝗨𝗟𝗟 𝗢𝗙 𝗣𝗜𝗥𝗢𝗦
🔥🔥🔥
𝗜 𝗙𝗢𝗥𝗚𝗢𝗧 𝗧𝗢 𝗦𝗔𝗬 𝗘𝗫𝗖𝗘𝗣𝗧 𝗬𝗢𝗨.\n𝗔𝗟𝗟 𝗔𝗥𝗘 𝗣𝗜𝗥𝗢𝗦

\n\n𝗘𝗩𝗜𝗟 𝗙𝗔𝗧𝗛𝗘𝗥, 
𝗬𝗔𝗗𝗨, 
𝗧𝗛𝗢𝗥, 
𝗨𝗗𝗜𝗧, 
𝗥𝗢𝗕𝗜𝗡, 
𝗗𝗘𝗕

""")

@events.register(events.NewMessage(outgoing=True, pattern=r'\.bye'))

async def byee(event):
  chat = await event.get_chat()
  await client.edit_message(event.message, q)


#@events.register(event.NewMessage(outgoing=True, pattern=r'\.family'))
#async def family(event):
 # chat = await event.get_chat()
 # await client.edit_message(event.message, famiily)

@events.register(events.NewMessage(outgoing=True, pattern=r'\.family'))

async def family(event):
  chat = await event.get_chat()
  await client.edit_message(event.message, famiily)





