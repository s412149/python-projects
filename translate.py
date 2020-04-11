# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:10:17 2020

@author: agato
"""
from googletrans import Translator

def main():
    translator = Translator()
    result = translator.translate('Jak się masz?',dest='es')
    print(result.text)
    
    
main()