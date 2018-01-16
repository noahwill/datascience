# Data Cleaning Case Study - Life Expectancy

This Case Study may be found at the end of the [Cleaning Data in Python](https://www.datacamp.com/courses/cleaning-data-in-python) course provided by Data Camp.

The course itself used Gapminder data that showed life expectancy by country from 1800-1899, however for the project I am featuring here, I am using the complete data set found [here](https://www.gapminder.org/data/) by searching for "Life expectancy (years)."

## Formatting Data

The file of data from Gapminder is downloadable as .xlxs, however for this project I wanted to practice manipulating .csv files. So, in the .xlxs file, I replaces all the blank spaces with NaN to signify missing data points. Then, I saved the sheet as a .csv file. 

That file, found in this repository as **g18002016.csv**, contains life expectancy data by country from 1800 to 2016.

## Importing the File

See [importing_data.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/importing_data.py) for importing process. 

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

Here, I found out that the first column, "Life expectancy," contains all of the country names included in the data set. This means that the 999 rows of data are for 998 countries. **_In my data cleaning process, I will have to change the name of the first column to "Country Names" to accurately show what data is given in it._**

## Visualizing the Data



