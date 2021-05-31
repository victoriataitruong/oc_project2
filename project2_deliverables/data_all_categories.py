# import libs
import requests
import csv 
from bs4 import BeautifulSoup
import re


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

# list to hold all urls
new_book_categories = []
# grabbing only category urls
for i in range(3, 53):
    new_book_categories.append(book_categories[i])

# add url prefixes. new_book_categories now has all book urls for bookstoscape
new_book_categories = [w.replace('../', 'http://books.toscrape.com/catalogue/category/') for w in new_book_categories]

# visit each category page and extract all book urls
book_urls = []
for i in new_book_categories: 
    page = requests.get(i)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup_string = str(soup.find_all("h3"))
    book_urls.append(soup_string)
book_urls = [w.replace('../../../', 'http://books.toscrape.com/catalogue/') for w in book_urls]  
book_urls = [re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(book_urls))]
print(book_urls)