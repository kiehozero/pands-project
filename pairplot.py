# A program that uses seaborn to re-create an example of iris data analysis found on the dataset's Wikipedia page (link in README)
# lines 12 and 13 are all that are required to run this in the same manner as the seaborn tutorial in the README

import matplotlib.pyplot as plt
import os.path
import pandas as pd
import seaborn as sns

# file read and conversion to numPy array
iris_csv = pd.read_csv("iris.csv")

sns.pairplot(data=iris_csv, hue="species")
plt.legend()

# saves a filename that includes the user's selected variable name to a child directory of the current directory
# this method of generating a unique filename and saving it to a separate location both came from a StackOverflow article in the README
filename = "pairplot.png"
path = "./outputs/"
filepath = os.path.join(path, filename)
plt.savefig(filepath)