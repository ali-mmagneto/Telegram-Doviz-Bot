# Kutuphaneleri import ediyoruz
import os
import requests
import json
import pyrogram
from pyrogram import Client
from pyrogram import filters

from os import getenv, environ

bot_token = os.environ['BOT_TOKEN']
api_id = int(os.environ['API_ID'])
api_hash = os.environ['API_HASH']

# Telegram sunucusuna bagliyoruz
app = Client(
    "LambdaBot",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash
)

# Json ile veri cekiyoruz
dovizjson = "https://api.agacinayetvar.ml/canli.json"


# Baslat komutunda atilacak mesaji ayarliyoruz
@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, f"""**Merhaba** {message.from_user.first_name}.
**Ben Sana Güncel Doviz Kurunu Aktarıcam Komutları öğrenmek için /help komutunu Kullan.**
""")

# Degiskenlere atadigimiz veriyi Telegram'a yukluyoruz
@app.on_message(filters.command("dolar"))
async def doviz(client, message):
    dovizcek = requests.get(dovizjson)
    dovizveri = json.loads(dovizcek.text)
    dolar = dovizveri["veriler"][0]
    await client.send_message(message.chat.id, f"""**USD/TL**
**Alış:** ```{dolar["alis"]}```\n**Satış:** ```{dolar["satis"]}```\n**Fark:** ```{dolar["fark"]}```""")
    
@app.on_message(filters.command("euro"))
async def euro(client, message):
    dovizcek = requests.get(dovizjson)
    dovizveri = json.loads(dovizcek.text)
    euro = dovizveri["veriler"][1]
    await client.send_message(message.chat.id, f"""**EURO/TL**
**Alış:** ```{euro["alis"]}```\n**Satış:** ```{euro["satis"]}```\n**Fark:** ```{euro["fark"]}```""")
    
    
@app.on_message(filters.command("help"))
async def help(client, message):
    await client.send_message(message.chat.id, f"""
**Dolar**:  ```/dolar```
**Euro**: ```/euro```
**Adam Olana çok bile**
""")    
    
app.run()
