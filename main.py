import requests
import json
import pyrogram
from pyrogram import Client
from pyrogram import filters
import os

from os import getenv, environ

bot_token = os.environ['BOT_TOKEN']
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

# Telegram sunucusuna bagliyoruz
app = Client(
    "Dovizbot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins=datalar
)

app.run()
