const token = '1680049120:AAH0IY83YSdLJguqUN4zfN46O5WN9Y2YjbA'
const TelegramBot = require('node-telegram-bot-api')
const bot = new TelegramBot(token, {polling: true})

bot.on('text', async (message) => {
    if (message.text == '/start') {
        message.send = (text, params) => bot.sendMessage(message.chat.id, text, params);
        return message.send(`✌️ <b>Привет, ${message.from.first_name}</b>
📝 <b>Цель игры:</b>
├─Пополняем счет 🤘
├─Покупаем команды 🏆
├─Собираем Голы 🎖
├─Обмениваем Голы 💵
└─Получаем деньги 💹

❓ Чем мы выплачиваем?
❗️ С пополнения бота, продажи рекламы нашего проекта.
💳 <b>Выплаты</b> 👉 @paymentsfootball`,{
    reply_markup: {
        keyboard: [
            [{ text: "🛒 Магазин" }],
            [{ text: "🏆Мои Команды" }]
        ]
    },
    resize_keyboard: true
});
    }
})