import cfscrape
from bs4 import BeautifulSoup
from urllib import parse


def get_webpage(weather):
    weather = parse.quote(weather)
    site = f'https://search.naver.com/search.naver?query={weather}'
    scraper = cfscrape.create_scraper()
    webpage = scraper.get(site)
    soup = BeautifulSoup(webpage.content, "html.parser")
    weather_info = find_weather_info(soup)
    return weather_info


def find_weather_info(soup):
    container = {}
    location = ""
    weather = ""
    temperature = []
    highest = ""
    lowest = ""
    fine_dust = ""
    ultra_fine_dust = ""

    for i in soup.select('h2[class=title]'):
        location = i.text
    container['위치'] = location

    for i in soup.select('span.weather.before_slash'):
        weather = i.text
    container['오늘 날씨'] = weather

    for i in soup.select('div[class=temperature_text]'):
        temp = i.text[6:-1]
        temperature.append(temp)
    print(temperature)
    container['현재 기온'] = temperature[0]

    for i in soup.select('span[class=highest]')[0]:
        highest = i.text
    container['최고 기온'] = highest

    for i in soup.select('span[class=lowest]')[0]:
        lowest = i.text
    container['최저 기온'] = lowest

    for i in soup.select('span.txt')[0]:
        fine_dust = i.text
    container['미세먼지'] = fine_dust

    for i in soup.select('span.txt')[1]:
        ultra_fine_dust = i.text
    container['초미세먼지'] = ultra_fine_dust

    return container

