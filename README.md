# pands-project
A repository for the final project in GMIT Programming and Scripting 2022

# Dataset background

Background, information, general findings, mention the fact that one of the best ways of distinguishing the species isn't actually using petal or sepal data at all, but seed data (see article here https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5), proving the cardinal rule that correlation does not equal causation, and just because a parttern between variables has been detected, it does not necessarily mean that any of those variables or the relationships between them caused it

# Methodology and working notes

# Bugfixes
1. The first bug I encountered was when I was attempting to plot from a CSV file. the csv.reader() function was bringing in the lengths and widths as strings instead of floating-point numbers, so it wasn't plotting the points in value order, but rather in the order that each entry was within the CSV file. I didn't find an exact solution to rectify this in csv.reader(), but going to a basic [matplotlib tutorial](https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib) provided the read_csv() that corrected the problem.

# References

For isolating specific columns in a numPy array: https://www.statology.org/numpy-get-column/
For reading CSV files in matplotlib: https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib
General matplotlib basics: https://www.w3schools.com/python/matplotlib_intro.asp
For plotting items by group: https://www.w3schools.com/python/matplotlib_scatter.asp
For filtering with pandas: https://www.tutorialspoint.com/filter-the-rows-python-pandas and https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
Subplots: https://www.geeksforgeeks.org/plot-multiple-plots-in-matplotlib/
Context on dataset: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
Colour-blind-friendly colour palette: https://www.color-hex.com/color-palette/49436
Matplotlib docs for general function and parameter queries: https://matplotlib.org/3.5.1/index.html