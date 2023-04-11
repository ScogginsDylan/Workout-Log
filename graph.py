
# * Handles data processing and rendering of graphs

import fileio
import matplotlib.pyplot as plt

# * Generate graph from Leader#1 data
def generate_graph(title, x_axis, y_axis):

    plt.plot(x_axis,y_axis)

    plt.xlabel('Time')
    plt.ylabel('Weight')
    plt.title(title)

    plt.show()
