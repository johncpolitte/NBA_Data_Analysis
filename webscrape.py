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
        i = {}
        webpage = requests.get(season_urls[i])
        i['misc_tables'] = str(webpage.find_all('div', id="all_misc_stats")[0])
        i['team_stats_table'] = str(webpage.find_all('div', id='all_team-stats-base')[0])
        i['shooting_table'] = str(webpage.find_all('div', id='all_team_shooting')[0])
        with open('scrape_records.log', 'a+') as log:
            log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
            log.write('Webpage: {},'.format(webpage))
        soup = BeautifulSoup(webpage.text, 'lxml')
        mongo_connect.insert_one(i)
        time.sleep(60)