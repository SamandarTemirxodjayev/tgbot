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
    if (message.text.find('Uc') != -1 or message.text.find('uc') != -1 or message.text.find('UC') != -1) and message.chat.type == 'private' and filters.user:
      app.send_message(message.chat.id,"Qancha",reply_to_message_id=message.message_id)
    print(message)
    f = open("data.txt", "a+")
    
    text = '"Date: "'+ str(message.date) + '\n' + '"Message": "' + message.text + '"\n' + '"chat_id": "' + str(message.chat.id) + '"\n\n'
    f.write(text)
    f.close()

app.run()