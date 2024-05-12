import csv
import sys
import json 
import pandas as pd

def read_csv_rows(file_path, num_rows=100000):
    with open(file_path) as fl:
        reader = csv.reader(fl, delimiter=",", quotechar='"')
        headers = next(reader)  
        data_rows = [row for _, row in zip(range(num_rows), reader)]
        return headers, data_rows


csv_file_path = "C:/flows.csv"
column_names, rows = read_csv_rows(csv_file_path)

df = pd.DataFrame(rows, columns=column_names)
#to do list : json labeling 
df.to_json("data.json")