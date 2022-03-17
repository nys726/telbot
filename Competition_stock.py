import time

import pandas as pd
import cfscrape
import requests
import time
from bs4 import BeautifulSoup


def get_webpage():
    site = f'http://www.38.co.kr/html/fund/index.htm?o=k&page=1'
    scraper = cfscrape.create_scraper()
    webpage = scraper.get(site)
    soup = BeautifulSoup(webpage.content, "html.parser")
    listing_data = find_listing_info(soup)
    return listing_data


def data_convert(dataframe):
    container = []
    tm = time.localtime()
    df_li = dataframe.values.tolist()
    today = f"{tm.tm_mon}.{tm.tm_mday}"
#    print(today)
    for i in df_li:
#        date = i[1].split('~')[0].split('.')
#        print(date)
#
#
        k = f"회사명: {i[0]}\n공모주 일정: {i[1]}\n확정공모가: {i[2]}\n청약경쟁률: {i[3]}\n주간사: {i[4]}\r\n"
        container.append(k)
    return container


def find_listing_info(soup):
    company_list = []
    listing_data = []
    fixed_price = []
    competition = []
    lead_company = []

    data = soup.find('table', {'summary': '공모주 청약일정'})
    data = data.find_all('tr')[2:]

    for row in range(0, len(data)):
        data_list = data[row].text.replace('\xa0', '').replace(' ', '').split('\n')[1:-2]
        if data_list[4] == '':
            data_list[4] = '확인 중'

        company_list.append(data_list[0].replace('(유가)', ''))
        listing_data.append(data_list[1])
        fixed_price.append(data_list[2].replace('-', '산정중'))
        competition.append(data_list[4])
        lead_company.append(data_list[5])

    listing_list = pd.DataFrame({'회사명': company_list,
                                 '공모주 일정': listing_data,
                                 '확정 공모가': fixed_price,
                                 '청약 경쟁률': competition,
                                 '주간사': lead_company})

    convert_listing = data_convert(listing_list)
    return convert_listing


if __name__ == '__main__':
#    import argparse
#    parser = argparse.ArgumentParser()
#    parser.add_argument('-c', '--company', required=True, help='Enter Company name')
#    args = parser.parse_args()
    get_webpage()