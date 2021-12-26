import requests
import json
import pyrogram
from pyrogram import Client
from pyrogram import filters
import os

# Json ile veri cekiyoruz
dovizjson = "api.agacinayetvar.ml/doviz.json"

@app.on_message(filters.command("dolar"))
async def dolar(client, message):
    dovizcek = requests.get(dovizjson)
    dovizveri = json.loads(dovizcek.text)
    dolar = dovizveri["veriler"][0]
    await client.send_message(message.chat.id, f"""**USD/TL**
**Alış:** ```{dolar["alis"]}```\n**Satış:** ```{dolar["satis"]}```\n**Fark:** ```{dolar["fark"]}```""")
    
    app.run()
