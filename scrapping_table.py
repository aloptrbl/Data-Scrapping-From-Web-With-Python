# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:40:52 2018
This program demonstrated scraping tabular data from web page
@author: alop-dev
"""

import requests

#Step 1 : Create Request object - to get the webpage you want
request = requests.get("https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/all-time")

#Step 2 : Get the page in text and store it locally
page = request.text

#Step 3 : Parse page into soap object
soup = BeautifulSoup(page, 'lmxl')


print("Program ends")
