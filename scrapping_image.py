# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 15:32:09 2018
This program demonstrated scraping image from web
@author: alop-dev
"""

import requests

from bs4 import BeautifulSoup

#Step 1: Create request object - to get the webpage you want 
request = requests.get("https://static-v3.fashionvalet.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/1/2/12830071809_a.jpg")

#Step 2: Get the page in text and store it locally
page = request.text

#Step 3: Parse page into soup object
soup = BeautifulSoup(page, 'lxml')

#Step 4 : Find Image
image = soup.find("img",{"class" : "img-responsive thumb_swap"})

print("Program ends")

