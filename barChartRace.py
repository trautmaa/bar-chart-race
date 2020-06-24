import pandas as pd
import csv
from urllib.request import urlopen

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports_us/06-19-2020.csv'

df = pd.read_csv(url, error_bad_lines=False)
print(df)