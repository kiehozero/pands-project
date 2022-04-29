# A program that prints a summary of key information about this dataset to a .txt file

import matplotlib.pyplot as plt
import os.path
import pandas as pd
import seaborn as sns

# file read
iris_csv = pd.read_csv("iris.csv")

# file to write summary data to
file_to = "outputs/summary.txt"

# number of records, max, min, mean, range, printout of all items, most of these are built-in functions in python, could be worth exploring numpy/math functions

# standalone dataset for each variable, method came from the Tutorials Point link in the README
set_data = iris_csv[iris_csv["species"]=="setosa"]
ver_data = iris_csv[iris_csv["species"]=="versicolor"]
vir_data = iris_csv[iris_csv["species"]=="virginica"]

max_ver = str(max(ver_data["sepal_width"]))

with open(file_to,"at") as f:

    f.write(f"{max_ver}")

# with open(file_to,"r") as f:

#    living = f.readline()
#    print(living)
# )