
# * Module for handling file manipulation and data processing

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

        # TODO: parse np array for data to be sent to graph.py
        indices = [0,1]
        processed_nparray = np.take(exercise_nparray, indices, axis=1)
        return processed_nparray

# * For testing purposes only
def print_data(nparray):
    print(nparray)