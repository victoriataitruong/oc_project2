import requests
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

#See html source
print(page.content)

"""
Even though we have all the HTML saved in our code, it still looks like a whole lot of mumbo jumbo. We have to figure out how to parse out the exact elements that we want - and we can use Beautiful Soup to do just that!

Parse means "to split a file or other input into pieces of data that can be easily manipulated or stored."
"""