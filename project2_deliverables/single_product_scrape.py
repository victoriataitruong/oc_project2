# Requests
import requests
import csv 

#BeautifulSoup
from bs4 import BeautifulSoup

# url to scrape
url = "http://books.toscrape.com/catalogue/walt-disneys-alice-in-wonderland_777/index.html"

page = requests.get(url)

# Turn HTML to BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

# file = open("test.csv", 'w')
book_data = []
for row in soup.find_all('tr'):
    for col in row.find_all('td'):
        book_data.append(col.text)
		
print (book_data)	


