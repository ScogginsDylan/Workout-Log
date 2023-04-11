# Start of a new workout log app to track progress using graphical data. Uses TK and some graph modules
# to display data over period of weeks/months/years.

# * main.py is the driver file for the app

import fileio
import graph

# ? should main.py handle file io or graph.py?
# fileio.open_file_CSV("531 4-day program - Leader #1 (5s PRO_FSL).csv", "r")

# * Generates graphs from data provided to generate_graph function in graph.py
graph.generate_graph("Leader 1 Cycle Data",[1,2,3],[2,4,1])
graph.generate_graph("Leader 2 Cylce Data",[1,2,3],[2,6,3])
graph.generate_graph("Anchor Cycle Data",[1,2,3],[2,6,3])