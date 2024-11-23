from telethon import TelegramClient





api_id = 
api_hash =
bot_token =

client = TelegramClient('man', api_id, api_hash)

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
