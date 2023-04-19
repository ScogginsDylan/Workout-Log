# Start of a new workout log app to track progress using graphical data.
# Uses Pandas, MatPlotLib, and Numpy modules to display graphical data over period of time.

# * main.py is the driver file for the program

import fileio
import graph

def main():

    # * Generates graphs from data provided to generate_graph function in graph.py
    graph.generate_graph('531 TM Progress',fileio.process_file_CSV('531 4-day program - TM Log.csv'))

    # * Write data to makeshift database aka CSV file
    # TODO: finish write_to_CSV function
    # fileio.write_to_CSV(fileio.process_file_CSV('531 4-day program - TM.csv'), '531 Log.csv')

main()