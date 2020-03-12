from telegram.ext import Updater, InlineQueryHandler, CommandHandler
from telegram.ext.dispatcher import run_async
import requests
import re

@run_async
def start(update, context):
    msg = '/diselo para hacerselo saber y /flundea para el terror de Rod'
    chat_id = update.message.chat_id
    context.bot.sendMessage(chat_id=chat_id, text=msg)

@run_async
def diselo(update, context):
    url = 'https://media.giphy.com/media/cOuHHFJVzmf8YAZeiL/giphy.gif'
    chat_id = update.message.chat_id
    context.bot.sendAnimation(chat_id=chat_id, animation=url)

@run_async
def flundea(update, context):
    url = 'https://media.giphy.com/media/cOuHHFJVzmf8YAZeiL/giphy.gif'
    chat_id = update.message.chat_id
    for x in range(100):
        context.bot.sendAnimation(chat_id=chat_id, animation=url)

def main():
    f = open("token.txt", "r")
    token = f.readline()
    f.close()
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('diselo',diselo))
    dp.add_handler(CommandHandler('flundea',flundea))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
