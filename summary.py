# A program that prints a summary of key information about this dataset to a .txt file

import matplotlib.pyplot as plt
import os.path
import pandas as pd
import seaborn as sns

# file read and conversion to numPy array
iris_csv = pd.read_csv("iris.csv")

# number of records, max of each, min of each, mean of each, printout of all items, mnost of these are built-in functions in python, could be worth exploring numpy/math functions

# creates a set filter for each variable
set_filter = iris_csv[:,4]=="setosa"
ver_filter = iris_csv[:,4]=="versicolor"
vir_filter = iris_csv[:,4]=="virginica"

# uses above filter to create standalone dataset for each variable
set_data = iris_csv[set_filter]
ver_data = iris_csv[ver_filter]
vir_data = iris_csv[vir_filter]

print(max(ver_data))