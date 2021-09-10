from pyrogram import Client, filters
from pyrogram.errors import FloodWait
 
from pyrogram.types import ChatPermissions
 
import time
from time import sleep
import random
 
app = Client("my_account")
@app.on_message(filters.text & ~filters.edited)
def my_handler(client, message):
    if (message.text.find('Salom') != -1 or message.text.find('salom') != -1) and message.chat.type == 'private' and filters.user:
      app.send_message(message.chat.id,"Salom nima xizmat",reply_to_message_id=message.message_id)
    if (message.text.find('uc qancha') != -1 or message.text.find('uc ') != -1 or message.text.find('Uc ') != -1 or message.text.find('UC ') != -1) and message.chat.type == 'private' and filters.user:
      app.send_message(message.chat.id,"""
<b>🌙  PUBG Mobile ga ko'proq va arzonroq donat qilmoqchimisiz ? 😍  Bizda siz uchun aksiya narxlari:

🔝 Aksiyadagi UC narxlari:
💵 360 UC – 57.000 so'm
💵 750 UC – 110.000 so'm
💵 2055 UC – 265.000 so'm
💵 4450 UC – 555.000 so'm
💵 9480 UC – 1.095.000 so'm

⌛️ Bular vaqtinchalik  aksiya va bitta iD raqamga bir marta tashlanadi xolos shoshiling...💯

✍🏻 Murojat uchun: @method_uz</b>""",reply_to_message_id=message.message_id)
      app.send_message(message.chat.id,"""<b>
Eng arzon UC METHOD UZ🤩🥳
➖➖➖➖➖➖➖➖
🌍 GLOBAL 
 60  💸UC - 10.000 min 🔥
120  💸UC - 20.000 min
180 💸UC - 29.000 min
240 💸UC - 39.000 min
300 💸UC - 49.000 min RP🔥
360 💸UC - 57.000 min RP🔥
600 💸UC - 100.000 min 
660 💸UC - 103.000 min 
900 💸UC - 150.000 min RP🔥
960 💸UC - 159.000 min RP🔥
1320💸UC - 205.000 min
2100💸UC- 310.000 min
1800💸UC - 265.000 min
3850💸UC - 500.000 min
8100💸UC - 990.000 min
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
🖤 Bizda hammasi ishonchli va kafolatlangan !!!✔️
💥 Bog'lanish 👉 @Method_UZ
‼️ +998995363021 saxranit qilib qo'ying 😉
        </b>""",parse_mode="html")
      app.send_message(message.chat.id,"""<b>
Donaterlarimiz uchun Super muper skidka🔥😍
Akkauntga kirib olib berish xizmati yana ishga tushdi!💣

💸 325uc - 50.000 so'm💣
💸 660uc - 87.000 so'm💣
💸 1800uc - 220.000 so'm💣
💸 3850uc - 470.000 so'm💣
💸 8100 UC - 850.000 so'm💣
💸 16.200 UC - 1.700.000 so'm💣
💸 105.300 UC - 11.600.000 so'm💣

(UC akkauntga kirib tashlab beriladi!)✅
➖➖➖➖➖➖➖➖➖
TO'LOV YO'LLARI💳!

1️⃣KARTADAN KARTAGA PUL O'TKAZISH!
2️⃣PAYNETDAN KARTAGA PUL O'TKAZISH!
➖➖➖➖➖➖➖➖➖
📍TELEGRAM: @Method_UZ
📞TELEFON: +998995363021
➖➖➖➖➖➖➖➖➖
ILTIMOS NOMERNI SOXRANIT QILING!
(MASHENNIKLARDAN EXTIYOT BO'LING!)
     </b> """,parse_mode="html")
    if (message.text.find('Karta') != -1 or message.text.find('karta') != -1 or message.text.find('Карта') != -1 or message.text.find('карта') != -1) and message.chat.type == 'private' and filters.user:
      app.send_message(message.chat.id,"""
<b>💳 HUMO 9860 1601 0180 8782
💳 UZCARD 8600 4904 4794 8779</b>
 🙍‍♂️ TEMIRKHODJAEVA RAKHIMA

To'lov qilgandan so'ng chekni rasm isbotini yuborishingiz shart!😊""",parse_mode="html")
    if (message.text.find('alo') != -1 or message.text.find('Alo') != -1) and message.chat.type == 'private' and filters.user:
      app.send_message(message.chat.id,'Kutish vaqti 5-15 daqiqagacha')
    print(message)
    f = open("data.txt", "a+")
    text = '"Date: "'+ str(message.date) + '\n' + '"Message": "' + message.text + '"\n' + '"chat_id": "' + str(message.chat.id) + '"\n\n'
    f.write(text)
    f.close()
@app.on_message(filters.audio)
def my_handler(client, message):
    print(message)
@app.on_message(filters.photo)
def my_handler(client, message):
    print(message)
@app.on_message(filters.voice)
def my_handler(client, message):
    print(message)
@app.on_message(filters.video)
def my_handler(client, message):
    print(message)

app.run()