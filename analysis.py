# Main file for performing analysis

# 1. Output a summary of each variable to a single text file
# 2. Save a histogram of each variable to png files
# 3. Output a scatter plot for each pair of variables
# 4. Performs any other analysis you think is appropriate
# The last point is what will make the project stand out, the first three are the minimum requirements
# Remember to comment and document all processes to show understanding of each step, especially where you may be following a tutorial

import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

iris_csv = pd.read_csv("iris.csv")

iris_csv = np.array(iris_csv)
# selects only PL and Species columns
petal = iris_csv[1:, [2,3,4]]
# selects all data for Virginica species, need appending to a list to use as data points, make into a function, loop through species name to
# create unique dataset for each, then another function that loops through each dataset to create scatters to overlay each other
test = []
for row in petal:
    if row[2] == "virginica":
        test.append(list(row))

testarr = np.array(test)



print(testarr) 
filter_arr = petal[:,2]=="virginica"

print(filter_arr)

x_axis = testarr[:,0]
y_axis = testarr[:,1]

# can plot multiple items in one file

plt.scatter(x_axis,y_axis)
plt.show()

finalfilter = petal[filter_arr]

print(finalfilter)

# file to create summary of sepal_length
# number of records, max of each, min of each, mean of each, printout of all items

# file to create summary of sepal_width
# number of records, max of each, min of each, mean of each, printout of all items

# file to create summary of petal_length
# number of records, max of each, min of each, mean of each, printout of all items

# file to create summary of petal_width
# number of records, max of each, min of each, mean of each, printout of all items

# histogram sepal_length

# histogram sepal_width

# histogram petal_length

# histogram petal_width

# scatter sepal_l vs sepal_w

# scatter sepal_l vs petal_l

# scatter sepal_l vs petal_w

# scatter petal_l vs petal_w

# scatter petal_l vs sepal_w

# scatter sepal_w vs petal_w
