# Kutuphaneleri import ediyoruz
import requests
from pyrogram.types.bots_and_keyboards import InlineKeyboardButton, InlineKeyboardMarkup
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
dovizjson = "https://api.agacinayetvar.ml/canli.json"


# Baslat komutunda atilacak mesaji ayarliyoruz
@app.on_message(filters.command("start"))
async def start(client, message):
    await client.send_message(message.chat.id, f"""
**Merhaba İnsancık Ben Sana Güncel Doviz Kurunu Aktarıcam Komutları öğrenmek için /help komutunu Kullan.**""", 
reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(text="buraya metin", url=f"buraya url")]]))

# Degiskenlere atadigimiz veriyi Telegram'a yukluyoruz
@app.on_message(filters.command("dolar"))
async def dolar(client, message):
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

@app.on_message(filters.command("sterlin"))
async def sterlin(client, message):
    dovizcek = requests.get(dovizjson)
    dovizveri = json.loads(dovizcek.text)
    ingilizsterlini  = dovizveri["veriler"][2]
    await client.send_message(message.chat.id, f"""**İngiliz Sterlini/TL**
**Alış:** ```{ingilizsterlini["alis"]}```\n**Satış:** ```{ingilizsterlini["satis"]}```\n**Fark:** ```{ingilizsterlini["fark"]}```""")
    
@app.on_message(filters.command("kanadadolar"))
async def sterlin(client, message):
    dovizcek = requests.get(dovizjson)
    dovizveri = json.loads(dovizcek.text)
    kanadadoları  = dovizveri["veriler"][3]
    await client.send_message(message.chat.id, f"""**Kanada Doları/TL**
**Alış:** ```{kanadadoları["alis"]}```\n**Satış:** ```{kanadadoları["satis"]}```\n**Fark:** ```{kanadadoları["fark"]}```""")

@app.on_message(filters.command("frang"))
async def sterlin(client, message):
    dovizcek = requests.get(dovizjson)
    dovizveri = json.loads(dovizcek.text)
    isviçrefrangı  = dovizveri["veriler"][4]
    await client.send_message(message.chat.id, f"""**İsviçre Frangı/TL**
**Alış:** ```{isviçrefrangı["alis"]}```\n**Satış:** ```{isviçrefrangı["satis"]}```\n**Fark:** ```{isviçrefrangı["fark"]}```""")
    
@app.on_message(filters.command("help"))
async def help(client, message):
    await client.send_message(message.chat.id, f"""
**Dolar**: /dolar
**Euro**: /euro
**İngiliz Sterlini**: /sterlin
**İsviçre Frangı**: /frang
**Kanada Doları**: /kanadadolar
**Adam Olana çok bile**
""")    
    
app.run()
