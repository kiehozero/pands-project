# a file that allows users to plot the variable of their choosing into a chart that displays distribution of data by species, including quartile values

import matplotlib.pyplot as plt
import os.path
import pandas as pd
import seaborn as sns

# file read and conversion to numPy array
iris_csv = pd.read_csv("iris.csv")

# function to create and plot a box-and-whisker chart
def plotter(userInput):
    # needs error handling for values that aren't between 1 and 4, see previous lectures
    sns.boxplot(x="species", y=varIndex[userInput], data=iris_csv)
    # The split function is introduced to print the name of the variable without the underscore, the is used in both the y-axis label and the title
    splitName = varIndex[userInput].split("_")
    plt.ylabel(f"{splitName[0]} {splitName[1]}")
    plt.title(label=f"Distribution of {splitName[0]} {splitName[1]} by species")
    # saves a filename that includes the user's selected variable name to a child directory of the current directory
    # this method of generating a unique filename and saving it to a separate location both came from a StackOverflow article in the README
    filename = f"dist_{varIndex[userInput]}.png"
    path = "./images/"
    filepath = os.path.join(path, filename)
    plt.savefig(filepath)

# assigns each variable a value, with the user-selected item to be defined as the y-axis in the resulting box-and-whisker
varIndex = {
    1: "petal_length",
    2: "petal_width",
    3: "sepal_length",
    4: "sepal_width"
    }

# input for user to select which variable they wish to see
userInput = int(input("Select a variable from the list to view its distribution (1: petal length, 2: petal width, 3: sepal length, 4: sepal width): "))

plotter(userInput)
