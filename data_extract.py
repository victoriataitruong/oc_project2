"""
Requests: an elegant and simple HTTP library for Python, commonly used for REST API calls.

Beautiful Soup: a library for pulling data out of HTML and XML files.  

Pandas: a fast, powerful, and easy-to-use open-source data analysis and manipulation tool. 

To install a package using pip in your terminal, we use the following pattern: pip install <name-of-package>

To view the packages already installed, you can type the following:

Using the  import  keyword at the top of your code file, you can import certain library functions or the entire library at once. For example, to import the entire requests library, you must first install requests using your terminal with  pip install requests . Then you can write the following code in your text editor: 
"""

import requests
# Now to call the get() function in the requests library, write:
requests.get()
# If you want to import just one function named  get  from the requests library, write the following:
from requests import get

"""
Now that we have the HTML source, we need to parse it. The way to parse the HTML is through the HTML attributes of  class  and  id  mentioned earlier.  

We can use Beautiful Soup to help find the elements that can be identified with the class or the ID that we want to find. Similar to any library, we’ll use pip to install Beautiful Soup.
pip install beautifulsoup4

Web scraping is the automated process of retrieving data from the internet.

ETL stands for extract, transform, load, and is a widely used industry acronym representing the process of taking data from one place, changing it up a little, and storing it in another place.

HTML is the backbone of any web page, and understanding its structure will help you figure out how to get the data you need.

Requests and Beautiful Soup are third-party Python libraries that can help you retrieve and parse data from the internet.

Parsing data means preparing it for transformation or storage.
"""
