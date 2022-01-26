import cfscrape
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

    for i in soup.select('span[class=Name]'):
        player = i.text
    container['Player'] = player

    for i in soup.select('div[class=TierRank]'):
        solo_ranking = i.text
    container['SoloRanking'] = solo_ranking

    if not container['SoloRanking']:
        container['SoloRanking'] = "unrank"
        return container

    for i in soup.select('span[class=wins]'):
        wins = i.text
    container['승'] = wins

    for i in soup.select('span[class=losses]'):
        losses = i.text
    container['패'] = losses

    for i in soup.select('span[class=winratio]'):
        win_ratio = i.text
    container['승률'] = win_ratio

    return container
