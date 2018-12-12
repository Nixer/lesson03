from telegram import ReplyKeyboardMarkup, KeyboardButton
from emoji import emojize
import settings
from random import choice


def get_user_emo(user_data):
    if 'emo' in user_data:
        return user_data['emo']
    else:
        user_data['emo'] = emojize(choice(settings.USER_EMOJI), use_aliases=True)
        return user_data['emo']


def get_keyboard():
    contact_button = KeyboardButton('Contacts', request_contact=True)
    location_button = KeyboardButton('Geolocation', request_location=True)
    my_keyboard = ReplyKeyboardMarkup([
                                        ["Get cat", "Change avatar"],
                                        [contact_button, location_button],
                                     ], resize_keyboard=True)
    return my_keyboard
