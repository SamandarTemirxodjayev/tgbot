const TelegramBot = require('node-telegram-bot-api')
const bot = new TelegramBot('1641750487:AAHd4Xv1n7HHWUINbpWYDMiPoqCy_BG4Fsg', {polling: true})
bot.on('text', async (message) => {
    message.send = (text, params) => bot.sendMessage(message.chat.id, text, params)
    if(message.text == "/start"){
        return message.send(`
✌️ <b>Привет, ${message.from.first_name}</b>
📝 <b>Цель игры:</b>
├─Пополняем счет 🤘
├─Покупаем танки 💎
├─Собираем доход 💸
├─Обмениваем доход 💵
└─Получаем деньги 💹
❓ Чем мы выплачиваем?
❗️ С пополнений бота, продажи рекламы и других наших проектов
🏝 <b>Чат</b> 👉 @WoT_Chats
💳 <b>Выплаты</b> 👉 @WoT_Pay
📢 <b>Новости</b> 👉 @WoT_infoo`, {
			parse_mode: "HTML"
	    })
    }
})
