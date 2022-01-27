from telethon import TelegramClient





api_id = 2724713
api_hash = "fbcd36359ec632d453539eea3934c718"
bot_token = '5015741515:AAENkLa22nkzrnGhShIVajlTRRlwidQ9mzs'

client = TelegramClient('man', api_id, api_hash)

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
