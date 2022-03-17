import telegram
import lol
import weather
import stock
import listing

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters
#import requests
#import cfscrape
#from urllib import parse
#from bs4 import BeautifulSoup

# telegram Bot API
api_key = '5066924599:AAFO6EyWswaUiWKGSAoIOaaKwdCEiMt1gaU'
bot = telegram.Bot(token=api_key)
info_message = '''- 리그오브레전드 랭크 확인 : /1 (롤 아이디 입력)'  
- 현재 위치 날씨 정보 확인 /2 '''

updater = Updater(token=api_key, use_context=True)
context = bot.getUpdates()
#command = context[-1].message.text
chat_id = context[-1].message.chat_id
print(chat_id)
dispatcher = updater.dispatcher
updater.start_polling()


def handler(update, context):
    command = update.message.text
    print(command)
    chat_id_list = []

    if chat_id not in chat_id_list:
        chat_id_list.append(chat_id)

    if command[1] == "1":
        lol_web = lol.get_webpage(command[2:])
        lol_web_li = [str(f'{k} : {v}') for k, v in lol_web.items()]
        league_of_legends = '\n'.join(lol_web_li)

        # set rank
        bot.send_message(chat_id=chat_id, text=league_of_legends)

    if command[1] == "2":
        weather_web = weather.get_webpage("서울날씨")
        weather_web_li = [str(f'{k} : {v}') for k, v in weather_web.items()]
        weather_data = '\n'.join(weather_web_li)

        # set weather
        bot.send_message(chat_id=chat_id, text=weather_data)

    if command[1] == "3":
        stock_web = stock.get_webpage(command[3:])

        if command[3:] == '목록':
            stock_web_li = [str(f'{k}') for k in stock_web.keys()]
            stock_data = '\n'.join(stock_web_li)
        elif stock_web == 'w':
            warnings_msg = '목록에 해당 회사명이 없습니다.'
            stock_data = warnings_msg
        else:
            stock_web_li = [str(f'{k} : {v}') for k, v in stock_web.items()]
            stock_data = '\n'.join(stock_web_li)

        # set stock_data
        bot.send_message(chat_id=chat_id, text=stock_data)

    if command[1] == "4":
        listing_info = listing.get_webpage()
        listing_data = '\n'.join(listing_info)

        bot.send_message(chat_id=chat_id, text=listing_data)

echo_handler = MessageHandler(Filters.text, handler)
dispatcher.add_handler(echo_handler)

#if __name__ == '__main__':