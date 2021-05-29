Required:

1. single_product_scrape.py

Pick any single product page on Books to Scrape. Write a Python script that visits this page and extracts the following information:

product_page_url
universal_ product_code (upc)
title 
price_including_tax
price_excluding_tax
number_available
product_description
category
review_rating
image_url
Write the data to a CSV file using the above fields as column headings.

2. category_url_scape.py

Now that you have obtained the information for one book, you can try and get all of the necessary information for one category. Pick any book category on Books to Scrape. Write a Python script that visits this category page and extracts the product page URL for each book in the category. Then combine this with the work you have completed to extract the product data for all the books in your category and write the data to a single CSV file.

Note: some category pages have more than 20 books listed, so they are spread across different pages (‘pagination’). Your application should be able to handle this scenario automatically!