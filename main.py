import telebot
import os
from telebot import types
from dotenv import load_dotenv
import requests
import random


load_dotenv()

bot = telebot.TeleBot(os.getenv("Telegram_Token"), parse_mode=None)
print("Bot Loaded and started")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton("/help")
    itembtn2 = types.KeyboardButton("curse")
    itembtn3 = types.KeyboardButton("humor")
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)


@bot.message_handler(commands=["help"])
def help(m):
    cid = m.chat.id
    bot.send_message(
        cid,
        "*Bot Help Page*\n\n/setup - Start setup the Bot in this group",
        parse_mode="Markdown",
    )


@bot.message_handler(func=lambda message: "humor" in message.text.lower())
def echo_all(message):
    r = requests.get(
        "http://xkcd.com/" + str(int(random.random() * 2465)) + "/info.0.json"
    )
    bot.reply_to(message, r.json()["img"])


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    ran = random.random()
    if ran > 0.5:
        r = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
        bot.reply_to(message, r.json()["insult"])
    else:
        r = requests.get(
            "https://yomomma-api.herokuapp.com/jokes/" + str(int(random.random() * 980))
        )
        bot.reply_to(message, r.json()["joke"])


bot.polling()
