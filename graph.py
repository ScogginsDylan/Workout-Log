
# * Handles graph rendering

import numpy as np
import matplotlib.pyplot as plt

# * Generate graph from provided nparray data
def generate_graph(title, nparray):

    x_indices = [0]
    y_indices = [1]
    x_axis = np.take(nparray, x_indices, axis=1)
    y_axis = np.take(nparray, y_indices, axis=1)

    # * Converts axis to shape that matplotlib likes
    mod_x_axis = x_axis.ravel()
    mod_y_axis = y_axis.ravel()

    plt.plot(mod_x_axis,mod_y_axis)

    plt.xlabel('Time')
    plt.ylabel('Weight')
    plt.title(title)

    plt.show()
