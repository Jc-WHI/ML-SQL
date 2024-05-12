import numpy as np
import csv



def col_checker():
    with open("C://flow.csv") as fl:
        reader = csv.reader(fl, delimiter=",", quotechar='"')

    # next(reader, None)  # skip the headers
        data_read = [row for row in reader[10]]
        print(data_read)