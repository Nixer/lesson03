from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
import ephem
import datetime
import json

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )


def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = f"Привет {update.message.chat.first_name}! Ты написал: {update.message.text}"
    logging.info(f"User: {update.message.chat.username}, "
                 f"Chat id: {update.message.chat.id}, "
                 f"Message: {update.message.text}")
    update.message.reply_text(user_text)


def const_planet(bot, update, args):
    now = datetime.datetime.now()
    planets = {'Pluto': ephem.Pluto(),
               'Mercury': ephem.Mercury(),
               'Venus': ephem.Venus(),
               'Mars': ephem.Mars(),
               'Jupiter': ephem.Jupiter(),
               'Saturn': ephem.Saturn(),
               'Uranus': ephem.Uranus(),
               'Neptune': ephem.Neptune()
               }
    if len(args) > 0:
        input_planet = args[0].strip()
        if input_planet in planets:
            planet = planets[input_planet]
            planet.compute(f'{now.year}/{now.month}/{now.day}')
            user_text = f"Планета {input_planet} сейчас в созвездии {ephem.constellation(planet)[1]}"
            update.message.reply_text(user_text)
        else:
            update.message.reply_text('Введите правильное название планеты!')
    else:
        update.message.reply_text('Введите название планеты!')


def word_count(bot, update, args):
    if len(args) == 0:
        update.message.reply_text('В введенной фразе: 0 слов')
    else:
        update.message.reply_text(f'В введенной фразе: {len(args)} слова')


def next_full_moon(bot, update, args):
    try:
        if len(args) == 0:
            update.message.reply_text('Введите дату')
        elif len(args) > 1:
            update.message.reply_text('Дата введена не верно')
        else:
            update.message.reply_text(f'Ближайшее полнолуние: {ephem.next_full_moon(args[0])}')
    except ValueError:
        update.message.reply_text('Введите дату в правильном формате')


def cities(bot, update, args):
    with open('cities.json') as f:
        data = json.load(f)
    print(data)


def main():
    mybot = Updater(settings.API_KEY)

    logging.info("Bot starting")
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", const_planet, pass_args=True))
    dp.add_handler(CommandHandler("wordcount", word_count, pass_args=True))
    dp.add_handler(CommandHandler("next_full_moon", next_full_moon, pass_args=True))
    dp.add_handler(CommandHandler("cities", cities, pass_args=True))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


main()
