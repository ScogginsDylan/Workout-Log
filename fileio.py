
# * Module for handling file manipulation and data processing

# ? may have to consider restructuring how data is passed between modules, try to reduce module nesting
# TODO: convert data from CSV to JSON format at some point
#  import json
import pandas as pd
import numpy as np

# * Reads data from CSV file into a pandas dataframe, which gets converted to a numpy array
# * for easier processing
def process_file_CSV(fname):
    with open(fname, newline='', encoding='utf-8') as csvfile:
        exercise_dframe = pd.read_csv(csvfile)
        exercise_nparray = np.array(exercise_dframe)

        return exercise_nparray

# * Converts np array back to pandas df and writes data to makeshift database aka CSV file
# TODO: 1) determine structure of database
# TODO: 2) account for existing file to append to
# def write_to_CSV(nparray, fname):
#     new_df = pd.DataFrame(nparray, columns=['Exercise','Weight'])
#     new_df.to_csv(fname, sep='\t', encoding='utf-8', index=False)
#     return

# * For testing purposes only
def print_data(nparray):
    print(nparray)