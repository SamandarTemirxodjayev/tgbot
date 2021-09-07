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
    if (message.text.find('uc qancha') != -1 or message.text.find('uc') != -1 or message.text.find('Uc') != -1) and message.chat.type == 'private' and filters.user:
      app.send_message(message.chat.id,"""
[🇺🇿] AKSIYA UC 💸/ АКЦИЯ UC 💸

 60  💸UC - 12.000 min 🔥
120 💸UC - 24.000 min 🔥
180 💸UC - 35.000 min 🔥
240 💸UC - 42.000 min 🔥
300 💸UC - 50.000 min RP🔥
360 💸UC - 59.000 min RP🔥
600 💸UC - 99.000 min 🔥
660 💸UC - 104.000 min🔥
900 💸UC - 149.000 min RP🔥
960 💸UC - 159.000 min RP🔥
➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖ ➖
✅Isbot kanal/Barcha to'lovlar 📥:@blacksgarant""",reply_to_message_id=message.message_id)
    if message.text.find('Karta') != -1 message.text.find('karta') != -1 or message.text.find('Карта') != -1 or message.text.find('карта') != -1:
      app.send_message(message.chat.id,""""
💳 8600120470390884
 🙍‍♂️ Журабоев Жахонгир

👆UZCARD

To'lov qilgandan so'ng chekni rasm isbotini yuborishingiz shart!😊""")
    if message.text.find('alo') != -1 or message.text.find('Alo') != -1:
      app.send_message(message.chat.id,'Kutish vaqti 5-15 daqiqagacha')
    if message.text.find('')
    print(message)
    f = open("data.txt", "a+")
    
    text = '"Date: "'+ str(message.date) + '\n' + '"Message": "' + message.text + '"\n' + '"chat_id": "' + str(message.chat.id) + '"\n\n'
    f.write(text)
    f.close()

app.run()