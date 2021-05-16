# Requests
import requests
import csv 
#BeautifulSoup
from bs4 import BeautifulSoup

# url to scrape
url = "https://victoriataitruong.github.io/project2/"

page = requests.get(url)

#See html source
print(page.content)


# Turn HTML to BeautifulSoup object
soup = BeautifulSoup(page.content, 'html.parser')
soup.title.string



