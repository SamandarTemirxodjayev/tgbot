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
π METHOD UZ kanalida aksiya
π YANADA KO'PROQ UC π

πPUBG MOBILE UC πΈ
(ID orqali tashlab beramiza)
πΈ 30UC - 7.000 β
πΈ 40 UC - 9.000 β
πΈ 60 UC - 11.000 π³
πΈ 63 UC - 11.500 β
πΈ 120 UC - 22.000 β
πΈ 126 UC - 23.000 β
πΈ 180 UC - 33.000 π
πΈ 189 UC - 36.000 π
πΈ 240 UC - 44.000 β
πΈ 252 UC - 46.000 β
πΈ 300 UC - 52.000 β RP
πΈ 325 UC - 53.000 π± RP
πΈ 340 UC - 56.000 π± RP
πΈ 360 UC - 60.000 π± RP
πΈ 385 UC - 64.000 π± RP 
πΈ 445 UC - 76.000 π±
πΈ 505 UC - 87.000 π±
πΈ 565 UC - 98.000 π±
πΈ 660 UC - 104.000 π ππ
πΈ 690 UC- 110.000 π ππ
πΈ 720 UC - 115.000 β
πΈ 900UC - 149.000 βElite RP
πΈ 985 UC - 156.000 βElite RP
πΈ 1320 UC - 208.000 β
πΈ 1800 UC - 259.000 π± 
πΈ 1875 UC - 265.000 π± 
πΈ 2125 UC - 316.000 β
πΈ 3850 UC - 505.000 β
πΈ 4000 UC - 555.000 β
πΈ 8100 UC - 980.000 π₯³
πΈ 8400 UC - 1.095.000 π₯³
πΈ 16200 UC - 1.970.000 β
πΈ 24300 UC - 2.965.000 π₯³

π°π· PUBG KOREYSKIY UC πΈ
(Koreyskiy UC uchun akkaunt login va paroli kerak bo'ladi)
π° 60UC - 11.000π
π° 190UC - 32.000π
π° 660UC - 99.000π
π° 1800UC - 289.000π
π° 3850UC - 570.000π
π° 8100UC - 1.095.000π
π° Boshqa miqdorda UC larni ham ob beramizaπ

π³ PUBG MOBILE LITE BC πΈ
(PUBG LITE BC uchun akkaunt login va paroli kerak bo'ladi)
π 90BC - 12.000βοΈ
π 180BC - 24.000βοΈ
π 285BC - 36.000βοΈWP 
π 480BC - 54.000βοΈ
π 975BC - 110.000βοΈ ELITE WP
π 2550BC - 280.000βοΈ
π 5250BC - 555.000βοΈ
π Boshqa miqdorda UC larni ham ob beramizaβοΈ

π³ To'lovlar qabul qilish:
1οΈβ£ Kartadan kartaga pul o'tkazish
2οΈβ£ Kartaga PAYNET orqali pul to'lash
βββββββββββββ
πTo'lov oldindan amalga oshiriladi:
πΊπΏ HUMO  9860 1601 0180 8782
β UZCARD 8600 4904 4794 8779
βββββββββββββ
π±Telefon raqam: +998995363021
π¨βπ»Telegram: @Method_UZ
π€ Botimiza: @Method_UZbot
βοΈIsbotlar: @Method_UZ_Isbot
        </b>""",parse_mode="html")
      app.send_message(message.chat.id,"""<b>
Super muper skidkaπ₯π
Akkauntga kirib olib berish xizmati yana ishga tushdi!π£

πΈ 325uc - 50.000 so'mπ£
πΈ 660uc - 87.000 so'mπ£
πΈ 1800uc - 220.000 so'mπ£
πΈ 3850uc - 470.000 so'mπ£
πΈ 8100 UC - 850.000 so'mπ£
πΈ 16.200 UC - 1.700.000 so'mπ£
πΈ 105.300 UC - 11.600.000 so'mπ£

(UC akkauntga kirib tashlab beriladi!)β
βββββββββ
TO'LOV YO'LLARIπ³!

1οΈβ£KARTADAN KARTAGA PUL O'TKAZISH!
2οΈβ£PAYNETDAN KARTAGA PUL O'TKAZISH!
βββββββββ
πTELEGRAM: @Method_UZ
πTELEFON: +998995363021
βββββββββ
ILTIMOS NOMERNI SOXRANIT QILING!
(MASHENNIKLARDAN EXTIYOT BO'LING!)
     </b> """,parse_mode="html")
      app.send_photo(message.chat.id,'aksiya.jpg',caption="""<b>
Bomba aksiyaπΉ

Endi siz Bizdan UC xarid qilib rasmdagi narsalarni qo'lga kiritishingiz mumkinπ±

Agar siz 1030UC xarid qilsangiz 126UCdan 1030UCgacha bo'lgan barcha sovg'alarni olishingiz muminππ

πΉ126UC - 23.000so'mπ₯
πΉ252UC - 46.000so'mπ₯
πΉ504UC - 92.000so'mπ₯
πΉ690UC - 110.000so'mπ₯
πΉ1030UC - 167.000so'mπ₯

ββββββββββ
 π Orqali tashlab beriladiπ
ββββββββββ
TO'LOV YO'LLARIπ³!

1οΈβ£KARTADAN KARTAGA PUL O'TKAZISH!
2οΈβ£PAYNETDAN KARTAGA PUL O'TKAZISH!
ββββββββββ

πArzon, ishonchli va omadli UC sotib olish uchunπ
π@Method_UZπ
      </b>""")
    if (message.text.find('Karta') != -1 or message.text.find('karta') != -1 or message.text.find('ΠΠ°ΡΡΠ°') != -1 or message.text.find('ΠΊΠ°ΡΡΠ°') != -1) and message.chat.type == 'private' and filters.user:
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