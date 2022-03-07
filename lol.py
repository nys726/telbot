import cfscrape
import re
from urllib import parse
from bs4 import BeautifulSoup


def get_webpage(lol_id):
    lol_id = parse.quote(lol_id)
    site = f'https://www.op.gg/summoner/userName={lol_id}'
    scraper = cfscrape.create_scraper()
    webpage = scraper.get(site)
    soup = BeautifulSoup(webpage.content, "html.parser")
    rank_info = find_lol_info(soup)
    return rank_info


def find_lol_info(soup):
    container = {}
    player = ""
    solo_ranking = []
    wins = ""
    losses = []
    win_ratio = []

    for i in soup.select('span[class=name]'):
        player = i.text
    container['Player'] = player

    for i in soup.select('div[class=tier-rank]'):
        solo_ranking = i.text
    container['SoloRanking'] = solo_ranking

    if not container['SoloRanking']:
        container['SoloRanking'] = "unrank"
        return container

    for i in soup.select('span[class=win-lose]'):
        record = i.text
        sp_record = record.split()
        only_num = [re.sub(r'[^0-9]', '', i) for i in sp_record]
        wins = only_num[0]
        losses = only_num[1]
        win_ratio = only_num[3]
    container['승'] = wins
    container['패'] = losses
    container['승률'] = win_ratio

#    for i in soup.select('span[class=losses]'):
#        losses = i.text
#    container['패'] = losses
#
#    for i in soup.select('span[class=winratio]'):
#        win_ratio = i.text
#    container['승률'] = win_ratio

    return container

if __name__ == '__main__':
    get_webpage('느금마카롱')
