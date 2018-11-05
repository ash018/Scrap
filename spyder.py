# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 12:49:01 2018

@author: smakash
"""

import json
import scrapy
import urllib.request 
 
class SpidyQuotesSpider(scrapy.Spider):
    name = 'spidyquotes'
    quotes_base_url = 'http://spidyquotes.herokuapp.com/api/quotes?page=%s'
    start_urls = [quotes_base_url % 1]
    download_delay = 1.5
    
    def parse(self, response):
        data = json.loads(response.body)
        for item in data.get('quotes', []):
            yield {
                'text': item.get('text'),
                'author': item.get('author', {}).get('name'),
                'tags': item.get('tags'),
            }
        if data['has_next']:
            next_page = data['page'] + 1
            yield scrapy.Request(self.quotes_base_url % next_page)
            
if __name__ == '__main__':
    scraper = SpidyQuotesSpider()
    