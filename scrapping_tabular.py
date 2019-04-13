# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 11:40:52 2018
This program demonstrated scraping tabular data from web page (Page Analysis)
@author: alop-dev
"""


import requests

from bs4 import BeautifulSoup

#Step 1 : Create Request object - to get the webpage you want
request = requests.get("https://www.the-numbers.com/box-office-records/worldwide/all-movies/cumulative/all-time")

#Step 2 : Get the page in text and store it locally
page = request.text

#Step 3 : Parse page into soap object
soup = BeautifulSoup(page, 'lxml')

#Step 4 : Get the table
table = soup.find('table')

#Step 5 : Get the table header
thead = table.find('thead')
tr = thead.find('tr')
ths = tr.findAll('th')

table_header = ""
for th in ths:
    table_header += th.get_text().strip() + ","
print(table_header)

#Step 6 : Open file to write data
out_file = open("boxoffice.csv","w", encoding='utf-8')

#Step 6 : Get table data
table_data = ""
tbody = table.find('tbody')
rows = tbody.findAll('tr')

for row in rows:
    tds = row.findAll('td')
    for td in tds:
        table_data += td.get_text().strip() + ","
        
    print(table_data + "\n")
    table_data = ""

#Step 7 : Open file to write data
out_file.write(table_header + "\n")

#Step 8 : Get table data
table_data = ""
tbody = table.find('tbody')
rows = tbody.findAll('tr')

#Step 9 : Record table data in file
for row in rows:
    tds = row.findAll('td')
    for td in tds:
        table_data += td.get_text().strip() + ","
#indent is important here    
    print(table_data + "\n")
    out_file.write(table_data + "\n")
    table_data = ""

#Step 10: Close file
out_file.close()

print("Program ends")