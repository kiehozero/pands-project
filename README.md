# Programming and Scripting Assignment on Fisher's Iris Data
This repository contains the scripts, output files, original datasets and supporting documentation for my project submission to the Programming and Scripting module of the HDip Computing and Analytics course at the [Atlantic Technological University](https://www.atu.ie/), Ireland.

## The task

The research task was to use Python to research a given dataset using Python libraries of your choosing, whether covered in the course or otherwise, and document the results arising. 

## Dataset background and previous findings

This project is based on the Iris flower data set, prepared by Roland Fisher, a British biologist and statistician - amongst other things - in 1936. The dataset is considered a starting point for budding data analysts and statisticians, utilising a number of methods and programming languages. While the dataset was accessed for this project from the University of California at Irvine's [Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris) (1988), it can be accessed from countless GitHub repositories for academic projects just like this one. Indeed, such is the popularity of the dataset as a training tool for all manner of data-related disciplines, it can be difficult to find much background information, as the most prominent search results almost exclusively concern the dataset's value as a training aid, rather than its initial purpose.

Nevertheless, one article by [Yong Cui](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5) (2020) did offer some context, including that Fisher obtained the data from a Dr. Edgar Anderson, a notable American botanist who collected the data in southern Quebec. Interestingly, while the object of the research was for Fisher to write a function that allowed biologists to correctly observe the iris species given the length and width of petals and sepals, Cui points out that Anderson, "published a manuscript titled “The Species Problems in Iris” to discuss the discrimination of Iris species... Anderson noted that the morphology of the seeds of these flowers was more informative [than the variables already gathered]."

There is also an argument, summarised nicely by Timothée Poisot at [Armchair Ecology](https://armchairecology.blog/iris-dataset/), that the dataset be retired from future use due to its initial publication in a eugenics journal during the mid-1930s, and that, "parading it around in 2020 is an unacceptable endorsement of a repulsive (but still very much alive) way to subsume science under ideology" (Poisot, 2020).

The data itself consists of the length and width of two separate parts of an iris flower, the petal and the sepal. Fisher and his research partner Anderson measured 150 individuals plants, and these are divided evenly between three species of iris: setosa, versicolor and virginica. The overall conclusion of the data as presented by Fisher was that while one species, iris setosa, can be distinguished from the others by assessing any of the four variables presented, there are varying degrees of uncertainty between iris versicolor and iris virginica.

## Methodology and Findings

As expected, there will be no ground-breaking contribution to the fields of botany or biology within this GitHub repository. Within my initial investigations, a [scatter plot](https://en.wikipedia.org/wiki/Iris_flower_data_set) on the dataset's Wikipedia page provided a compact summary of this data, which I have attempted to reproduce in the [pairplot](pairplot.py) program. >>> Description of seaborn process, this was actually the last task I accomplished.


### Findings arising from [histogram](histogram.py)

Using guidance from the initial project brief, I attempted to create a histogram that would display the distribution of measurements by variable. I used the pandas read_csv function and the numPy array function, and then created a unique dataset for each species by filtering and slicing the original dataset, and assigning this to a new variable. A user-inputted selection determines the variable to be plotted, a filename is determined based on this selection, and os.path.join is used to add the completed plot to the images sub-folder. The histograms are probably best used when plotting a single variable, or multiple-variables that do not overlap, but I found that I had to customise the settings of the plots (see the Geeksforgeeks article in the Formatting Plots section of the References below) to get overlapping data even remotely visible, particular when plotting sepal data.

### Findings arising from [distribution](distribution.py)

>>> Creating a scatter graph largely resolved the visibility issues that the [histogram](histogram.py) presented

### Findings arising from [scatter](scatter.py)

A scatter graph allowed for the plotting of measurements based on both dimensions, as well as all unique measurements to be displayed
>>> removed numPy from above so could use column references instead of slicing columns after the header and making the more code less difficult to read. Similar to [histogram](histogram.py), uses an input to determine whether to scatter the petal or sepal variables
>>> setosa easily identifiable based on petals, with minimal overlap between virginica and versicolor, strong correlation between length and width of latter two, not so much for setosa. In contrast, setosa shows much stronger correlation between sepal length and width, while virginica and versicolor not only show slightly less correlation between length and width, but they also show significant overlap in these areas. On the whole virginica is larger, with about 25% of measurements larger than any of the versicolor measurements



### Findings arising from [summary](summary.py)

>>>

### Findings arising from [pairplot](pairplot.py)

>>>

## Software Packages

All analysis within this project was undertaken using Python, specifically the below libraries:
- [matplotlib](https://matplotlib.org/) - The website describes this library as, "a comprehensive library for creating static, animated, and interactive visualizations in Python."
- [numPy](https://numpy.org/pand) - The website describes this library as, "The fundamental package for scientific computing with Python."
- [pandas](https://pandas.pydata.org/) - The website describes this library as, "a fast, powerful, flexible and easy to use open source data analysis and manipulation tool."
- [seaborn](https://seaborn.pydata.org/) - The website describes this library as, "a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

## Operation of code
- [analysis](analysis.py) - main script to fulfil project requirements
- [distribution](distribution.py) - explanation of box-and-whisker, interactive element, ease of using seaborn
- [pairplot](pairplot.py) - This script is purely a demonstration of previous analysis done on this dataset, and my attempt to replicate it using the seaborn library. Utilises pandas to prepare data, seaborn to access more advanced visuals, and matplot to actually create them

## Bug and fixes
1. The first bug I encountered was when I was attempting to plot from a CSV file. the csv.reader() function was bringing in the lengths and widths as strings instead of floating-point numbers, so it wasn't plotting the points in value order, but rather in the order that each entry was within the CSV file. I didn't find an exact solution to rectify this in csv.reader(), but going to a basic [matplotlib tutorial](https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib) provided the read_csv() function that corrected the problem.
2. When the [pairplot](pairplot.py) program runs, everything operates as planned but the warning message "No handles with labels found to put in legend" is printed to the terminal. When I got this on other plots it was because I had added a legend but not given any labels; adding labels to the seaborn pairplot function results in an unexepected keyword argument error, so I have reverted the code back to the earlier warning message instead.

## Potential improvements
1. The analysis in [distribution](distribution.py) could be developed further by plotting the count of measurements as a size variable. At present, if the length and width of two or more measurements are identical, they are plotted in the same position. Using the count as a size variable here on a bubble chart would display clustered measurements in a more dynamic way than simply overlapping them.

## References

### Isolating specific columns in a numPy array:
- Zach (2021) How to Get Specific Column from NumPy Array. Statology. URL: https://www.statology.org/numpy-get-column/

### Reading CSV files in matplotlib:
- Tutorial Points (n.d.) Plot data from CSV file with Matplotlib. URL: https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib
- W3Schools (n.d.) Matplotlib Tutorial. URL: https://www.w3schools.com/python/matplotlib_intro.asp

### Plotting items by group:
- W3Schools (n.d.) Matplotlib Scatter. URL: https://www.w3schools.com/python/matplotlib_scatter.asp

### Filtering with pandas: 
- Python and R Tips (2018) How To Filter Pandas Dataframe By Values of Column? URL: https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
- Tutorials Point (n.d.) Filter the rows – Python Pandas. URL: https://www.tutorialspoint.com/filter-the-rows-python-pandas

### Subplots:
- GeeksforGeeks (2021) Plot multiple plots in Matplotlib. URL: https://www.geeksforgeeks.org/plot-multiple-plots-in-matplotlib/

### Formatting plots:
- GeeksforGeeks (2020) How to plot two histograms together in Matplotlib? URL: https://www.geeksforgeeks.org/how-to-plot-two-histograms-together-in-matplotlib/
- Matplotlib (n.d.) matplotlib.pyplot.ylabel — Matplotlib 3.5.1 documentation. URL: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html

### Colour-blind-friendly colour palette: 
- Color Hex (n.d.) color-blind-friendly Color Palette. URL: https://www.color-hex.com/color-palette/49436

### Seaborn tutorial
- AskPython (2020) Python Seaborn Tutorial. URL: https://www.askpython.com/python-modules/python-seaborn-tutorial

### Saving files in a new location:
- Stack Overflow (2012) filesystems - Python: how do I save a file in a different directory? URL: https://stackoverflow.com/questions/13825719/python-how-do-i-save-a-file-in-a-different-directory

### Data source and context:
- Cui, Y. (2020) The Iris Dataset — A Little Bit of History and Biology. Medium. URL: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
- Machine Learning Repository: Iris Data Set (1988) University of California at Irvine. URL: https://archive.ics.uci.edu/ml/datasets/iris
- Poissot, T. (2020) It’s time to retire the iris dataset. Armchair Ecology. URL: https://armchairecology.blog/iris-dataset/

### General documentation:
- Matplotlib (n.d.) Matplotlib 3.5.1 documentation. URL: https://matplotlib.org/3.5.1/index.html
- NumPy (n.d.) Overview — NumPy v1.19 Manual. URL: https://numpy.org/doc/stable/
- Pandas (n.d.) pandas 1.0.1 documentation. URL: https://pandas.pydata.org/docs/
- Seaborn (2012) statistical data visualization — seaborn 0.9.0 documentation. URL: https://seaborn.pydata.org/