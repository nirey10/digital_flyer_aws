import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_ynet_articles():

    articlelist = []
    url = 'https://www.ynet.co.il/news/category/184'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='lxml')
    articles = soup.find_all('div', class_ = 'title')

    for item in articles:
        article_text = item.get_text()
        articlelist.append(article_text)

    return articlelist


def get_globs_articles():
    articlelist = []
    url = 'https://www.globes.co.il/portal/'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='lxml')
    articles = soup.find_all('a', class_ = 'text')

    for item in articles:
        article_text = item.get_text()
        articlelist.append(article_text)

    return articlelist


def get_one_articles():
    articlelist = []
    url = 'https://www.one.co.il/'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, features='lxml')
    articles = soup.find_all('h2')

    for item in articles:
        article_text = item.get_text()
        articlelist.append(article_text)

    return articlelist
