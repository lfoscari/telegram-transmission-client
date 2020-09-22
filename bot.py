from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from os import system
from datetime import datetime

from instanceElements import TOKEN
try: from instanceElements import USERS
except: USERS = None

def log(message, username):
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print("[{}] {} from @{}".format(now, message, username))

# Authentication

def authentication(func):
    def inner(*args, **kwargs):
        if USERS is None or args[0].message.from_user.id in USERS:
            return func(*args, **kwargs)
        log("unauthorized user", args[0].message.from_user.username)
        return error(*args, **kwargs)
    return inner

def error(update, context):
    update.message.reply_text("Get lost")

# Torrent manipulation

def add_torrent(path):
    if not 0:
    # if not os.system("transmission-remote -a {}".format(url))
        return "I got you bro, just wait for it"
    return "oh dear, I'm terribly sorry, but something went wrong"

@authentication
def text_to_path(update, context):
    torrent_path = update.message.text
    log("new torrent", update.message.from_user.username)
    update.message.reply_text(add_torrent(torrent_path))

@authentication
def file_to_path(update, context):
    torrent_path = update.message.document.get_file().file_path
    log("new torrent", update.message.from_user.username)
    update.message.reply_text(add_torrent(torrent_path))

@authentication
def list_torrents(update, context):
    log("/list", update.message.from_user.username)
    # os.system("transmission-remote -l")
    update.message.reply_text("I gotta work on that")

if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("list", list_torrents))
    dp.add_handler(MessageHandler(Filters.text, text_to_path))
    dp.add_handler(MessageHandler(Filters.document, file_to_path))

    print("Now listening...")

    updater.start_polling()
    updater.idle()
