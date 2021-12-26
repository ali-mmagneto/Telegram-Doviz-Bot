import requests
import json
import pyrogram
from pyrogram import Client
from pyrogram import filters
import os

# Json ile veri cekiyoruz
dovizjson = "api.agacinayetvar.ml/doviz.json"

@app.on_message(filters.command("euro"))
async def euro(client, message):
    dovizcek = requests.get(dovizjson)
    dovizveri = json.loads(dovizcek.text)
    euro = dovizveri["veriler"][1]
    await client.send_message(message.chat.id, f"""**EURO/TL**
**Alış:** ```{euro["alis"]}```\n**Satış:** ```{euro["satis"]}```\n**Fark:** ```{euro["fark"]}```""")

app.run()
