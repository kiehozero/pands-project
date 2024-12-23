# Programming and Scripting Assignment on Fisher's Iris Data

This repository contains the scripts, output files, original datasets and supporting documentation for my project submission to the Programming and Scripting module of the HDip Computing and Analytics course at the [Atlantic Technological University](https://www.atu.ie/), Ireland.

## The task

The research task was to use Python to research a given dataset using Python libraries of your choosing, whether covered in the course or otherwise, and document the results arising. 

## Dataset background and previous findings

This project is based on the Iris flower data set, prepared by Roland Fisher, a British biologist and statistician - amongst other things - in 1936. The dataset is considered a starting point for budding data analysts and statisticians, utilising a number of methods and programming languages. While the dataset was accessed for this project from the University of California at Irvine's [Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris) (1988), it can be accessed from countless GitHub repositories for academic projects just like this one. Indeed, such is the popularity of the dataset as a training tool for all manner of data-related disciplines, it can be difficult to find much background information, as the most prominent search results almost exclusively concern the dataset's value as a training aid, rather than its initial purpose.

Nevertheless, one article by [Yong Cui](https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5) (2020) did offer some context, including that Fisher obtained the data from a Dr. Edgar Anderson, a notable American botanist who collected the data in southern Quebec. Interestingly, while the object of the research was for Fisher to write a function that allowed biologists to correctly observe the iris species given the length and width of petals and sepals, Cui points out that Anderson, "published a manuscript titled “The Species Problems in Iris” to discuss the discrimination of Iris species... Anderson noted that the morphology of the seeds of these flowers was more informative [than the variables already gathered]."

There is also an argument, summarised nicely by Timothée Poisot at [Armchair Ecology](https://armchairecology.blog/iris-dataset/), that the dataset be retired from future use due to its initial publication in a eugenics journal during the mid-1930s, and that, "parading it around in 2020 is an unacceptable endorsement of a repulsive (but still very much alive) way to subsume science under ideology" (Poisot, 2020).

The data itself consists of the length and width of two separate parts of an iris flower, the petal and the sepal. Fisher and his research partner Anderson measured 150 individuals plants, and these are divided evenly between three species of iris: setosa, versicolor and virginica. The overall conclusion of the data as presented by Fisher was that while one species, iris setosa, can be distinguished from the others by assessing any of the four variables presented, there are varying degrees of uncertainty between iris versicolor and iris virginica.

## Working Notes

### Findings

As expected, there will be no ground-breaking contribution to the fields of botany or biology within this GitHub repository. Within my initial investigations, a [scatter plot](https://en.wikipedia.org/wiki/Iris_flower_data_set) on the dataset's Wikipedia page provided a compact summary of this data, which I have attempted to reproduce in the [pairplot](pairplot.py) program.

The various charts contained show that the subspecies setosa is easily identifiable based on petals, with minimal overlap between virginica and versicolor. This is also strong correlation between length and width of latter two, with weaker correlation for setosa. In contrast, setosa shows much stronger correlation between sepal length and width, while virginica and versicolor not only show slightly less correlation between length and width, but they also show significant overlap in these areas, to be discussed in greater detail below. On the whole virginica is larger, with about 25% of measurements larger than any of the versicolor measurements. Subsequently, as a measure of identifying the species, it would appear that the variables most useful for this task are, in descending order, the petal length, the petal width, the sepal length, and finally the sepal width as the least reliable variable.

### [Histogram](histogram.py) methodology

Using guidance from the initial project brief, I attempted to create a histogram that would display the distribution of measurements by variable. I used the pandas read_csv function and the numPy array function, and then created a unique dataset for each species by filtering and slicing the original dataset, and assigning this to a new variable. A user-inputted selection determines the variable to be plotted, a filename is determined based on this selection, and os.path.join is used to add the completed plot to the outputs sub-folder.

The histograms are probably best used when plotting a single variable, or multiple-variables that do not overlap, but I found that I had to customise the settings of the plots (see the Geeksforgeeks article in the Formatting Plots section of the References below) to get overlapping data even remotely visible, particularly when plotting sepal data. Overlapping ranges on the histograms are of the most detriment where data is most concentrated, in the case of sepal width this is in the 2.5cm-3.5cm range.

### [Distribution](distribution.py) methodology

Creating a box-and-whisker graph largely resolved the visibility issues that the histogram presented, displaying the three species without overlap on a variable-by-variable basis. The inspiration for this view came from a work project I was involved in recently, and a quick Google found that box-and-whisker plots were a fairly standard graph within seaborn. Seaborn is both a package that has plenty of simple tutorials online, and also was not covered in the course material. After this, and as with the histogram, a filename is determined based on the user selection, and os.path.join is used to add the completed plot to the outputs sub-folder.

Similar to the histogram this program uses an input to determine the displayed variable, but packages the processes of plotting and saving the graphs within a function. Unlike the histogram, the box-and-whisker can sub-divide data based using a third variable, in this case the species, so while much of the underlying code is similar, there is no need to separate the data into three subsets before plotting onto separate charts. The boxplot function simply takes this in as an axis variable, allowing complete separation between data, but still allowing for easy comparison due to the lack of overlaid information. 

The petal charts confirm the distinct dimensions of the setosa mentioned above, as well as the slight overlap between virginia and versicolor petals. The box-and-whisker also plots outlying data as individual points; setosa contains the most of these, but they still fall relatively close to the other setosa measurements, and never overlap within the expected ranges of the other species. The sepal charts more cleanly display the significant overlaps between species than the histogram does. This is particularly helpful for sepal width, where versicolor occupies a range between 2.0cm and 3.4cm, while virginica lies between 2.2cm-3.8cm range; in the histogram this resulted in a plot that was difficult to read. Crucially, the box-and-whisker displays inter-quartile data as the focal box, with the remaining statistically-significant range as the whiskers, allowing users to pinpoint the central range of each species, reducing the ranges down to 2.5cm-3.0cm and 2.7cm-3.2cm respectively. 

### [Scatter](scatter.py) methodology

Unlike either the histogram or the box-and-whisker chart, a scatter graph allows for the plotting of measurements based on multiple dimensions, as well more unique measurements to be displayed together. This view generally provides a better view of data ranges where there may be overlapping measurements within the virginica and versicolor sets, provided you choose the icons and colours carefully to avoid conflicts. The disadvantage of this view is that it is initially difficult to establish the central quartile of each dataset, unlike the boxplot where it is a core feature of the function.

Similar to the histogram program, the scatter program works by filtering the original dataset and creating a new one for each species. A user input then determines whether to create a scatter or sepal or petal data, and a length and width dataset for each species is creating using the input to determine which column to select. The two datasets for each species are then added to a scatter plot, and the three plots are added to the same visual. Lastly, a filename is determined based on the user selection, and os.path.join is used to add the completed plot to the outputs sub-folder.

### [Summary](summary.py) methodology

This program offers a selection of numerical data relevant to the dataset, segmented by species, using Python's built-in mathematical functions, to serve as a companion piece to the various data visualisations. The program is mostly a combination of the existing filtering and slicing options used in the earlier scripts, as well as the basic file-read and file-write techniques that were discussed in week 7 of the course. There is a definitely a million ways that this file can be optimised but I wrote it at midnight on the 29th April so it is what it is, I don't think I've ever used print as much in my life as messing around trying to get this to print out basic information.

### [Pair-plot](pairplot.py) methodology

This script is purely a demonstration of [previous analysis](https://en.wikipedia.org/wiki/Iris_flower_data_set#/media/File:Iris_dataset_scatterplot.svg) done on this dataset, and my attempt to replicate it using the seaborn library. Luckily the seaborn documentation in the References section includes this exact charts as one of the first examples, and it requires under ten lines of code to prepare. As it stands, this plot contains all of the previous visuals that were contained in the scatter and histogram output, and using even less code to do so.

The practice of organising sixteen charts, with variable assigned along master x and y axes is an extremely effective way of viewing all data plotted together. It becomes very easy to spot which of the various variable combinations display the most or least correlation, and a simple line graph is used in place of scatter graphs where a variable would be otherwise plotted against each other (see the central top-left to bottom-right sequence). The one drawback to this view is that a dataset any larger than this, or containing more variables, might suffer from trying to fit too much into a small space.

## Software Packages

All analysis within this project was undertaken using Python, specifically the below libraries:
- [matplotlib](https://matplotlib.org/) - The website describes this library as, "a comprehensive library for creating static, animated, and interactive visualizations in Python."
- [numPy](https://numpy.org/pand) - The website describes this library as, "The fundamental package for scientific computing with Python."
- [pandas](https://pandas.pydata.org/) - The website describes this library as, "a fast, powerful, flexible and easy to use open source data analysis and manipulation tool."
- [seaborn](https://seaborn.pydata.org/) - The website describes this library as, "a Python data visualization library based on matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics."

## Bugs and fixes

1. The first bug I encountered was when I was attempting to plot from a CSV file. the csv.reader() function was bringing in the lengths and widths as strings instead of floating-point numbers, so it wasn't plotting the points in value order, but rather in the order that each entry was within the CSV file. I didn't find an exact solution to rectify this in csv.reader(), but going to a basic [matplotlib tutorial](https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib) provided the read_csv() function that corrected the problem.

2. When the [pairplot](pairplot.py) program runs, everything operates as planned but the warning message "No handles with labels found to put in legend" is printed to the terminal. When I got this on other plots it was because I had added a legend but not given any labels; adding labels to the seaborn pairplot function results in an unexepected keyword argument error, so I have reverted the code back to the earlier warning message instead.

3. Towards the end of the project I noticed that I had not included any error-handling in the user inputs. To handle any non-integer values I wrapped the existing code in try/except blocks, and added if/elif/else statements to handle any out-of-range integers. I have omitted this from the pairplot file as this does not require user input.

## Potential improvements

1. The analysis in [scatter](scatter.py) could be developed further by plotting the count of measurements as a size variable. At present, if the length and width of two or more measurements are identical, they are plotted in the same position. Using the count as a size variable here on a bubble chart would display clustered measurements in a more dynamic way than simply overlapping them.

2. I wanted to use a loop in [distribution](distribution.py) to loop through the varIndex range, thus creating all four charts simultaneously rather than asking a user to select a particular chart. I attempted to create this but could only get the code the generate four charts, with the first containing only the first variable, but with the fourth containing all four variable. I have included the [png](outputs/dist_error.png) to better explain the output. I think looping all of these files would ultimately be preferable to a user than having to repeat the process multiple times.

## References

### Colour-blind-friendly colour palette

- Color Hex (n.d.) color-blind-friendly Color Palette. URL: https://www.color-hex.com/color-palette/49436

### Data source and context

- Cui, Y. (2020) The Iris Dataset — A Little Bit of History and Biology. Medium. URL: https://towardsdatascience.com/the-iris-dataset-a-little-bit-of-history-and-biology-fb4812f5a7b5
- Machine Learning Repository (1988) Iris Data Set. University of California at Irvine. URL: https://archive.ics.uci.edu/ml/datasets/iris
- Poissot, T. (2020) It’s time to retire the iris dataset. Armchair Ecology. URL: https://armchairecology.blog/iris-dataset/
- Wikipedia Contributors (2019) Iris flower data set. Wikipedia. URL: https://en.wikipedia.org/wiki/Iris_flower_data_set

### Error handling in Python

- Python Docs (n.d.) Built-in Exceptions — Python 3.8.2 documentation. URL: https://docs.python.org/3/library/exceptions.html

### File handling in Python

- W3schools (2019) Python File Write. URL: https://www.w3schools.com/python/python_file_write.asp

### Formatting plots

- GeeksforGeeks (2020) How to plot two histograms together in Matplotlib? URL: https://www.geeksforgeeks.org/how-to-plot-two-histograms-together-in-matplotlib/
- Matplotlib (n.d.) matplotlib.pyplot.ylabel — Matplotlib 3.5.1 documentation. URL: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylabel.html

### Filtering with pandas

- Python and R Tips (2018) How To Filter Pandas Dataframe By Values of Column? URL: https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
- Tutorials Point (n.d.) Filter the rows – Python Pandas. URL: https://www.tutorialspoint.com/filter-the-rows-python-pandas

### General documentation

- Matplotlib (n.d.) Matplotlib 3.5.1 documentation. URL: https://matplotlib.org/3.5.1/index.html
- NumPy (n.d.) Overview — NumPy v1.19 Manual. URL: https://numpy.org/doc/stable/
- Pandas (n.d.) pandas 1.0.1 documentation. URL: https://pandas.pydata.org/docs/
- Seaborn (2012) statistical data visualization — seaborn 0.9.0 documentation. URL: https://seaborn.pydata.org/

### Isolating specific columns in a numPy array
- Zach (2021) How to Get Specific Column from NumPy Array. Statology. URL: https://www.statology.org/numpy-get-column/

### Maths in Python

- GeeksforGeeks (2017) max() and min() in Python. URL: https://www.geeksforgeeks.org/max-min-python/
- GeeksforGeeks (2018) Python statistics | mean() function. URL: https://www.geeksforgeeks.org/python-statistics-mean-function/
- Stack Overflow. (n.d.) integer - Python how to remove decimal? URL: https://stackoverflow.com/questions/32669400/python-how-to-remove-decimal#32669460

### Plotting items by group

- W3Schools (n.d.) Matplotlib Scatter. URL: https://www.w3schools.com/python/matplotlib_scatter.asp

### Reading CSV files in matplotlib

- Tutorial Points (n.d.) Plot data from CSV file with Matplotlib. URL: https://www.tutorialspoint.com/plot-data-from-csv-file-with-matplotlib
- W3Schools (n.d.) Matplotlib Tutorial. URL: https://www.w3schools.com/python/matplotlib_intro.asp

### Saving files in a new location

- Stack Overflow (2012) filesystems - Python: how do I save a file in a different directory? URL: https://stackoverflow.com/questions/13825719/python-how-do-i-save-a-file-in-a-different-directory

### Seaborn tutorials

- AskPython (2020) Python Seaborn Tutorial. URL: https://www.askpython.com/python-modules/python-seaborn-tutorial
- Seaborn Documentation (n.d.). seaborn.boxplot — seaborn 0.11.1 documentation. URL: https://seaborn.pydata.org/generated/seaborn.boxplot.html

### Subplots

- GeeksforGeeks (2021) Plot multiple plots in Matplotlib. URL: https://www.geeksforgeeks.org/plot-multiple-plots-in-matplotlib/
