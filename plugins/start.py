# Kutuphaneleri import ediyoruz
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
    api_hash=api_hash
)

dovizjson = "api.agacinayetvar.ml/doviz.json"

@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, f"""
**Merhaba İnsancık Ben Sana Güncel Doviz Kurunu Aktarıcam Komutları öğrenmek için /help komutunu Kullan.**""")

app.run()
