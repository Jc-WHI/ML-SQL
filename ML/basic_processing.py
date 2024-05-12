import csv
import sys

def read_csv_rows(file_path, num_rows=5):
    with open(file_path) as fl:
        reader = csv.reader(fl, delimiter=",", quotechar='"')
        headers = next(reader)  
        data_rows = [row for _, row in zip(range(num_rows), reader)]
        return headers, data_rows


csv_file_path = "C:/flows.csv"
column_names, first_5_rows = read_csv_rows(csv_file_path)

print("Column names:")
print(column_names)

print("\nFirst 5 rows:")
for row in first_5_rows:
    print(row)
