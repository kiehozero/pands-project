# A program that uses seaborn to re-create an example of iris data analysis found on the dataset's Wikipedia page (link in README)

import matplotlib.pyplot as plt
import os.path
import pandas as pd
import seaborn as sns

# file read and conversion to numPy array
iris_csv = pd.read_csv("iris.csv")

sns.pairplot(data=iris_csv, hue="species")
plt.legend()
filename = "pairplot.png"
path = "./images/"
filepath = os.path.join(path, filename)
plt.savefig(filepath)