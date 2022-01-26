import telegram
import lol
import weather
import requests
import cfscrape
from urllib import parse
from bs4 import BeautifulSoup
from telegram.ext import Updater, CommandHandler


def run(jarvis):
    updates = jarvis.getUpdates()
    chat_id_list = []
    command = updates[-1].message.text
    chat_id = updates[-1].message.chat_id

    if chat_id not in chat_id_list:
        chat_id_list.append(chat_id)

    if command[1] == "1":
        lol_web = lol.get_webpage(command[2:])
        lol_web_li = [str(f'{k} : {v}') for k, v in lol_web.items()]
        league_of_legends = '\n'.join(lol_web_li)

        # set rank
        jarvis.send_message(chat_id=chat_id, text=league_of_legends)

    if command[1] == "2":
        weather_web = weather.get_webpage("날씨")
        weather_web_li = [str(f'{k} : {v}') for k, v in weather_web.items()]
        weather_data = '\n'.join(weather_web_li)

        # set weather
        jarvis.send_message(chat_id=chat_id, text=weather_data)



if __name__ == '__main__':
    # telegram Bot API
    api_key = '5066924599:AAFO6EyWswaUiWKGSAoIOaaKwdCEiMt1gaU'
    bot = telegram.Bot(token=api_key)
    run(bot)
