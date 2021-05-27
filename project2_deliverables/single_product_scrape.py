# import libs
import requests
import csv 
from bs4 import BeautifulSoup

# url to scrape from
book_url = "http://books.toscrape.com/catalogue/walt-disneys-alice-in-wonderland_777/index.html"
page = requests.get(book_url)

# turn HTML to BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')

# open csv file and write headings
f = csv.writer(open('book_data.csv', 'w'))
f.writerow(["url", 'universal_product_code', 'title', 'price_including_tax','price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])

# scape data 
url = book_url,
universal_product_code = soup.tr, 
title = soup.title,
price_including_tax = soup.tr.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling,
price_excluding_tax = soup.tr.next_sibling.next_sibling.next_sibling.next_sibling,
number_available = soup.tr.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling,
product_description = soup.find('meta', attrs={'name': 'description'})
category = soup.li.next_sibling.next_sibling.next_sibling.next_sibling,
review_rating = soup.p.next_sibling.next_sibling.next_sibling.next_sibling,
image_url = soup.img

# write scaped data to csv file
f.writerow([url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url])
