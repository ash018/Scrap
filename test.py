# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
import requests

from bs4 import BeautifulSoup
import json

# new url      
url = 'http://www.meenaclick.com/product-details/93'

# read all data
#page = urllib.request.urlopen(url).read()
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())
links = soup.find_all('li',class_='dropdown-tree ng-scope')
for link in links:
    #x = link.select('a')
    #print(x)
    print(link.getText())
#print(page.content)
# convert json text to python dictionary
#data = json.loads(page)

#print(data['principal_activities'])