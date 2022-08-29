from unittest import result
import requests
from bs4 import BeautifulSoup
import pandas as pd


productToSearch = input("Enter a product to find prices for: ")


def get_data(product):
    url = f'https://www.ebay.co.uk/sch/i.html?_from=R40&_nkw={product}&_sacat=0&LH_PrefLoc=1&LH_Auction=1&rt=nc&LH_Sold=1&LH_Complete=1'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(soup):
    productsList = []
    products = soup.find_all('div', class_='s-item__info clearfix')

    for i in range(1, len(products)):
        product = {
            'title': products[i].find('h3', class_='s-item__title s-item__title--has-tags').text,
            'soldPrice': float(products[i].find('span', class_='s-item__price').text.replace('£', '').replace(',','')),
            'soldDate' : products[i].find('div', class_='s-item__title--tagblock').find('span', class_='POSITIVE').text.replace('Sold  ', ''),
            'bids': products[i].find('span', class_='s-item__bids s-item__bidCount').text,
            'link': products[i].find('a', class_='s-item__link')['href']
        }
        productsList.append(product)
    return productsList


def output(products, productToSearch):
    productsdf = pd.DataFrame(products)
    productsdf.to_csv(productToSearch + 'productsInfo.csv', index=False)
    print(productsdf)

soup = get_data(productToSearch)
output(parse(soup), productToSearch)
