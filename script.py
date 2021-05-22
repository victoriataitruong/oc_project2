import requests
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

#See html source
print(page.content)

