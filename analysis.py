# Main file for performing analysis

# 1. Output a summary of each variable to a single text file
# 2. Save a histogram of each variable to png files
# 3. Output a scatter plot for each pair of variables
# 4. Performs any other analysis you think is appropriate
# The last point is what will make the project stand out, the first three are the minimum requirements

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# file read and conversion to numPy array
iris_csv = pd.read_csv("iris.csv")

# creates a set filter for each variable
set_filter = iris_csv["species"]=="setosa"
ver_filter = iris_csv["species"]=="versicolor"
vir_filter = iris_csv["species"]=="virginica"

# uses above filter to create standalone dataset for each variable
set_data = iris_csv[set_filter]
ver_data = iris_csv[ver_filter]
vir_data = iris_csv[vir_filter]

# CREATION OF SCATTER TO COMPARE PETAL VARIABLES

# x and y variables for each set, definitely could loop the creation of these
x_set = set_data["petal_length"]
y_set = set_data["petal_width"]
x_ver = ver_data["petal_length"]
y_ver = ver_data["petal_width"]
x_vir = vir_data["petal_length"]
y_vir = vir_data["petal_width"]

# can plot multiple items in one file

plt.scatter(x_set,y_set, marker="x", color="#d55e00", label="setosa")
plt.scatter(x_ver,y_ver, marker="o", color="#0072b2", label="versicolor")
plt.scatter(x_vir,y_vir, marker="^", color="#f0e442", label="virginica")
plt.legend(title="Species")
plt.title(label="Comparison of petal variables of three iris species", loc="center")
plt.show()
# plt.savefig(FILENAME HERE)

# should there be a single function for all scatters, with the inputs being the required ranges rather than creating new sets 
# over and over, could then make a function where the two axes variables are passed in from a user input

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
