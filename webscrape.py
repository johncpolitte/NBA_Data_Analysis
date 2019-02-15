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
mongo_connect = database['seasons'] 

def url_gen(url):
        '''
        This function takes in the root web address for basketball reference 
        and generates a list of urls from 2001-2018
        input: string
        output: list

        '''
        url_list = []
        for i in range(2001, 2019):
            url_list.append(url + str(i) + '.html')
        return url_list


def scrape(season_urls):
        '''
        This function takes in a list of urls and scrapes the Misc table,
        team stats table, and shooting table from basketball reference.
        It then pipelines each seasons tables as a Beautiful Soup object in
        dictionary. The result is a list of the dictionaries for each season
        
        input: list of urls that you want to scrape
        output: List of dictionaries with Beautiful soup objects for each season

        '''
    season = 2001
    for i in season_urls:
        fields= {}
        webpage = requests.get(i)
        soup = BeautifulSoup(webpage.text, 'lxml')
        fields['misc_tables'] = str(soup.find_all('div', id="all_misc_stats")[0])
        fields['team_stats_table'] = str(soup.find_all('div', id='all_team-stats-base')[0])
        fields['shooting_table'] = str(soup.find_all('div', id='all_team_shooting')[0])

        fields['season'] = season
        season +=1
        with open('scrape_records.log', 'a+') as log:
             log.write(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()))
             log.write('Webpage: {},'.format(i))
        
        mongo_connect.insert_one(fields)
        time.sleep(30)


if __name__ =="__main__":
    url = 'https://www.basketball-reference.com/leagues/NBA_'
    
    urls = url_gen(url)
    scrape(urls)