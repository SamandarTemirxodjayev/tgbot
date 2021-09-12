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
      app.send_message(message.chat.id,"""<b>
📆 METHOD UZ kanalida aksiya
🌏 YANADA KO'PROQ UC 🌏

🏁PUBG MOBILE UC 💸
(ID orqali tashlab beramiza)
💸 30UC - 7.000 ✅
💸 40 UC - 9.000 ✅
💸 60 UC - 11.000 😳
💸 63 UC - 11.500 ✅
💸 120 UC - 22.000 ✅
💸 126 UC - 23.000 ✅
💸 180 UC - 33.000 😍
💸 189 UC - 36.000 😍
💸 240 UC - 44.000 ✅
💸 252 UC - 46.000 ✅
💸 300 UC - 52.000 ✅ RP
💸 325 UC - 53.000 😱 RP
💸 340 UC - 56.000 😱 RP
💸 360 UC - 60.000 😱 RP
💸 385 UC - 64.000 😱 RP 
💸 445 UC - 76.000 😱
💸 505 UC - 87.000 😱
💸 565 UC - 98.000 😱
💸 660 UC - 104.000 💎 😏🛍
💸 690 UC- 110.000 💎 😏🛍
💸 720 UC - 115.000 ✅
💸 900UC - 149.000 ✅Elite RP
💸 985 UC - 156.000 ✅Elite RP
💸 1320 UC - 208.000 ✅
💸 1800 UC - 259.000 🔱 
💸 1875 UC - 265.000 🔱 
💸 2125 UC - 316.000 ✅
💸 3850 UC - 505.000 ✅
💸 4000 UC - 555.000 ✅
💸 8100 UC - 980.000 🥳
💸 8400 UC - 1.095.000 🥳
💸 16200 UC - 1.970.000 ✅
💸 24300 UC - 2.965.000 🥳

🇰🇷 PUBG KOREYSKIY UC 💸
(Koreyskiy UC uchun akkaunt login va paroli kerak bo'ladi)
🔰 60UC - 11.000🏆
🔰 190UC - 32.000🏆
🔰 660UC - 99.000🏆
🔰 1800UC - 289.000🏆
🔰 3850UC - 570.000🏆
🔰 8100UC - 1.095.000🏆
🔰 Boshqa miqdorda UC larni ham ob beramiza🏆

🏳 PUBG MOBILE LITE BC 💸
(PUBG LITE BC uchun akkaunt login va paroli kerak bo'ladi)
🎁 90BC - 12.000☑️
🎁 180BC - 24.000☑️
🎁 285BC - 36.000☑️WP 
🎁 480BC - 54.000☑️
🎁 975BC - 110.000☑️ ELITE WP
🎁 2550BC - 280.000☑️
🎁 5250BC - 555.000☑️
🎁 Boshqa miqdorda UC larni ham ob beramiza☑️

💳 To'lovlar qabul qilish:
1️⃣ Kartadan kartaga pul o'tkazish
2️⃣ Kartaga PAYNET orqali pul to'lash
➖➖➖➖➖➖➖➖➖➖➖➖➖
💎To'lov oldindan amalga oshiriladi:
🇺🇿 HUMO  9860 1601 0180 8782
✅ UZCARD 8600 4904 4794 8779
➖➖➖➖➖➖➖➖➖➖➖➖➖
📱Telefon raqam: +998995363021
👨‍💻Telegram: @Method_UZ
🤖 Botimiza: @Method_UZbot
☑️Isbotlar: @Method_UZ_Isbot
        </b>""",parse_mode="html")
      app.send_message(message.chat.id,"""<b>
Super muper skidka🔥😍
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
      app.send_photo(message.chat.id,'aksiya.jpg',caption="""<b>
Bomba aksiya🌹

Endi siz Bizdan UC xarid qilib rasmdagi narsalarni qo'lga kiritishingiz mumkin😱

Agar siz 1030UC xarid qilsangiz 126UCdan 1030UCgacha bo'lgan barcha sovg'alarni olishingiz mumin👌😏

🌹126UC - 23.000so'm🔥
🌹252UC - 46.000so'm🔥
🌹504UC - 92.000so'm🔥
🌹690UC - 110.000so'm🔥
🌹1030UC - 167.000so'm🔥

➖➖➖➖➖➖➖➖➖➖
 🆔 Orqali tashlab beriladi👌
➖➖➖➖➖➖➖➖➖➖
TO'LOV YO'LLARI💳!

1️⃣KARTADAN KARTAGA PUL O'TKAZISH!
2️⃣PAYNETDAN KARTAGA PUL O'TKAZISH!
➖➖➖➖➖➖➖➖➖➖

😏Arzon, ishonchli va omadli UC sotib olish uchun👇
😋@Method_UZ😋
      </b>""")
    if (message.text.find('Karta') != -1 or message.text.find('karta') != -1 or message.text.find('Карта') != -1 or message.text.find('карта') != -1) and message.chat.type == 'private' and filters.user:
      app.send_sticker(message.chat.id,'karta_humo.webp')
      app.send_sticker(message.chat.id,'karta_uzcard.webp')
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