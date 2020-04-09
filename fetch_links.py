# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:47:27 2020

@author: agato
"""

import urllib.request
from bs4 import BeautifulSoup

url = input("Input your url: ")
#url = 'file:///C:/Users/agato/Desktop/example3.html'
response = urllib.request.urlopen(url)
data = response.read()
doc = BeautifulSoup(data, 'html.parser')

lists = doc.find_all('ol')
for li in lists:
    i = 1
    list_items = li.find_all('li')
    print('\n')
    for l in list_items:
        print(str(i) +'. ' + l.get_text())
        i += 1



