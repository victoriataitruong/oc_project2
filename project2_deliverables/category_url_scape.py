import requests
import csv 
import re
from bs4 import BeautifulSoup

additional_pages = True
category_url = "http://books.toscrape.com/catalogue/category/books/default_15/index.html"

category_url_additional_page_count = 1
book_urls = []

while(additional_pages): 
    page = requests.get(category_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup_string = str(soup.find_all("h3"))
    book_urls.append(soup_string)
    category_url_additional_page_count+= 1
    category_url_additional_page_count_str = str(category_url_additional_page_count)
    category_url = "http://books.toscrape.com/catalogue/category/books/default_15/page-" + category_url_additional_page_count_str + ".html"
    r = requests.get(category_url)
    if(r.status_code != 200):
        additional_pages = False
# replacing shortcut url with full url
book_urls = [w.replace('../../../', 'http://books.toscrape.com/catalogue/') for w in book_urls]
# extracting urls 
book_urls = [re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', str(book_urls))]
# changing list to string
str_book_lists = ','.join(book_urls[0])
# a list of all urls from the category
my_urls = str_book_lists.split(",")



f = csv.writer(open('multiple_book_data.csv', 'w', encoding="utf-8"))
f.writerow(["url", 'universal_product_code', 'title', 'price_including_tax','price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])
for x in my_urls:
   # url to scrape from
    book_url = x
    page = requests.get(book_url)
    # turn HTML to BeautifulSoup object
    soup = BeautifulSoup(page.content, 'html.parser')
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


