
# * Module for handling file manipulation

# TODO: convert data from CSV to JSON format at some point
#  import json
import pandas

def open_file_CSV(fname):
    with open(fname, newline='', encoding='utf-8') as csvfile:
        dframe = pandas.read_csv(csvfile)
        print(dframe)