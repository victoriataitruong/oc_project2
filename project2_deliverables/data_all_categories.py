# import libs
import requests
import csv 
import re
from bs4 import BeautifulSoup

# url to scrape from
book_url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
page = requests.get(book_url)

# turn HTML to BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

# variable to hold all category urls
book_categories = []

# looping through and getting all links
for link in soup.find_all('a'):
    book_categories.append(link.get('href', {"class":"side_categories"}))
# 
new_book_categories = []
# index 3 to 52
for i in range(3, 53):
    new_book_categories.append(book_categories[i])

new_book_categories = [w.replace('../', 'http://books.toscrape.com/catalogue/category/') for w in new_book_categories]

print (new_book_categories)