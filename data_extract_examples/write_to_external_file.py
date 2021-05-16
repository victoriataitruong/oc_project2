"""
To both read from and write to a file, you can use the built-in function  open(), which takes in two parameters: file name and mode. 
File name: the directory path to the file that you want to read or write to. 

Mode: the mode you want to use for the file. The main options are:

Read:  "r"

Write:  "w"

Append:  "a"

Read and write:  "r+" 

To create a new file called “hello.txt” and write “Hello, world!” to it, use the following code:
"""

# Requests
import requests
import csv 

#BeautifulSoup
from bs4 import BeautifulSoup


#Save titles and descriptions as lists of strings
def extract_strings(elements):
	items = []
	for e in elements:
		items.append(e.string)
	return items


# write data to a csv file
def load_data(file_name, headers, titles, descriptions):
	with open(file_name, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',',
	                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
		writer.writerow(headers)
		for i in range(len(titles)):
			row = [titles[i], descriptions[i]]
			writer.writerow(row)

def main():
	# url to scrape
	url = "https://www.gov.uk/search/news-and-communications"

	page = requests.get(url)

	# Turn HTML to BeautifulSoup object
	soup = BeautifulSoup(page.content, 'html.parser')

	#Get all titles with gem-c-document-list__item-title class
	titles = soup.find_all("a", class_="gem-c-document-list__item-title")
	#Get all descriptions with class gem-c-document-list__item-description
	descriptions = soup.find_all("p", class_="gem-c-document-list__item-description")


	headers = ["title", "description"]
	titles = extract_strings(titles)
	descriptions = extract_strings(descriptions)
	load_data("data1.csv", headers, titles, descriptions)


main()
