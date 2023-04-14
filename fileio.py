
# * Module for handling file manipulation and data processing

# TODO: convert data from CSV to JSON format at some point
#  import json
import pandas as pd

def open_file_CSV(fname):
    with open(fname, newline='', encoding='utf-8') as csvfile:
        exercise_dframe = pd.read_csv(csvfile, index_col='Week')
        print(exercise_dframe)