import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# file read and conversion to numPy array
iris_csv = pd.read_csv("iris.csv")

sns.pairplot(data=iris_csv, hue="species")
plt.legend()
plt.show()