# A program that prints a summary of key information about the dataset to a .txt file

import math
import pandas as pd
import statistics

# file read
iris_csv = pd.read_csv("iris.csv")

# file to write summary data to
file_to = "outputs/summary.txt"

# standalone dataset for each variable, method came from the Tutorials Point link in the README
set_data = iris_csv[iris_csv["species"]=="setosa"]
ver_data = iris_csv[iris_csv["species"]=="versicolor"]
vir_data = iris_csv[iris_csv["species"]=="virginica"]

# adds new datasets to a dictionary, enabling looping below
datasets = {
    "setosa": set_data,
    "versicolor": ver_data,
    "virginica": vir_data
}

# list of variables to loop through dataset columns
varIndex = [
    "petal_length",
    "petal_width",
    "sepal_length",
    "sepal_width"
    ]

# there is absolutely no way on earth this is the best way to retrieve the name of the dataset I'm using, but it is all I can think of
setname = ["setosa", "versicolor", "virginica"]

# the loop below goes through each 
with open(file_to, "wt") as f:

    counter = 0
    while counter < 3:
        for d in datasets.values():
            # uses value of counter to return value of setname list
            setInUse = setname[counter]
            print(counter)
            for v in varIndex:
                # displays column name and max value
                f.write(str(f"{setInUse} {v} - Max: "))
                f.write(
                    str(min(d[v]))
                )
                # displays column name and min value
                f.write(", Min: ")
                f.write(
                    str(max(d[v]))
                )
                # displays range value, see README reference for StackOverflow link on truncating decimals
                range = max(d[v]) - min(d[v])
                f.write(", Range: {:1f}".format(range))
                # displays mean value, see README reference for Geeksforgeeks article on mean function
                mean_ave = statistics.mean(d[v])
                f.write(f". Mean: {mean_ave}")
                f.write(f";\n")
            # adds new line to separate species
            f.write(f"\n")
            counter += 1
