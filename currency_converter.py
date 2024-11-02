import requests


def currency_converter(base_currency, target_currency, amount):
    try:
        response = requests.get(
            f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
        )
        response.raise_for_status()
        exchange_rates = response.json()["rates"]
        target_rate = exchange_rates.get(target_currency)
        if target_rate:
            converted_amount = amount * target_rate
            return f"Сконвертированная сумма: {converted_amount:.2f} {target_currency}"
        else:
            return f"Неверный код целевой валюты: {target_currency}. Выберите заново команду."
    except requests.RequestException as error:
        return (
            f"Ошибка при получении данных о валюте: {error}. Выберите заново команду."
        )
