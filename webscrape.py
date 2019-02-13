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
    for i in range(2000, 2019):
        url_list.append(url + str(i) + '.html')
    return url_list

season_urls = url_gen(url)
print(season_urls)

def scrape(season_urls):
    season = 2000
    for i in season_urls:
        fields= {}
        
        webpage = requests.get(season_urls[i])
        soup = BeautifulSoup(webpage.text, 'lxml')
        fields['misc_tables'] = str(webpage.find_all('div', id="all_misc_stats")[0])
        fields['team_stats_table'] = str(webpage.find_all('div', id='all_team-stats-base')[0])
        fields['shooting_table'] = str(webpage.find_all('div', id='all_team_shooting')[0])
        fields['season'] = season
        season +=1
        with open('scrape_records.log', 'a+') as log:
             log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
             log.write('Webpage: {},'.format(webpage))
        
        mongo_connect.insert_one(fields)
        time.sleep(60)