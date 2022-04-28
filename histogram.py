# A program that prints a summary of key information about this dataset to a .txt file

import matplotlib.pyplot as plt
import numpy as np
import os.path
import pandas as pd
import seaborn as sns

# file read and conversion to numPy array
iris_csv = pd.read_csv("iris.csv")
iris_csv = np.array(iris_csv)

# creates a set filter for each variable
set_filter = iris_csv[:,4]=="setosa"
ver_filter = iris_csv[:,4]=="versicolor"
vir_filter = iris_csv[:,4]=="virginica"

# uses above filter to create standalone dataset for each variable
set_data = iris_csv[set_filter]
ver_data = iris_csv[ver_filter]
vir_data = iris_csv[vir_filter]

# assigns each variable a value, with the user-selected item to be defined as the y-axis in the resulting box-and-whisker
# if you want these in the same order as in distribution.py, you'll need to add headers back into the filtered items, then you'll be able to ref them
varIndex = {
    0: "sepal_length",
    1: "sepal_width",
    2: "petal_length",
    3: "petal_width"
    }

# input for user to select which variable they wish to see
userInput = int(input("Select a variable from the list to view its distribution (0: sepal length, 1: sepal width, 2: petal length, 3: petal width): "))

plt.hist(set_data[0:,userInput])
plt.hist(ver_data[0:,userInput])
plt.hist(vir_data[0:,userInput])
plt.title(f"Distribution of {varIndex[userInput]} by species")
plt.legend()
plt.show()