import os
import telebot
from general_functions import get_target_currency
from general_functions import get_base_currency
from dotenv import load_dotenv

load_dotenv()
tg_token = os.getenv("TG_BOT_TOKEN")
bot = telebot.TeleBot(tg_token)


@bot.message_handler(commands=["eur"])
def currency_converter(message):
    base_currency = "EUR"
    chat_id = message.chat.id
    get_target_currency(message, bot, base_currency, chat_id)


@bot.message_handler(commands=["gbp"])
def currency_converter(message):
    base_currency = "GBP"
    chat_id = message.chat.id
    get_target_currency(message, bot, base_currency, chat_id)


@bot.message_handler(commands=["usd"])
def currency_converter(message):
    base_currency = "USD"
    chat_id = message.chat.id
    get_target_currency(message, bot, base_currency, chat_id)


@bot.message_handler(commands=["cny"])
def currency_converter(message):
    base_currency = "CNY"
    chat_id = message.chat.id
    get_target_currency(message, bot, base_currency, chat_id)


@bot.message_handler(commands=["rub"])
def currency_converter(message):
    base_currency = "RUB"
    chat_id = message.chat.id
    get_target_currency(message, bot, base_currency, chat_id)


@bot.message_handler(commands=["jpy"])
def currency_converter(message):
    base_currency = "JPY"
    chat_id = message.chat.id
    get_target_currency(message, bot, base_currency, chat_id)


@bot.message_handler(commands=["othercurrency"])
def currency_converter(message):
    chat_id = message.chat.id
    get_base_currency(message, bot, chat_id)


bot.polling()
