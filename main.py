import os

from slaq.bot import bot

if __name__ == '__main__':
    bot.start(port=int(os.environ.get("PORT", 3000)))
