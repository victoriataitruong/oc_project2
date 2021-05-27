import requests
import csv 
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

book_urls = [w.replace('../../../', 'http://books.toscrape.com/catalogue/') for w in book_urls]
print (book_urls)