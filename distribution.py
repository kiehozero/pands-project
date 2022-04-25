# a file that allows users to plot the variable of their choosing into a chart that displays distribution of data by species, including quartile values

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# file read and conversion to numPy array
iris_csv = pd.read_csv("iris.csv")

userInput = int(input("Select a variable from the list to view its distribution (1: petal_length, 2: petal_width, 3: sepal_length, 4: sepal_width): "))

# assigns each variable a value, with the user-selected item to be defined as the y-axis in the resulting box-and-whisker
varIndex = {
    1: "petal_length",
    2: "petal_width",
    3: "sepal_length",
    4: "sepal_width"
    }

# option to use swarmplot or boxplot here

sns.swarmplot(x="species", y=varIndex[userInput], data=iris_csv)
plt.title(label=f"Distribution of {varIndex[userInput]} by species")
plt.show()
# plt.savefig(FILENAME HERE)