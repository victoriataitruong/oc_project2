"""
product_page_url*
universal_ product_code (upc)* 
title*
price_including_tax*
price_excluding_tax*
number_available
product_description
category*
review_rating
image_url*
"""
# requests
import requests
import csv 
# beautifulSoup
from bs4 import BeautifulSoup
# url to scrape
url = "http://books.toscrape.com/catalogue/walt-disneys-alice-in-wonderland_777/index.html"
page = requests.get(url)
# turn HTML to BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

# create a list to hold scaped data
book_data = []
# adding product_page_url
book_data.append(url)
# adding universal_ product_code
universal_product_code = soup.tr
book_data.append(universal_product_code)
# adding page title to list 
title = soup.title
book_data.append(title)
# adding price_including_tax
price_including_tax = soup.tr.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
book_data.append(price_including_tax)
# adding price_excluding_tax
price_excluding_tax = soup.tr.next_sibling.next_sibling.next_sibling.next_sibling
book_data.append(price_excluding_tax)
# printing out list
print(*book_data, sep='\n')

