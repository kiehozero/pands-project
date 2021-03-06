# A program that creates a histogram for each variable and plots each species on the same axis

import matplotlib.pyplot as plt
import numpy as np
import os.path
import pandas as pd

# file read and conversion to numPy array
iris_csv = pd.read_csv("iris.csv")
iris_csv = np.array(iris_csv)

# creates a filter for each variable, method came from the Tutorials Point link in the README
set_filter = iris_csv[:,4]=="setosa"
ver_filter = iris_csv[:,4]=="versicolor"
vir_filter = iris_csv[:,4]=="virginica"

# uses above filter to create standalone dataset for each variable
set_data = iris_csv[set_filter]
ver_data = iris_csv[ver_filter]
vir_data = iris_csv[vir_filter]

# input for user to select which variable they wish to see, prints the same message if the input is not an integer, or not between 0 and 3
try:
    userInput = int(input("Select a variable from the list to view its distribution (0: sepal length, 1: sepal width, 2: petal length, 3: petal width): "))
    if userInput < 0:
        print("Please choose a number between 1 and 4")
    elif userInput >= 4:
        print("Please choose a number between 1 and 4")
    else:
        # one histogram per species, plotted on a single chart
        plt.hist(set_data[0:,userInput], alpha=0.5, edgecolor="black", label="setosa")
        plt.hist(ver_data[0:,userInput], alpha=0.5, edgecolor="blue", label="versicolor")
        plt.hist(vir_data[0:,userInput], alpha=0.5, edgecolor="green", label="virginica")

        # a dictionary of variable names for use in the title of the plot amd the saved filename
        # if you want these in the same order as in distribution.py, you'll need to add headers back into the filtered items, then you'll be able to reference
        varIndex = {
            0: "sepal_length",
            1: "sepal_width",
            2: "petal_length",
            3: "petal_width"
            }

        # saves a filename that includes the user's selected variable name (from the dictionary above) to a child directory of the current directory
        # this method of generating a unique filename and saving it to a separate location both came from a StackOverflow article in the README
        filename = f"hist_{varIndex[userInput]}.png"
        path = "./outputs/"
        filepath = os.path.join(path, filename)
        plt.title(f"Distribution of {varIndex[userInput]} by species")
        plt.legend()
        plt.savefig(filepath)

# visited the Python docs link in the README for the exact error syntax
except ValueError:
    print("Please choose a number between 1 and 4")