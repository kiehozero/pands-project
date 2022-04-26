# Programming and Scripting Assignment on Fisher's Iris Data
This repository contains the scripts, output files, original datasets and supporting documentation for my project submission to the Programming and Scripting module of the HDip Computing and Analytics course at the [Atlantic Technological University](https://www.atu.ie/), Ireland.

## The task

The research task was to use Python to research a given dataset using Python libraries of your choosing, whether covered in the course or otherwise, and document the results arising. 

## Dataset background and previous findings

This project is based on the Iris flower data set, prepared by Roland Fisher, a British biologist and statistician - amongst other things - in 1936. The dataset is considered a starting point for budding data analysts and statisticians, utilising a number of methods and programming languages. While the dataset was accessed for this project from the University of California at Irvine's [Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris) (1988), it can be accessed from countless GitHub repositories for academic projects just like this one. Indeed, such is the popularity of the dataset as a training tool for all manner of data-related disciplines, it can be difficult to find much background information, as the most prominent search results almost exclusively concern the dataset's value as a training aid, rather than its initial purpose.

Nevertheless, one article by [Yong Cui](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5) (2020) did offer some context, including that Fisher obtained the data from a Dr. Edgar Anderson, a notable American botanist who collected the data in southern Quebec. Interestingly, while the object of the research was for Fisher to write a function that allowed biologists to correctly observe the iris species given the length and width of petals and sepals, Cui points out that Anderson, "published a manuscript titled “The Species Problems in Iris” to discuss the discrimination of Iris species... Anderson noted that the morphology of the seeds of these flowers was more informative [than the variables already gathered]."

There is also an argument, summarised nicely by Timothée Poisot at [Armchair Ecology](https://armchairecology.blog/iris-dataset/), that the dataset be retired from future use due to its initial publication in a eugenics journal during the mid-1930s, and that, "parading it around in 2020 is an unacceptable endorsement of a repulsive (but still very much alive) way to subsume science under ideology" (Poisot, 2020).

The data itself consists of the length and width of two separate parts of an iris flower, the petal and the sepal. Fisher and his research partner Anderson measured 150 individuals plants, and these are divided evenly between three species of iris: setosa, versicolor and virginica. The overall conclusion of the data as presented by Fisher was that while one species, iris setosa, can be distinguished from the others by assessing any of the four variables presented, there are varying degrees of uncertainty between iris versicolor and iris virginica.

## Findings 

As expected, there will be no ground-breaking contribution to the fields of botany or biology within this GitHub repository. Within my initial investigations, a [scatter plot](https://en.wikipedia.org/wiki/Iris_flower_data_set) on the dataset's Wikipedia page provided a compact summary of this data, which I have attempted to reproduce in the [pairplot](pairplot.py) program. >>> Description of seaborn process, this was actually the last task I accomplished.

findings arising from [analysis](analysis.py)

findings arising from [distribution](distribution.py)


## Software Packages

All analysis within this project was undertaken using Python, specifically the below libraries:
- [matplotlib](https://matplotlib.org/) - The website describes this library as, "a comprehensive library for creating static, animated, and interactive visualizations in Python."
- [numPy](https://numpy.org/pand) - The website describes this library as, "The fundamental package for scientific computing with Python."
- [pandas](https://pandas.pydata.org/) - The website describes this library as, "a fast, powerful, flexible and easy to use open source data analysis and manipulation tool."
- [seaborn](https://seaborn.pydata.org/) - The website describes this library as, "a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

## Operation of code
- analysis.py - main script to fulfil project requirements
- distribution.py - explanation of box-and-whisker, interactive element, ease of using seaborn
- pairplot.py - This script is purely a demonstration of previous analysis done on this dataset, and my attempt to replicate it using the seaborn library.

## Bug and fixes
1. The first bug I encountered was when I was attempting to plot from a CSV file. the csv.reader() function was bringing in the lengths and widths as strings instead of floating-point numbers, so it wasn't plotting the points in value order, but rather in the order that each entry was within the CSV file. I didn't find an exact solution to rectify this in csv.reader(), but going to a basic [matplotlib tutorial](https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib) provided the read_csv() that corrected the problem.
2. "No handles with labels found to put in legend" - doesn't seem to affect the operation of pairplot.py

## Potential improvements

## References

For isolating specific columns in a numPy array: https://www.statology.org/numpy-get-column/
For reading CSV files in matplotlib: https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib
General matplotlib basics: https://www.w3schools.com/python/matplotlib_intro.asp
For plotting items by group: https://www.w3schools.com/python/matplotlib_scatter.asp
For filtering with pandas: https://www.tutorialspoint.com/filter-the-rows-python-pandas and https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
Subplots: https://www.geeksforgeeks.org/plot-multiple-plots-in-matplotlib/
Context on dataset: Yong Cui, https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5  (2020)
Colour-blind-friendly colour palette: https://www.color-hex.com/color-palette/49436
Matplotlib docs for general function and parameter queries: https://matplotlib.org/3.5.1/index.html
Seaborn tutorial:
Host repo for data: https://archive.ics.uci.edu/ml/datasets/iris (1988)
Iris debate: Poissot, T. (2020), [Armchair Ecology](https://armchairecology.blog/iris-dataset/
[matplotlib](https://matplotlib.org/)
[numPy](https://numpy.org/pand)
[Pandas](https://pandas.pydata.org/)
[seaborn](https://seaborn.pydata.org/)