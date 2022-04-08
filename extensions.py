import json
import requests
from config import keys


class ConvertionEx(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionEx("Указаны одинаковые валюты")
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionEx(f'Нет валюты {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionEx(f'Нет валюты {base}')
        try:
            float(amount)
        except ValueError:
            raise ConvertionEx('Problem with float number')
        r = requests.get(f'https://free.currconv.com/api/v7/convert?q={quote_ticker}_{base_ticker}&compact=ultra&apiKey=a6d20ef02fd3deb5774e')
        total_base = json.loads(r.content)
        total_base = list(total_base.values())
        amount = float(amount)
        total_base = total_base[0]
        return total_base*amount
