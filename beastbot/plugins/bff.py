from telethon import events
import beastbot.client


client = beastbot.client.client

@events.register(events.NewMessage(outgoing=True, pattern=r'\.bff'))
async def bffs(event):
  chat = await event.get_chat()
  await client.edit_message(event.message, "𝗠𝗬 BFF 𝗔𝗥𝗘 𝗘𝗩𝗜𝗟 𝗙𝗔𝗧𝗛𝗘𝗥 & 𝗬𝗔𝗗𝗨𝗛𝗔𝗖𝗞𝗘𝗥")
