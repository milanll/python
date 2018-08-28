import csv

filename = 'F:/Jupyter Notebook/matplotlib_pygal_csv_json/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    print(list(reader))