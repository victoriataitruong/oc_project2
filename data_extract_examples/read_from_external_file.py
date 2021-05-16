"""
The  .reader()  method will take all the text in a CSV, parse it line by line, and convert each row into a list of strings. You can use different delimiters to decide how to break up each row, but the most common one is a comma. The code snippet below reads the CSV file and prints each row.


import csv

with open('test_data.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print (row)


While this approach can be helpful sometimes, it treats the header row the same as any other. A more useful method for reading CSVs while recognizing headers to identify the columns is the  DictReader()  method. This method knows the first line is a header and saves the rest of the rows as dictionaries with each key as the column name and the value as the column value.

The code below shows how to use the  DictReader()  method. 
"""

import csv

with open('test_data.csv') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        print(row['name'] + " works as a " + row['occupation'] + " and their favorite color is " + row['favorite_color'])