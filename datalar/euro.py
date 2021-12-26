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

# Json ile veri cekiyoruz
dovizjson = "api.agacinayetvar.ml/doviz.json"

@app.on_message(filters.command("euro"))
async def euro(client, message):
    dovizcek = requests.get(dovizjson)
    dovizveri = json.loads(dovizcek.text)
    euro = dovizveri["veriler"][1]
    await client.send_message(message.chat.id, f"""**EURO/TL**
**Alış:** ```{euro["alis"]}```\n**Satış:** ```{euro["satis"]}```\n**Fark:** ```{euro["fark"]}```""")
