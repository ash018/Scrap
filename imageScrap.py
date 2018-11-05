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

option = webdriver.ChromeOptions()
#option.add_argument(" — incognito")

url = "https://www.facebook.com/Shwapno.ACILL/"

browser = webdriver.Chrome(executable_path=r"F:\software\chromedriver", chrome_options=option)
browser.get(url)
soup = BeautifulSoup(browser.page_source, 'lxml')
#print(soup.prettify())


'''
with open('meenabazar_feature.csv', mode='a',encoding="utf-8",newline='') as meenabazar_feature:
    meenabazar_feature = csv.writer(meenabazar_feature, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    meenabazar_feature.writerow(['ID','ProductName', 'Price','Date'])
    id=0
    
    
    for product,price in zip(productName,productPrice):
        id+=1
        print(product.getText().strip()+' '+price.getText().strip())
        meenabazar_feature.writerow([ str(id),product.getText().strip(),price.getText().strip().split()[1]+'TK',strftime("%Y-%m-%d", gmtime())])
'''        
    
    



    
# Wait 20 seconds for page to load
timeout = 60
try:
    #WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))
    #WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='img-responsive']")))
    # find_elements_by_xpath returns an array of selenium objects.
    productName = soup.find_all('div',class_='UFILikeSentenceText')
    id = 0
    productPrice = soup.find_all('div',class_='_5pbx userContent _3576')
    for product in productName:
        print(product.getText().strip())
    
    for product,price in zip(productName,productPrice):
        id+=1
        print(product.getText().strip()+' '+price.getText().strip())
    titles_element = browser.find_elements_by_xpath("//div[@class='product ng-scope']")
    
    # use list comprehension to get the actual repo titles and not the selenium objects.
    titles = [x.text for x in titles_element]
    # print out all the titles.
    print('titles:')
    print(titles, '\n')
    
    language_element = browser.find_elements_by_xpath("//div[@class='price']")
    # same concept as for list-comprehension above.
    languages = [x.text for x in language_element]
    print("languages:")
    print(languages, '\n')
    
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
    
