import cfscrape
import requests
from bs4 import BeautifulSoup


def get_webpage(company_name):
    site = f'https://finance.naver.com/sise/sise_market_sum.naver?&page='

    a = {}
    for i in range(1, 36):
        scraper = cfscrape.create_scraper()
        res = scraper.get(site+str(i))
        soup = BeautifulSoup(res.content, "html.parser")
        stock_info = get_company_info(soup)
        if company_name == '목록':
            return stock_info

        stock_price = find_stock_price(stock_info, company_name)

        if stock_price is not None:
            a['회사명'] = company_name
            a['현재가'] = stock_price

    if a == {}:
        warning_msg = 'w'
        return warning_msg
    else:
        return a


def get_company_info(soup):
    # import chardet
    section = soup.find('tbody')
    items = section.find_all('tr', onmouseover="mouseOver(this)")
    stock_info = {}
    for stock_data in items:
        basic_info = stock_data.get_text()
        sinfo = basic_info.split("\n")
        jinfo = '\t'.join(sinfo).split('\t')
        stock_info[jinfo[2]] = jinfo[3]
    return stock_info


def find_stock_price(stock_info, company_name):
    if company_name in list(stock_info.keys()):
        return stock_info[company_name]


if __name__ == '__main__':
#    import argparse
#    parser = argparse.ArgumentParser()
#    parser.add_argument('-c', '--company', required=True, help='Enter Company name')
#    args = parser.parse_args()
    get_webpage("대한항공")
