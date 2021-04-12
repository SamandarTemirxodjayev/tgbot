const token = '1680049120:AAH0IY83YSdLJguqUN4zfN46O5WN9Y2YjbA'
const TelegramBot = require('node-telegram-bot-api')
const bot = new TelegramBot(token, {polling: true})

bot.on('message', msg => {
    if(message.text=="/start"){
        bot.sendMessage(msg.chat.id,"hello world")
    }
})