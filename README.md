# pands-project
A repository for the final project in GMIT Programming and Scripting 2022

# Dataset background



# Methodology and working notes

# Bugfixes
1. The first bug I encountered was when I was attempting to plot from a CSV file. the csv.reader() function was bringing in the lengths and widths as strings instead of floating-point numbers, so it wasn't plotting the points in value order, but rather in the order that each entry was within the CSV file. I didn't find an exact solution to rectify this in csv.reader(), but going to a basic [matplotlib tutorial](https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib) provided the read_csv() that corrected the problem.

# References

For isolating specific columns in a numPy array: https://www.statology.org/numpy-get-column/
For reading CSV files in matplotlib: https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib
For plotting items by group: https://www.w3schools.com/python/matplotlib_scatter.asp
For filtering with pandas: https://www.tutorialspoint.com/filter-the-rows-python-pandas