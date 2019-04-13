# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:40:52 2018
This program demonstrated scraping tabular data from web page (Page Analysis)
@author: alop-dev
"""

import pandas as pd

import requests

from bs4 import BeautifulSoup

#Step 1: Create request object - to get the webpage you want 
request = requests.get("https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/all-time")

#Step 2: Get the page in text and store it locally
page = request.text

#Step 3: Parse page into soup object
soup = BeautifulSoup(page, 'lxml')

#Step 4: Declare list to store data from each column:
ranks = []
releases = []
movies = []
worldwides = []
domestics = []
internationals = []

#Step 4: Get the table
table = soup.find('table')

#Step 5: Get table header
thead = table.find('thead')
tr = thead.find('tr')
ths = tr.findAll('th')

table_header = ""
for th in ths:
    table_header += th.get_text().strip() + ","
print(table_header)

#Step 6: Open file to write data
#out_file = open("boxoffice.csv","w", encoding='utf-8')

#Step 6: Get table data
table_data = ""
tbody = table.find('tbody')
rows = tbody.findAll('tr')

for row in rows:
    tds = row.findAll('td')
    
    ranks.append(tds[0].get_text().strip())
    releases.append(tds[1].get_text().strip())
    movies.append(tds[2].get_text().strip())
    worldwides.append(tds[3].get_text().strip())
    domestics.append(tds[4].get_text().strip())
    internationals.append(tds[5].get_text().strip())

#Step 7: Write table header
#out_file.write(table_header + "\n")

#Step 8: Get table data
table_data = ""
tbody = table.find('tbody')
rows = tbody.findAll('tr')
df = pd.DataFrame()

df['rank'] = ranks
df['release'] = releases
df['movie'] = movies
df['worldwide'] = worldwides
df['domestic'] = domestics
df['international'] = internationals

#Step 9: Save dataframe
df.to_excel("boxoffice.xlsx", header=True)

#Step 9: Record table data in file
for row in rows:
    tds = row.findAll('td')
    for td in tds:
        table_data += td.get_text().strip() + ","
        
    print(table_data + "\n")
#    out_file.write(table_data + "\n")
    table_data = ""

#Step 10: Close file
#out_file.close()

print ("Program ends")