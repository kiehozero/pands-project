# A program to create scatter plots by species for either sepal or petal data, dependent on user selection

import matplotlib.pyplot as plt
import os.path
import pandas as pd

# file read and conversion to numPy array
iris_csv = pd.read_csv("iris.csv")

# creates a filtered dataset for each variable, method came from the Tutorials Point link in the README
set_data = iris_csv[iris_csv["species"]=="setosa"]
ver_data = iris_csv[iris_csv["species"]=="versicolor"]
vir_data = iris_csv[iris_csv["species"]=="virginica"]

# input for user to select which part they wish to see
userInput = input("Select a flower part to view ('sepal' or 'petal'): ")
if userInput == "sepal" or userInput == "petal":
    # x and y variables for each set, definitely could loop the creation of these
    x_set = set_data[f"{userInput}_length"]
    y_set = set_data[f"{userInput}_width"]
    x_ver = ver_data[f"{userInput}_length"]
    y_ver = ver_data[f"{userInput}_width"]
    x_vir = vir_data[f"{userInput}_length"]
    y_vir = vir_data[f"{userInput}_width"]

    # one scatter per species, plotted on a single chart
    # the colour selection was chosen using the Color Hex colour-blindness guide in the README
    plt.scatter(x_set,y_set, marker="x", color="#d55e00", label="setosa")
    plt.scatter(x_ver,y_ver, marker="o", color="#0072b2", label="versicolor")
    plt.scatter(x_vir,y_vir, marker="^", color="#f0e442", label="virginica")
    plt.legend(title="Species")
    plt.xlabel("Length")
    plt.ylabel("Width")
    plt.title(label=f"Comparison of {userInput} variables of three iris species", loc="center")

    # saves a filename that includes the user's selected part name to a child directory of the current directory
    # this method of generating a unique filename and saving it to a separate location both came from a StackOverflow article in the README
    filename = f"scatter_{userInput}.png"
    path = "./outputs/"
    filepath = os.path.join(path, filename)
    plt.savefig(filepath)
else:
    print("Please type either 'petal' or 'sepal'.")
