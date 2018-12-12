from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from handlers import *

import settings
import json
import logging
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(f'{__location__}/cities.json') as f:
    data = json.load(f)
data_proc = data.copy()


def main():
    mybot = Updater(settings.API_KEY)

    logging.info("Bot starting")

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user, pass_user_data=True))
    dp.add_handler(CommandHandler("planet", const_planet, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", word_count, pass_args=True))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon, pass_args=True))
    dp.add_handler(CommandHandler("cat", send_cat_picture, pass_user_data=True))
    dp.add_handler(CommandHandler("cities", cities, pass_args=True, pass_user_data=True))
    dp.add_handler(RegexHandler("^(Get cat)$", send_cat_picture, pass_user_data=True))
    dp.add_handler(RegexHandler("^(Change avatar)$", change_avatar, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.contact, get_contact, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.location, get_location, pass_user_data=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me, pass_user_data=True))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
