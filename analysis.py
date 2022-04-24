# Main file for performing analysis

# 1. Output a summary of each variable to a single text file
# 2. Save a histogram of each variable to png files
# 3. Output a scatter plot for each pair of variables
# 4. Performs any other analysis you think is appropriate
# The last point is what will make the project stand out, the first three are the minimum requirements
# Remember to comment and document all processes to show understanding of each step, especially where you may be following a tutorial

import csv
import numpy as np
import pandas as pd

iris_csv = list(csv.reader(open("iris.csv", "r"), delimiter=","))

iris_csv = np.array(iris_csv)
# selects only PL and Species columns
pet_len = iris_csv[:, [2,4]]
print(pet_len)
# selects all data for Virginica species
for row in iris_csv:
    if row[4] == "virginica":
        print(row)