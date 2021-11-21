from pyrogram import Client
from configs import Config

Bot = Client(
    session_name='Thumbnail bot',
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)
