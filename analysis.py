# Main file for performing analysis

# 1. Output a summary of each variable to a single text file
# 2. Save a histogram of each variable to png files
# 3. Output a scatter plot for each pair of variables
# 4. Performs any other analysis you think is appropriate
# The last point is what will make the project stand out, the first three are the minimum requirements
# Remember to comment and document all processes to show understanding of each step, especially where you may be following a tutorial

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# file read and conversion to numPy array
iris_csv = pd.read_csv("iris.csv")
iris_csv = np.array(iris_csv)

# CREATION OF SCATTER TO COMPARE PETAL VARIABLES

# creates a set filter for each variable
set_filter = iris_csv[:,4]=="setosa"
ver_filter = iris_csv[:,4]=="versicolor"
vir_filter = iris_csv[:,4]=="virginica"

# uses above filter to create standalone dataset for each variable
set_data = iris_csv[set_filter]
ver_data = iris_csv[ver_filter]
vir_data = iris_csv[vir_filter]

# x and y variables f, definitely could loop the creation of these
x_set = set_data[:,2]
y_set = set_data[:,3]
x_ver = ver_data[:,2]
y_ver = ver_data[:,3]
x_vir = vir_data[:,2]
y_vir = vir_data[:,3]

# can plot multiple items in one file

plt.scatter(x_set,y_set, marker="x", color="#d55e00", label="setosa")
plt.scatter(x_ver,y_ver, marker="o", color="#0072b2", label="versicolor")
plt.scatter(x_vir,y_vir, marker="^", color="#f0e442", label="virginica")
plt.legend(title="Species")
plt.title(label="Comparison of petal variables of three iris species", loc="center")
plt.show()
# plt.savefig(FILENAME HERE)

# CREATION OF SCATTER TO COMPARE SEPAL VARIABLES (sepal_length vs sepal_width)

# selects only sepal and species columns
sepal = iris_csv[1:, [0,1,4]]

# CREATION OF SCATTER TO COMPARE LENGTH VARIABLES (sepal_length vs petal_length)

# CREATION OF SCATTER TO COMPARE WIDTH VARIABLES (sepal_width vs petal_width)

# USE SUBPLOTS (README) TO PLOT SCATTERS ON ONE PAGE

# histogram sepal_length

# histogram sepal_width

# histogram petal_length

# histogram petal_width

# file to create summary of sepal_length
# number of records, max of each, min of each, mean of each, printout of all items

# file to create summary of sepal_width
# number of records, max of each, min of each, mean of each, printout of all items

# file to create summary of petal_length
# number of records, max of each, min of each, mean of each, printout of all items

# file to create summary of petal_width
# number of records, max of each, min of each, mean of each, printout of all items