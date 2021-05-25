import pandas as pd
import requests

url = "https://worldpopulationreview.com/countries/countries-by-gdp/#worldCountries"

r = requests.get(url)
df_list = pd.read_html(r.text) # this parses all the tables in webpages to a list
df = df_list[0]
df.head()