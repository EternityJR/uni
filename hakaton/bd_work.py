import models
import settings
from keyboards import *
from telegram import ReplyKeyboardRemove
from emoji import emojize

from keyboard import start_keyboard


def bd_edit_anketa(update, contex):  # изменение анкеты
    user_message = update.message.text
    return


def bd_search(update, contex):  # поиск друга
    user_message = update.message.text
    person = models.find_person(update.message.from_user.id)
    smile = emojize(settings.EMOJI[4], use_aliases = True)
    if person:
        update.message.reply_text(f"Мы нашли тебе друга!{smile} Это {person.name} и вот ссылка на него {person.link}",
                                  reply_markup = start_keyboard(update))
    else:
        update.message.reply_text(f"К сожалению, мы пока не можем найти для тебя достойного напарника. Приходи позже "
                                  f"и мы попробуем ещё раз! ",
                                  reply_markup = start_keyboard(update))
    return