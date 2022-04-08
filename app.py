import telebot
from config import keys, TOKEN
from extensions import ConvertionEx, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def helpme(message: telebot.types.Message):
    text = 'КОНВЕРТЕР ВАЛЮТЫ\n' \
           'Доступные валюты: /currencies\n' \
           'Пример ввода: рубль доллар 100\n' \
           'Пример вывода: 100 RUB = 1.26 USD'
    bot.reply_to(message, text)


@bot.message_handler(commands=['currencies'])
def currencies(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in keys.keys():
        text = '\n'.join((text, i,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3:
            raise ConvertionEx('Слишком много параметров ввода')
        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConvertionEx as e:
        bot.reply_to(message, f'User error:\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Cannot process:\n{e}')
    else:
        quote_ticker = keys[quote]
        base_ticker = keys[base]
        text = f'{amount} {quote_ticker} = {total_base} {base_ticker}'
        bot.send_message(message.chat.id, text)


bot.polling()
