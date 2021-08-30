from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token='1908018172:AAE9JKSivMC3Q9Dn3yDIwZaLct-ni1hC4tA')
dp = Dispatcher(bot)

keyboardMain = ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton('🛍 Magazin')).row(KeyboardButton('👭 Referal'), KeyboardButton('📞 Aloqa'), KeyboardButton('🗂 Isbotlar')).add(KeyboardButton('⚙️ Tilni tanlash'))
keyboardProof = InlineKeyboardMarkup().add(InlineKeyboardButton('Barcha isbotlar kanali', url='https://t.me/method_uz_isbot'))

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
  await message.reply("😊 Botga xush kelibsiz!",reply_markup=keyboardMain)

@dp.message_handler()
async def echo_message(msg: types.Message):
  if msg.text == '📞 Aloqa':
    await bot.send_message(msg.chat.id, "Xizmatimizga tegishli savollar / takliflaringiz bo'lsa biz bilan bog'laning.\nBiz bilan Aloqa:\n\nQo'llab-quvvatlash xizmati:\n📬 Telegram: @Method_UZ\n📞 Telefon: +998995363021\n👨‍💻 Dasturchi: @Method_UZ",reply_markup=keyboardMain)
  if msg.text == '🗂 Isbotlar':
    await bot.send_message(msg.chat.id,'Barcha isbotlar shu yerda⤵️',reply_markup=keyboardProof)
  print(msg)

if __name__ == '__main__':
    executor.start_polling(dp)