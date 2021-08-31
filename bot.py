from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

photo_url = 'https://t.me/dhdhdhdjsjei389/2'
bot = Bot(token='1888770200:AAFfyUZg4ZEljYeE2ID7aUeFjS9jzenJjdY')
dp = Dispatcher(bot)

keyboardMain = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('🛍 Magazin')).row(KeyboardButton('👭 Referal'), KeyboardButton('📞 Aloqa'), KeyboardButton('🗂 Isbotlar')).add(KeyboardButton('⚙️ Tilni tanlash'))
keyboardProof = InlineKeyboardMarkup().add(InlineKeyboardButton('Barcha isbotlar kanali', url='https://t.me/method_uz_isbot'))
keyboardShop = InlineKeyboardMarkup().add(InlineKeyboardButton('🔥 PUBG MOBILE 🔥', callback_data='pubgmobile')).add(InlineKeyboardButton('🗃 PUBG MOBILE PRIME 🗃', callback_data='pubgmobileprime'))
keyboardPUBGMOBILE = InlineKeyboardMarkup().add(InlineKeyboardButton('💸 60 UC - 35rubl 🔥', callback_data='uc60')).add(InlineKeyboardButton('💸 180 UC - 229rubl 🔥', callback_data='uc180')).add(InlineKeyboardButton('💸 325 UC - 379rubl 🔥', callback_data='uc325')).add(InlineKeyboardButton('💸 660 UC - 749rubl 🔥', callback_data='uc660')).add(InlineKeyboardButton('💸 1800 UC - 1890rubl 🔥', callback_data='uc1800'))
@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
  await message.reply("😊 Botga xush kelibsiz!",reply_markup=keyboardMain)

@dp.message_handler()
async def echo_message(msg: types.Message):
  if msg.text == '📞 Aloqa':
    await bot.send_message(msg.chat.id, "Xizmatimizga tegishli savollar / takliflaringiz bo'lsa biz bilan bog'laning.\nBiz bilan Aloqa:\n\nQo'llab-quvvatlash xizmati:\n📬 Telegram: @Method_UZ\n📞 Telefon: +998995363021\n👨‍💻 Dasturchi: @Method_UZ",reply_markup=keyboardMain)
  if msg.text == '🗂 Isbotlar':
    await bot.send_message(msg.chat.id,'Barcha isbotlar shu yerda⤵️',reply_markup=keyboardProof)
  if msg.text == '👭 Referal':
    await bot.send_message(msg.chat.id,'🤝 Referal tizim:\n🔑 Siz olasiz:\n▫️ Referaliz istalgan mahsulot harididan 1%\n\n🔗 Sizning referal havolangiz: https://t.me/Method_UZbot?start='+str(msg.chat.id)+'\n/n🎊 Siz taklif qilgan odamlar soni: 47ta\n💲 Siz ishlagan summa: 0so\'m',reply_markup=keyboardMain)
  if msg.text == '🛍 Magazin':
    await bot.send_photo(msg.chat.id,photo_url,caption="Magazinga xush kelibsiz. 😊\nQaysi o'yinga Donat qilmoqchisiz? 🔥\n\nBizda siz uchun 'PUBG MOBILE' o'yini uchun BOMBA narxlar 🧨",reply_markup=keyboardShop)
  print(msg)

@dp.callback_query_handler()
async def callback(call: types.CallbackQuery):
  if call.data == 'pubgmobile':
   await bot.delete_message(call.from_user.id, call.message.message_id)
   await bot.send_photo(call.from_user.id,photo_url,"Marhamat o'zingiz xohlagan mahsulotni tanlashingiz mumkin! ✅",reply_markup=keyboardPUBGMOBILE)
  print(call)

if __name__ == '__main__':
    executor.start_polling(dp)