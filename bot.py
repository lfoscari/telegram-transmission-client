from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from os import system
from datetime import datetime

from instanceElements import TOKEN
try: from instanceElements import USERS
except: USERS = None

def log(message, username):
    """Log to stdin"""
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    print("[{}] {} from @{}".format(now, message, username))

# Authentication

def auth(func):
    """Authenticate user from USERS"""
    def inner(*args, **kwargs):
        if USERS is None or args[0].message.from_user.id in USERS:
            return func(*args, **kwargs)
        log("unauthorized user", args[0].message.from_user.username)
        return error(*args, **kwargs)
    return inner

def error(update, context):
    update.message.reply_text("Get lost")

# Torrent manipulation

def load_torrent(path):
    """Add torrent to queue"""
    if not 0:
    # if not os.system("transmission-remote -a {}".format(url))
        return "I got you bro, just wait for it"
    return "oh dear, I'm terribly sorry, but something went wrong"

@auth
def load_torrent_from_path(update, context):
    """Extract uri or magnet from user's message"""
    torrent_path = update.message.text
    log("new torrent", update.message.from_user.username)
    update.message.reply_text(load_torrent(torrent_path))

@auth
def load_torrent_from_file(update, context):
    """Extract torrent file path from user's message"""
    torrent_path = update.message.document.get_file().file_path
    log("new torrent", update.message.from_user.username)
    update.message.reply_text(load_torrent(torrent_path))

@auth
def list_torrents(update, context):
    """Get all torrents"""
    log("/list", update.message.from_user.username)
    # os.system("transmission-remote -l")
    update.message.reply_text("I gotta work on that")

if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("list", list_torrents))
    dp.add_handler(MessageHandler(Filters.text, load_torrent_from_path))
    dp.add_handler(MessageHandler(Filters.document, load_torrent_from_file))

    print("Now listening...")

    updater.start_polling()
    updater.idle()
