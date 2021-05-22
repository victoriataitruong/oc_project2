"""
product_page_url: http://books.toscrape.com/catalogue/walt-disneys-alice-in-wonderland_777/index.html ?
universal_ product_code (upc): 6a31307a81e8f3a8
title: Walt Disney's Alice in Wonderland
price_including_tax: £12.96
price_excluding_tax: £12.96
number_available: 14
product_description:
The fantastical tale of a young girl chasing her White Rabbit has delighted children since Lewis Carroll wrote it generations ago. Here his Wonderland shines anew, viewed through the looking glasses of two incomparable artists.Mary Blair's vibrant art helped shape the look of Walt Disney's classic animated film. Collected in a picture book for the first time, her illustrat The fantastical tale of a young girl chasing her White Rabbit has delighted children since Lewis Carroll wrote it generations ago. Here his Wonderland shines anew, viewed through the looking glasses of two incomparable artists.Mary Blair's vibrant art helped shape the look of Walt Disney's classic animated film. Collected in a picture book for the first time, her illustrations capture the essence of such memorable characters as the Queen of Hearts and the Mad Hatter with stunning immediacy. Jon Scieszka's captivating text celebrates all that is curious-and all that is nonsensical-about the world that holds Alice spellbound, from a deliciously absurd tea party to the spectacle of a kingdom of playing cards . Brimming with wit and wonder, this sparkling retelling will enchant readers from the moment Alice falls down the rabbit hole, whether or not they've made the journey before. ...more
category: Childrens?
review_rating: 5
image_url: ../../media/cache/0f/65/0f65a1f2a3705c67b3d2a787ab3e8b99.jpg
"""
# Requests
import requests
import csv 
#BeautifulSoup
from bs4 import BeautifulSoup

# url to scrape
url = "http://books.toscrape.com/catalogue/walt-disneys-alice-in-wonderland_777/index.html"

page = requests.get(url)

#See html source
print(page.content)

# Turn HTML to BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

#Get all titles with gem-c-document-list__item-title class
bs_titles = soup.find_all("th", class="table table-striped")
 
#Save titles and descriptions as lists of strings
titles = []
for title in bs_titles:
	titles.append(title.string)

