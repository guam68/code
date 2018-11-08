# -*- coding: utf-8 -*-
import scrapy
import json


class RottenSpiderSpider(scrapy.Spider):
    name = 'rotten'
    allowed_domains = ['rottentomatoes.com']
    rotten_base_url = ('https://rottentomatoes.com/api/private/v2.0/browse?maxTomato=100&maxPopcorn=100&services=netflix_iw&certified=false&sortBy=release&type=dvd-streaming-all&page=')
    start_urls = [rotten_base_url]
    download_delay = 2

# Calculates total number of json pages and calls parse_page for each page

    def parse(self, response):
        data = json.loads(response.body)
        pages = -(-(data.get('counts', {}).get('total')) // data.get('counts', {}).get('count'))

        for page in range(pages):
            yield scrapy.Request(self.rotten_base_url + str(page), self.parse_page)

# Loads page and appends string 'movies' with title, critic score, and audience score for each result.
# Appends file 'movies.txt' with the contents of string 'movies' 
  
    def parse_page(self, response):
        data = json.loads(response.body)
        movies = ''

        for item in data.get('results', []):
            critic = str(item.get('tomatoScore'))
            audience = str(item.get('popcornScore'))

            if critic == '-1':
                critic = 'n/a'
            if audience == '-1':
                audience = 'n/a'

            movies += item.get('title') + ':\t ' + critic + ', ' + audience + '\n'

        filename = 'movies.txt'
        with open(filename, 'a') as f:
            f.write(movies)
        print('Data added!')
