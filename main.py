# Kutuphaneleri import ediyoruz
import requests
import json
import pyrogram
from pyrogram import Client
from pyrogram import filters
import os


#load_dotenv(".env", override=True)
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
    await client.send_message(message.chat.id, f"""**Welcome** @{message.from_user.username}.
**Grup**: ```{message.chat.title}```
**Davet Linki**:  ```t.me/{message.chat.username}```
**Snein Kullanıcı İd'in**: ```{message.from_user.id}```
Daha fazla yardıma ihtiyacınız olursa özel sohbetten benimle iletişime geçebilirsiniz. .
""")

# Degiskenlere atadigimiz veriyi Telegram'a yukluyoruz
@app.on_message(filters.command("dolar"))
async def doviz(client, message):
    dovizcek = requests.get(dovizjson)
    dovizveri = json.loads(dovizcek.text)
    dolar = dovizveri.Anlik[0]
    await client.send_message(message.chat.id, f"""
Dolar: ```Alış: {dolar.alis}\nSatış: {dolar.satis}```""")

app.run()
