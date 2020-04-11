# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:10:17 2020

@author: agato
"""
from googletrans import Translator
import requests
import json

def googletrans():
    translator = Translator()
    result = translator.translate('Jak się masz?',dest='es')
    print(result.text)
    
    
def piratetrans(text):
    url = 'https://api.funtranslations.com/translate/pirate.json'
    data = {'text': text}
    
    response = requests.post(url, data=data)
    json_data = json.loads(response.text)
    print(type(json_data))
    print(json_data['contents']['translated'])
    
piratetrans('Hello, sir')
    