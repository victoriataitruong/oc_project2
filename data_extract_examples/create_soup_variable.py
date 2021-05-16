import requests
from bs4 import BeautifulSoup
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

"""
Once we create a “soup object” out of this HTML, we can access all the elements of the page really easily!

#Get HTML page title
>> soup.title

#Get string of HTML title
>> soup.title.string

#Find all elements with <a> tag
>>soup.find_all('a')

# Find element with id of “link1”
>> soup.find(id="link1")

#Find all p elements with class “title”
>> soup.find_all("p", class_="title")
"""