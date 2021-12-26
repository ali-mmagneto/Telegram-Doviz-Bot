# Kutuphaneleri import ediyoruz
import requests
import json
import pyrogram
from pyrogram import Client
from pyrogram import filters
import os

@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, f"""
**Merhaba İnsancık Ben Sana Güncel Doviz Kurunu Aktarıcam Komutları öğrenmek için /help komutunu Kullan.**""")

app.run()
