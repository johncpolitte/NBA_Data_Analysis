from pymongo import MongoClient
import time
import random

#Import beautiful soup
import requests
import re
from bs4 import BeautifulSoup
import argparse

#from fake_useragent import UserAgent

client = MongoClient()
database = client['NBA_tables']   # Database name
mongo_connect = database['season_page'] 

url = 'https://www.basketball-reference.com/leagues/NBA_'

def url_gen(url):
    url_list = []
    for i in range(1979, 2019):
        url_list.append(url + str(i) + '.html')
    return url_list

season_urls = url_gen(url)

def scrape(season_urls):
    for i in season_urls:
        