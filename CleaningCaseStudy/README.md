# Data Cleaning Case Study - Life Expectancy

This Case Study may be found at the end of the [Cleaning Data in Python](https://www.datacamp.com/courses/cleaning-data-in-python) course provided by Data Camp.

The course itself used Gapminder data that showed life expectancy by country from 1800-1899, however for the project I am featuring here, I am using the complete data set found [here](https://www.gapminder.org/data/) by searching for "Life expectancy (years)."

## Table of Contents

* [Formatting Data](#formatting-data)
* [Importing Data](#importing-data)
* [Initial Exploration](#initial-exploration)
* [Visualizing Data](#visualizing-data)

## Formatting Data

The file of data from Gapminder is downloadable as .xlxs, however for this project I wanted to practice manipulating .csv files. So, in the .xlxs file, I replaces all the blank spaces with NaN to signify missing data points. Then, I saved the sheet as a .csv file. 

That file, found in this repository as **g18002016.csv**, contains life expectancy data by country from 1800 to 2016.

[Table of Contents](#table-of-contents)

## Importing Data

See [importing_data.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/importing_data.py) for importing process. 

[Table of Contents](#table-of-contents)

## Initial Exploration 

In order to help my workflow, I performed a few preliminary commands to show what the needs for cleaning were for this particular data set. 

```python
>>> print(data.shape)
(999, 218)
```

So, I know that the shape of the data frame is 999 rows by 218 columns. **_What are the column names?_**

```python 
>>> print(data.columns)
Index([u'Life expectancy', u'1800', u'1801', u'1802', u'1803', u'1804',
       u'1805', u'1806', u'1807', u'1808',
       ...
       u'2007', u'2008', u'2009', u'2010', u'2011', u'2012', u'2013', u'2014',
       u'2015', u'2016'],
      dtype='object', length=218)
```

As expected, the colums include the range of years in the data set. However, the first column, "Life expectancy" is probably the title for the kind of data given for each year by country. **_I printed the head next to see what the "Life expectancy" column contained._**

```python
>>> print(data.head(5))
         Life expectancy   1800   1801   1802   1803   1804   1805   1806  \
0               Abkhazia    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
1            Afghanistan  28.21  28.20  28.19  28.18  28.17  28.16  28.15   
2  Akrotiri and Dhekelia    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
3                Albania  35.40  35.40  35.40  35.40  35.40  35.40  35.40   
4                Algeria  28.82  28.82  28.82  28.82  28.82  28.82  28.82   

    1807   1808  ...    2007  2008  2009  2010  2011  2012  2013  2014  2015  \
0    NaN    NaN  ...     NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
1  28.14  28.13  ...    52.4  52.8  53.3  53.6  54.0  54.4  54.8  54.9  53.8   
2    NaN    NaN  ...     NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   NaN   
3  35.40  35.40  ...    76.6  76.8  77.0  77.2  77.4  77.5  77.7  77.9  78.0   
4  28.82  28.82  ...    75.3  75.5  75.7  76.0  76.1  76.2  76.3  76.3  76.4   

    2016  
0    NaN  
1  52.72  
```

Here, I found out that the first column, "Life expectancy," contains all of the country names included in the data set. **_In my data cleaning process, I will have to change the name of the first column to "Country Names" to accurately show what data is given in it._** Next, I printed basic descriptive statistics that may have been useful in the data cleaning process. 

```python
>>> print(data.describe())
             1800        1801        1802        1803        1804        1805  \
count  201.000000  201.000000  201.000000  201.000000  201.000000  201.000000   
mean    31.486020   31.448905   31.463483   31.377413   31.446318   31.562537   
std      3.763585    3.755739    3.878204    3.901966    3.877156    3.947957   
min     23.390000   23.390000   23.390000   19.600000   23.390000   23.390000   
25%     29.000000   28.950000   28.900000   28.900000   28.950000   29.000000   
50%     31.800000   31.700000   31.600000   31.500000   31.600000   31.700000   
75%     33.900000   33.900000   33.900000   33.800000   33.870000   33.900000   
max     42.850000   40.300000   44.370000   44.840000   42.830000   44.270000   

             1806        1807        1808        1809     ...            2007  \
count  201.000000  201.000000  201.000000  201.000000     ...      208.000000   
mean    31.615970   31.573134   31.376766   31.310448     ...       70.139712   
std      4.039261    3.917339    4.017228    3.972970     ...        8.953255   
min     23.390000   23.390000   12.480000   13.430000     ...       43.300000   
25%     29.000000   29.000000   28.950000   28.820000     ...       64.825000   
50%     31.800000   31.800000   31.600000   31.500000     ...       72.750000   
75%     34.000000   34.000000   33.870000   33.800000     ...       76.925000   
max     45.820000   43.560000   43.550000   41.740000     ...       84.500000   

             2008        2009        2010        2011        2012        2013  \
count  208.000000  208.000000  208.000000  208.000000  208.000000  208.000000   
mean    70.447163   70.767740   70.969904   71.324375   71.663077   71.916106   
std      8.800452    8.610341    8.898859    8.376540    8.217466    8.120852   
min     44.500000   45.500000   32.200000   46.700000   46.100000   45.600000   
25%     64.875000   65.225000   65.475000   65.600000   66.075000   66.475000   
50%     73.000000   73.350000   73.700000   73.750000   74.050000   74.150000   
75%     77.150000   77.425000   77.650000   77.825000   78.125000   78.300000   
max     84.600000   84.600000   84.700000   84.700000   84.700000   84.800000   

             2014       2015        2016  
count  208.000000  208.00000  208.000000  
mean    72.088125   72.32101   72.556635  
std      8.074990    7.90202    7.738535  
min     45.400000   47.10000   48.860000  
25%     66.775000   67.05000   67.175000  
50%     74.300000   74.40000   74.500000  
75%     78.400000   78.50000   78.650000  
max     84.800000   84.80000   84.800000
```
[Table of Contents](#table-of-contents)

## Visualizing Data

For code see [visualizing_data.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/visualizing_data.py)

The purpose of this step was to visually check the data for insights as well as for errors. Here is the output comparing the life expectancy in 1800 against that of 2016:

![alt text](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/images/Figure_1.png)

[Table of Contents](#table-of-contents)


