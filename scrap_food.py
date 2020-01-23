# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 23:35:35 2018
@author: Ash
"""

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import csv
from time import gmtime, strftime
import pandas as pd
from pathlib import Path
import re
import datetime
from seleniumwire import webdriver
#df = pd.read_csv('chaldal_feature.csv')

option = webdriver.ChromeOptions()
#option.add_argument(" — incognito")

url = "https://www.ubereats.com/bn-BD/feed/?pl=JTdCJTIyYWRkcmVzcyUyMiUzQSUyMiVFMCVBNiVBNCVFMCVBNyU4NyVFMCVBNiU5QyVFMCVBNiU5NyVFMCVBNiVCRSVFMCVBNiU4MSVFMCVBNiU5MyUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUptZUhqYUZfSFZUY1JhTFUwSnFyRWtSQSUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EyMy43NjExNDkyJTJDJTIybG9uZ2l0dWRlJTIyJTNBOTAuMzg5NDg4JTdE"
if(Path('/chaldal_feature.csv').is_file()):
    df = pd.read_csv('chaldal_feature.csv')
    id = df.tail(1).index.item()+1
else:
    id = 1
    

browser = webdriver.Chrome(executable_path=r"F:\software\chromedriver", chrome_options=option)
browser.get(url)
browser.implicitly_wait(30)
soup = BeautifulSoup(browser.page_source, 'lxml')


#print(soup.prettify())



''''
for request in browser.requests:
    if request.response:
        #print(request.path)
        
        if('js' in request.path):
            f = open("demofile2.txt", "a")
            f.write("=======================")
            f.write(str(request.response.body))
            f.close()
            print(
                request.path,
                request.response.status_code,
                request.response.headers['Content-Type'],
                request.response.body
            )

'''

import csv


import time
while True:
    time.sleep(10) 
    titles_element = browser.find_elements_by_xpath("//article[@class='af']")
    #input = browser.find_element_by_xpath("//input[@name='userQuery']")
    #locationTxt = input.get_attribute('value')
    titles = [x.text for x in titles_element]
    with open('writeData.csv', mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Location', 'Detail'])
        for x in titles_element:
            print(x.text)
            writer.writerow(['Tejgaon', x.text])
    #print(locationTxt)
    #print(titles, '\n')
    #print(soup.prettify())
    #parentName = soup.find('div')
    #print(parentName)
    #offerItem = parentName.find_all("li",class_='offer-item')
    #productList = parentName.find_all("div",class_='b8')

    # for i in parentName:
    #     print(i.prettify())
    # Delay for 1 minute (60 seconds).


'''
parentName2 = soup.find('li',class_='offer-item')
children = parentName.find_all() # returns a list of all <a> children of li


ff = open("f.txt","wb")
print('dd')
substring_list=["Details","Add to Shopping Bag","Add to bag",">","৳"]
#sku_list
for child in children:
    fl = 0
    if  any(substring in (child.getText().strip()) for substring in substring_list):
        continue
    else:
        #print(child.getText().strip())
        if(',' in child.getText().strip()):
           print('comma')
           print(type(child.getText().strip()))
           print(re.sub('[\$,]', '', child.getText().strip()))
           ff.write(re.sub('[\$,]', '', child.getText().strip()).encode('utf-8'))
           ff.write(b'\n')
        else:
            ff.write(child.getText().strip().encode('utf-8'))
            ff.write(b'\n')
        
        
        
ff.close()
intCount = 0
#Reading File From Text File without new lineS            
names_list = [line for line in open("f.txt", "r").read().splitlines() if line]
#print(names_list)
product=[]
discount=[]
price=[]
for i in range(len(names_list)):
    
        #names_list[i].replace(',', '')
        #print(names_list[i])
  
    try:
       
       intConversion =  int(names_list[i])
       if(intConversion%1 == 0):
           try:
               intNextVal = int(names_list[i+1])
               if (intConversion%1 == 0 and intNextVal%1 == 0):
                   print('Discounted Product')
                   print(names_list[i-2])
                   product.append(names_list[i-2])
                   print('Discount Price')
                   print(names_list[i])
                   discount.append(names_list[i])
                   print('PPrice')
                   print(names_list[i+1])
                   price.append(names_list[i+1])
                   intCount+=1
                   i+=1
           
           except:
               if(len(names_list[i-2])>6):
                   print('Not Discounted Product')
                   print(names_list[i-2])
                   product.append(names_list[i-2])
                   print('Discount Price')
                   print('NULL')
                   discount.append('0')
                   print('PPrice')
                   print(names_list[i])
                   price.append(names_list[i])
               continue 
                   
             
       
           
       
    except:
        continue
   
    #print('Price Count'+str(intCount))
        
        
        


discountedpriceList = parentName.find_all("div",class_='discountedPrice')
priceList = parentName.find_all("div",class_='price')

with open('chaldal_feature.csv', mode='a',encoding="utf-8",newline='') as chaldal_feature:
    chaldal_feature = csv.writer(chaldal_feature, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    df = pd.read_csv('chaldal_feature.csv')
    id = df.tail(1).index.item()+1
    value = df.tail(1).iloc[0]['Date']
    dt=datetime.datetime.today().strftime('%Y-%m-%d')
    
    if (id <= 1):
        chaldal_feature.writerow(['ID','ProductName','DiscountPrice', 'PPrice','Date'])
    
     
    for p,d,pr in zip(product,discount,price):
        if(value!=dt):
            id+=1 
            chaldal_feature.writerow([ str(id),p,d,pr,strftime("%Y-%m-%d", gmtime())])
        else:
            print('Data has been Collected For today')
        
        
    
    



    
# Wait 20 seconds for page to load
timeout = 20
try:
    #WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
    #WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='img-responsive']")))
    # find_elements_by_xpath returns an array of selenium objects.
    titles_element = browser.find_elements_by_xpath("//div[@class='product ng-scope']")
    
    # use list comprehension to get the actual repo titles and not the selenium objects.
    titles = [x.text for x in titles_element]
    # print out all the titles.
    print('titles:')
    #print(titles, '\n')
    
    language_element = browser.find_elements_by_xpath("//div[@class='price']")
    # same concept as for list-comprehension above.
    languages = [x.text for x in language_element]
    print("languages:")
    #print(languages, '\n')
    
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
'''