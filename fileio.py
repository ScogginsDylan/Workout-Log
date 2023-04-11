
# * Module for handling file manipulation

# TODO: convert data from CSV to JSON format at some point
#  import json
import csv

def open_file_CSV(fname):
    with open(fname, newline='', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
            for col in reader:
                print(col)

