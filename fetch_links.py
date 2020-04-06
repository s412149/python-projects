# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:47:27 2020

@author: agato
"""

import urllib.request
from bs4 import BeautifulSoup

url = 'file:///C:/Users/agato/Desktop/example3.html'
response = urllib.request.urlopen(url)
data = response.read()
doc = BeautifulSoup(data, 'html.parser')

li = doc.select('ol > li')
i = 1
for link in li:
    print(str(i) +'. ' + link.get_text())
    i += 1



