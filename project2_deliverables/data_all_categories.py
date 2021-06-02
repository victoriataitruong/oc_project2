# import libs
import requests
import csv 
from bs4 import BeautifulSoup
import re
from PIL import Image
# url to scrape from
booktoscape_url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
page = requests.get(booktoscape_url)
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
# add url prefixes
new_book_categories = [w.replace('../', 'http://books.toscrape.com/catalogue/category/') for w in new_book_categories]
# grab category names
for h in new_book_categories: 
    # to extract category names from url
    index = 0   
    if index < 8:
        cat_name_url = h.split('/')[-2]
        cat_name = cat_name_url[:-2]
    else:
        cat_name_url = h.split('/')[-2]
        cat_name = cat_name_url[:-3]
    index += 1
    cat_name_str = cat_name + ".csv"
    # creating a csv file with cat name and adding headings
    f = csv.writer(open('csv_files/' + cat_name_str, 'w', encoding="utf-8"))
    f.writerow(["url", 'universal_product_code', 'title', 'price_including_tax','price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])   
    # grabbing the book urls 
    additional_pages = True
    category_url = h
    category_url_additional_page_count = 1
    book_urls = []
    while(additional_pages): 
        page = requests.get(category_url)
        soup = BeautifulSoup(page.content, 'html.parser')
        soup_string = str(soup.find_all("h3"))
        book_urls.append(soup_string)
        category_url_additional_page_count+= 1
        category_url_additional_page_count_str = str(category_url_additional_page_count)
        category_url = "http://books.toscrape.com/catalogue/category/books/" + cat_name_url + "/page-" + category_url_additional_page_count_str + ".html"
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
    # scarping book data for each book
    book_count = 1
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
        image_url = soup.find('img')
        # write scaped data to csv file
        f.writerow([url, universal_product_code, title, price_including_tax, price_excluding_tax, number_available, product_description, category, review_rating, image_url])
        # saving all images
        image_url = image_url['src']
        image_url = image_url.replace('../..', 'http://books.toscrape.com/')
        img = Image.open(requests.get(image_url, stream = True).raw)
        img.save(f'{"images"}/{cat_name}_{book_count}.jpeg')
        book_count+=1
       

    
