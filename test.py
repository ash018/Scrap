# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import urllib.request
import requests
from pathlib import Path

from bs4 import BeautifulSoup
import json

''''
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
'''

import pandas as pd
import datetime
#import pandas.dataframe as df

df = pd.read_csv('chaldal_feature.csv')
#print( df.tail(1).index.item()+1)
#print(df.tail(1))
value = df.tail(1).iloc[0]['Date']
dt=datetime.datetime.today().strftime('%Y-%m-%d')
print(value)
print(dt)
if(value==dt):
    print('Equal')
else:
    print('not equal')
#print(df['ProductName'].size)
#print(df['ProductName'].unique().size)


'''
if(Path('meenabazar_feature.csv').is_file()):
    df = pd.read_csv('meenabazar_feature.csv')
    id = df.tail(1).index.item()+1
    print('found')
    
    
else:
    print('not found')
    print(id)
    id = 1
'''