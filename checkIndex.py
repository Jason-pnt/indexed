#-*-coding: utf-8 -*-
# pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
#pip3 install pillow selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert 
from PIL import Image
import time
import csv
import re
import sys
import datetime
import string
import os
from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import sys

nowTime = datetime.datetime.now().strftime('%Y%m%d%H%M')
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('log-level=3')
# chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--ignore-certificate-errors')
# chrome_options.add_argument('--disable-images')
chrome_options.add_argument('--start-maximized')

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.amazon.com/?currency=USD&language=en_US')
time.sleep(15)
driver.execute_script("document.body.style.zoom='0.9'")

with open('test.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        if (len(row) != 0):
            indexed=''
            banded=''
            lineToStr = row[0]
            lineToList = lineToStr.split(' ')
            linkStr='s?k=' #+ sys.argv[1] + '+'
            for i in range(len(lineToList)):
                linkStr= linkStr + lineToList[i] + '+'
            linkStr= linkStr[:-1]
            driver.maximize_window()
            keyword = linkStr.replace('+', ' ')[4:]
            bandlinkStr = linkStr
            linkStr = list(linkStr)
            asinNum = linkStr.index('=') + 1
            linkStr.insert(asinNum, sys.argv[1] + '+')
            linkStr = ''.join(linkStr)
            driver.get('https://www.amazon.com/' + linkStr + '&language=en_US')
            soup = BeautifulSoup(driver.page_source, "html.parser")
            asin = soup.find_all(href=re.compile("READY-PARD-"))
            if len(asin):
                indexed='Y'
            else:
                indexed='N'
            driver.get('https://www.amazon.com/' + bandlinkStr + '&language=en_US')
            count = driver.find_element_by_xpath('//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[1]').text
            count = count.split(' ')[-3].replace(',','')
            soup = BeautifulSoup(driver.page_source, "html.parser")
            bandList = []
            for bands in soup.select('#brandsRefinements > ul > li > span > a > span'):
                bandList.append(bands.text)
            if 'READY PARD' in bandList:
                banded='Y'
            else:
                banded='N'
            print('Keyword: '+ keyword +' Index: '+ indexed +' Band : '+banded+' Number: '+ count)
driver.quit()