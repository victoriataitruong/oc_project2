"""
The  .reader()  method will take all the text in a CSV, parse it line by line, and convert each row into a list of strings. You can use different delimiters to decide how to break up each row, but the most common one is a comma. The code snippet below reads the CSV file and prints each row.
"""

import csv

with open('test_data.csv') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        print (row)