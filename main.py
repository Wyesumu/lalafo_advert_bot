from typing import NoReturn

import telebot
from telebot.types import Message
from tinydb import Query, TinyDB

from api import get_ads
from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)
db = TinyDB("db.json")


class User(Query):
    id: int
    config: None | dict


ad_message = """
Title: {title}
Price: {price}
Description: {description}
Phone: {phone}
Url: {url}
"""


def notify_about_ads(user_id: int, ads: list):
    for ad in ads:
        bot.send_message(user_id, ad_message.format(**ad))


@bot.message_handler(commands=["start"])
def start(message: Message) -> NoReturn:
    user = User()
    if not db.search(user.id == message.from_user.id):
        db.insert({"id": message.from_user.id, "config": None})
        bot.send_message(message.from_user.id, "User was successfully added")
    else:
        bot.send_message(message.from_user.id, "Welcome back")


@bot.message_handler(commands=["check"])
def check(message: Message) -> NoReturn:
    ads = get_ads()
    if not ads:
        return bot.send_message(message.from_user.id, "No new ads")
    notify_about_ads(message.from_user.id, ads)


if __name__ == "__main__":
    bot.polling(none_stop=True, interval=0)
