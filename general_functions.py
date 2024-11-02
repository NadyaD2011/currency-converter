from currency_converter import currency_converter


def get_base_currency(message, bot, chat_id):
    msg = bot.send_message(chat_id, "Введите код базовой валютs (например, RUB):")
    bot.register_next_step_handler(msg, get_other_target_currency, bot, chat_id)


def get_other_target_currency(message, bot, chat_id):
    base_currency = message.text.upper()
    msg = bot.send_message(chat_id, "Введите код целевой валюты (например, USD):")
    bot.register_next_step_handler(msg, get_amount, bot, base_currency, chat_id)


def get_target_currency(message, bot, base_currency, chat_id):
    msg = bot.send_message(chat_id, "Введите код целевой валюты (например, USD):")
    bot.register_next_step_handler(msg, get_amount, bot, base_currency, chat_id)


def get_amount(message, bot, base_currency, chat_id):
    target_currency = message.text.upper()
    msg = bot.send_message(chat_id, "Введите сумму базовой валюты: ")
    bot.register_next_step_handler(
        msg, currency_converter_handler, bot, base_currency, target_currency, chat_id
    )


def currency_converter_handler(message, bot, base_currency, target_currency, chat_id):
    try:
        amount = float(message.text)
        answer = currency_converter(base_currency, target_currency, amount)
        bot.send_message(chat_id, answer)
    except ValueError:
        bot.send_message(
            chat_id, "Неверная сумма. Пожалуйста, введите числовое значение."
        )
