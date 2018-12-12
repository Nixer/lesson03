from utils import get_user_emo, get_keyboard
import datetime
import ephem
from glob import glob
from random import choice
import logging


def greet_user(bot, update, user_data):
    emo = get_user_emo(user_data)
    text = f'Привет {emo}'
    update.message.reply_text(text, reply_markup=get_keyboard())


def talk_to_me(bot, update, user_data):
    emo = get_user_emo(user_data)
    user_text = f"Привет {update.message.chat.first_name}! {emo} Ты написал: {update.message.text}"
    logging.info(f"User: {update.message.chat.username}, "
                 f"Chat id: {update.message.chat.id}, "
                 f"Message: {update.message.text}")
    update.message.reply_text(user_text, reply_markup=get_keyboard())


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


def cities(bot, update, args, user_data):
    city = " ".join(args)
    if len(args) == 0:
        update.message.reply_text('Введите город')
    elif (args[0][0] not in data) or (city not in data[args[0][0]]):
        update.message.reply_text('Введите любой город России')
    else:
        if " ".join(args) not in data_proc[args[0][0]]:
            update.message.reply_text('Такой город уже был назван')
        else:
            update.message.reply_text(data_proc[city[-1].capitalize()][0])
            del(data_proc[city[-1].capitalize()][0])


def send_cat_picture(bot, update, user_data):
    cat_list = glob('images/cat*.jp*g')
    cat_pic = choice(cat_list)
    bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))


def change_avatar(bot, update, user_data):
    if 'emo' in user_data:
        del user_data['emo']
    emo = get_user_emo(user_data)
    update.message.reply_text(f"New avatar: {emo}", reply_markup=get_keyboard())


def get_contact(bot, update, user_data):
    print(update.message.contact)
    update.message.reply_text(f"Done {get_user_emo(user_data)}", reply_markup=get_keyboard())


def get_location(bot, update, user_data):
    print(update.message.location)
    update.message.reply_text(f"Done {get_user_emo(user_data)}", reply_markup=get_keyboard())

