# Data Cleaning Case Study - Life Expectancy

This Case Study may be found at the end of the [Cleaning Data in Python](https://www.datacamp.com/courses/cleaning-data-in-python) course provided by Data Camp.

The course itself used Gapminder data that showed life expectancy by country from 1800-1899, however for the project I am featuring here, I am using the complete data set found [here](https://www.gapminder.org/data/) by searching for "Life expectancy (years)."

## Table of Contents

* [Formatting Data](#formatting-data)
* [Importing Data](#importing-data)
* [Initial Exploration](#initial-exploration)
* [Visualizing Data](#visualizing-data)
* [The Question at Hand](#the-question-at-hand)

## Formatting Data

The file of data from Gapminder is downloadable as .xlxs. That file, found in this repository as **gs18002016.xlsx**. To practice concatenating data later on in the data cleaning process, I divided life expectancy data by country into three time periods: 1800s, 1900s, and 2000s

[Table of Contents](#table-of-contents)

## Importing Data

I created three data frames using the method .parse() on each of the sheets from the imported excel file. See [importing_data.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/importing_data.py) for importing process. 

[Table of Contents](#table-of-contents)

## Initial Exploration 

In order to help my workflow, I performed a few preliminary commands to show what the needs for cleaning were for this particular data set. 

```python
>>> print(df_le1800.shape)
(260, 101)
```

So, I know that the shape of the data frame is 260 rows by 101 columns. Since this is country data, I can assume that the rows will be the country names. **_What are the column names?_**

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

Here, I found out that the first column, "Life expectancy," contains all of the country names included in the data set. Next, I printed basic descriptive statistics that may have been useful in the data cleaning process. 

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

             1806        1807        1808        1809     ...            1890  \
count  201.000000  201.000000  201.000000  201.000000     ...      201.000000   
mean    31.615970   31.573134   31.376766   31.310448     ...       32.291045   
std      4.039261    3.917339    4.017228    3.972970     ...        5.907298   
min     23.390000   23.390000   12.480000   13.430000     ...        4.000000   
25%     29.000000   29.000000   28.950000   28.820000     ...       29.200000   
50%     31.800000   31.800000   31.600000   31.500000     ...       32.000000   
75%     34.000000   34.000000   33.870000   33.800000     ...       35.000000   
max     45.820000   43.560000   43.550000   41.740000     ...       50.480000   

             1891        1892        1893        1894        1895        1896  \
count  201.000000  201.000000  201.000000  201.000000  201.000000  201.000000   
mean    32.475373   32.478408   32.533085   32.747214   32.811841   32.895224   
std      5.734794    5.825318    6.018269    5.822354    6.067020    6.344388   
min      8.000000   14.000000    8.000000   22.180000   22.000000   20.000000   
25%     29.200000   29.000000   29.000000   29.200000   29.200000   29.000000   
50%     32.000000   32.000000   32.000000   32.000000   32.000000   32.000000   
75%     35.100000   35.000000   35.000000   35.000000   35.000000   35.000000   
max     51.090000   52.730000   52.580000   52.100000   54.160000   53.840000   

             1897        1898        1899  
count  201.000000  201.000000  201.000000  
mean    32.964279   32.994080   32.962985  
std      6.390669    6.336805    6.325265  
min     19.000000   19.700000   18.900000  
25%     29.200000   29.160000   29.000000  
50%     32.000000   32.000000   32.000000  
75%     35.000000   35.180000   35.180000  
max     54.140000   54.690000   51.620000
```
[Table of Contents](#table-of-contents)

## Visualizing Data

For code see [visualizing_data.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/visualizing_data.py)

The purpose of this step was to visually check the data for insights as well as for errors. Here is the output comparing the life expectancy in 1800 against that of 1899:

This plot reveals what is already common knowledge about the world: life expectancy has drastically increased since the 1800s. An error that this plot could have made me aware of could have been a constant life expectancy for any country which would have shown itself by data falling on a diagonal line. 

[Table of Contents](#table-of-contents)

## The Question at Hand

For code see [assertions_check.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/assertions_check.py)

I wrote a quick function to drop all missing row values and check if the remaining values are greater-than or equal to zero. Three assertions are also included in the code: 
```python 
# Check whether the first column is 'Life expectancy'
assert data.columns[0] == 'Life expectancy'

# Check whether the values in the row are valid
assert data.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# Check that there is only one instance of each country
assert g1800s['Life expectancy'].value_counts()[0] == 1
```
I have a feeling I am going to have a love-hate relationship with asertions. Love because they will help me preemptively keep errors from popping up in my code. Hate because they don't actually give a response if they work. I really like to be told when stuff works...

[Table of Contents](#table-of-contents)
