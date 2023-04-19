
# * Handles graph rendering

import numpy as np
import matplotlib.pyplot as plt

# * Generate graph from provided nparray data
def generate_graph(title, nparray):

    # * Splice each column into individual numpy ndarrays
    x_indices = [0]
    benchp_indices = [1]
    squat_indices = [2]
    ohp_indices = [3]
    deadlift_indices = [4]
    x_axis = np.take(nparray, x_indices, axis=1)
    benchp_axis = np.take(nparray, benchp_indices, axis=1)
    squat_axis = np.take(nparray, squat_indices, axis=1)
    ohp_axis = np.take(nparray, ohp_indices, axis=1)
    deadlift_axis = np.take(nparray, deadlift_indices, axis=1)

    # * Converts axis to shape that matplotlib likes
    mod_x_axis = x_axis.ravel()
    mod_benchp_axis = benchp_axis.ravel()
    mod_squat_axis = squat_axis.ravel()
    mod_ohp_axis = ohp_axis.ravel()
    mod_deadlift_axis = deadlift_axis.ravel()

    # * Creates graph for each exercise
    plt.plot(mod_x_axis, mod_benchp_axis, color='r', label='bench press')
    plt.plot(mod_x_axis, mod_squat_axis, color='g', label='squat')
    plt.plot(mod_x_axis, mod_ohp_axis, color='b', label='overhead press')
    plt.plot(mod_x_axis, mod_deadlift_axis, color='y', label='deadlift')

    # * Assigns labels and title to graph
    plt.xlabel('Time(cycles)')
    plt.ylabel('Weight(lbs)')
    plt.title(title)

    # * Provides legend for readability
    plt.legend()

    # * Renders the graph
    plt.show()
