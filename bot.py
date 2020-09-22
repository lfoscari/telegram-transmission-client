from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from instanceElements import TOKEN, USERS
from os import system

# Authentication

def auth(func):
    def inner(*args, **kwargs):
        if USERS == [] or args[0].message.from_user.id in USERS:
            return func(*args, **kwargs)
        return error(*args, **kwargs)
    return inner

def error(update, context):
    update.message.reply_text("Get lost")


def load_torrent(path):
    if not 0:
    # if not os.system("transmission-remote -a {}".format(url))
        return "I got you bro, just wait for it"
    return "oh dear, I'm terribly sorry, but something went wrong"

@auth
def load_torrent_from_path(update, context):
    torrent_path = update.message.text
    update.message.reply_text(load_torrent(torrent_path))

@auth
def load_torrent_from_file(update, context):
    torrent_path = update.message.document.get_file().file_path
    update.message.reply_text(load_torrent(torrent_path))

@auth
def list_torrents(update, context):
    # os.system("transmission-remote -l")
    update.message.reply_text("I gotta work on that")

if __name__ == '__main__':
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, load_torrent_from_path))
    dp.add_handler(MessageHandler(Filters.document, load_torrent_from_file))
    dp.add_handler(CommandHandler("list", list_torrents))

    updater.start_polling()
    updater.idle()
