const token = '1680049120:AAH0IY83YSdLJguqUN4zfN46O5WN9Y2YjbA'
const TelegramBot = require('node-telegram-bot-api')
const bot = new TelegramBot(token, {polling: true})

bot.on('text', async (message) => {
    if (message.text == '/start') {
        message.send = (text, params) => bot.sendMessage(message.chat.id, text, params);
        return message.send('hello world',{});
    }
})