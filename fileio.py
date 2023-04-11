
# * Module for handling file manipulation

# TODO: convert data from CSV to JSON format at some point
#  import json

def open_file_CSV(fname, mode):

    try:
        f = open(fname, mode, encoding="utf-8")
    except IOError:
        print("Error opening file " + fname)
    else:
        print(fname + " opened successfully")
        data = f.read()
        print(data)
        f.close()

