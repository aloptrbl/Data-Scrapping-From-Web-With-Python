# -*- coding: utf-8 -*-
"""
Created on Fri Aug 17 10:06:31 2018
This program demonstrated harvesting/scrapping
@author: alop-dev
"""

from bs4 import BeautifulSoup

import requests

#Step 1 : Create request object - to get the webpage you want
request = requests.get("https://www.thestar.com.my/news/nation/2018/08/12/a-new-rock-for-batu-the-youngest-ever-mp-in-the-country-is-all-for-lowering-the-minimum-age-to-vote/")

#Step 2 : Get the page in text and store it locally
page = request.text

#Step 3 : Parse the page in text and store it locally 
soup = BeautifulSoup(page, 'lxml')

#Step 4 : Find the new heading using class object, get the text and display it
heading = soup.find('div', attrs={'class' : 'headline story-pg'})
head_text = heading.get_text().strip()

#Step 5 : Find the category and display it
category = soup.find('a', attrs={'class' : 'kicker'})
category_text = category.get_text()

#Step 6 : Find date and display it
date = soup.find('p', attrs={'class' : 'date'})
date_text = date.get_text().strip()

#Step 7 : Save the text into file 
output_file = open("news.txt","w")
output_file.write(head_text + "\n")
output_file.write(date_text + "\n")

div = soup.find('div', attrs={'id' : 'slcontent_0_sleft_0_storyDiv'})
stories = div.findAll('p')
for story in stories: 
    #indent is important here
    story_text = story.get_text()
    print(story_text)
    output_file.write(story_text + "\n")

print(head_text)
print(date_text)
print(category_text)
output_file.close()
print("Program ends")
