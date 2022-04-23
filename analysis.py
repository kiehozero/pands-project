# Main file for performing analysis

# 1. Output a summary of each variable to a single text file
# 2. Save a histogram of each variable to png files
# 3. Output a scatter plot for each pair of variables
# 4. Performs any other analysis you think is appropriate
# The last point is what will make the project stand out, the first three are the minimum requirements
# Remember to comment and document all processes to show understanding of each step, especially where you may be following a tutorial

import numpy as np
import csv

with open("iris.csv", "r") as d:
    sample_data = list(csv.reader(d, delimiter=","))

sample_data = np.array(sample_data)
print(sample_data)