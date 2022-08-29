from unittest import result
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw=raspberry+pi+4b&_sacat=0&LH_PrefLoc=1&LH_Auction=1&rt=nc&LH_Sold=1&LH_Complete=1'


def get_data(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(soup):
    results = soup.find_all('div', class_='s-item__info clearfix')
    print(len(results))
    return

soup = get_data(url)
parse(soup)
