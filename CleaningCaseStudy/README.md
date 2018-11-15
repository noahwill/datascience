# Data Cleaning Case Study - Life Expectancy

This Case Study may be found at the end of the [Cleaning Data in Python](https://www.datacamp.com/courses/cleaning-data-in-python) course provided by Data Camp.

The complete data set used in this study may be found [here](https://www.gapminder.org/data/) by searching for "Life expectancy (years)."

The final code has been compiled into [master_cleaner.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/code/master_cleaner.py)

## Table of Contents

* [Formatting Data](#formatting-data)
* [Importing Data](#importing-data)
* [Initial Exploration](#initial-exploration)
* [Visualizing Data](#visualizing-data)
* [The Question at Hand](#the-question-at-hand)
* [Assembling and Melting Data](#assembling-and-melting-data)
* [Asserting Data Types](#asserting_data_types)
* [Checking Country Spelling](#checking_country_spelling)
* [More Assertions](#more_assertions)
* [Wrapping Up](#wrapping_up)

## Formatting Data

The file of data from Gapminder is downloadable as .xlxs. That file, found in this repository as **gs18002016.xlsx**. To practice concatenating data later on in the data cleaning process, I divided life expectancy data by country into three time periods: 1800s, 1900s, and 2000s


## Importing Data

Code: [importing_data.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/code/importing_data.py)

I created three data frames using the method .parse() on each of the sheets from the imported excel file.

```python 
filename = 'gs18002016.xlsx'

data = pd.ExcelFile(filename)

df_le1800 = data.parse('1800s', head=0)
df_le1900 = data.parse('1900s', head=0)
df_le2000 = data.parse('2000s', head=0)
```

## Initial Exploration 

In order to help my workflow, I performed a few preliminary commands to show what the needs for cleaning were for this particular data set. 

```python
>>> print(df_le1800.shape)
(260, 101)
```

So, I know that the shape of the data frame is 260 rows by 101 columns. Since this is country data, I can assume that the rows will be the country names. **_What are the column names?_**

```python 
>>> print(df_le1800.columns)
Index([u'Life expectancy',               1800,               1801,
                     1802,               1803,               1804,
                     1805,               1806,               1807,
                     1808,
       ...
                     1890,               1891,               1892,
                     1893,               1894,               1895,
                     1896,               1897,               1898,
                     1899],
      dtype='object', length=101)
```

As expected, the colums include the range of years in the data set. However, the first column, "Life expectancy" is probably the title for the kind of data given for each year by country. **_I printed the head next to see what the "Life expectancy" column contained._**

```python
>>> print(df_le1800.head(5))
        Life expectancy   1800   1801   1802   1803   1804   1805   1806  \
0               Abkhazia    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
1            Afghanistan  28.21  28.20  28.19  28.18  28.17  28.16  28.15   
2  Akrotiri and Dhekelia    NaN    NaN    NaN    NaN    NaN    NaN    NaN   
3                Albania  35.40  35.40  35.40  35.40  35.40  35.40  35.40   
4                Algeria  28.82  28.82  28.82  28.82  28.82  28.82  28.82   

    1807   1808  ...     1890   1891   1892   1893   1894   1895   1896  \
0    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN    NaN   
1  28.14  28.13  ...    27.29  27.28  27.27  27.26  27.25  27.24  27.23   
2    NaN    NaN  ...      NaN    NaN    NaN    NaN    NaN    NaN    NaN   
3  35.40  35.40  ...    35.40  35.40  35.40  35.40  35.40  35.40  35.40   
4  28.82  28.82  ...    28.82  28.82  28.82  28.82  28.82  28.82  28.82   

    1897   1898   1899  
0    NaN    NaN    NaN  
1  27.22  27.21  27.20  
2    NaN    NaN    NaN  
3  35.40  35.40  35.40  
4  28.82  28.82  28.82
```

Here, I found out that the first column, "Life expectancy," contains all of the country names included in the data set. Next, I printed basic descriptive statistics that may have been useful in the data cleaning process. 

```python
>>> print(df_le1800.describe())
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

## Visualizing Data

Code: [visualizing_data.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/code/visualizing_data.py)

The purpose of this step was to visually check the data for insights as well as for errors. Here is the output comparing the life expectancy in 1800 against that of 1899:

![alt text](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/images/Figure_1.png)

This plot shows a potential error. The points fall on a diagonal line which means that life epectancy remained the same in the two years. Looking at the the dataframe df_le1800 closer reveals that 140 of the 260 countries did not have a change in life expectancy in the 1800s. This may be because of not having access to data for all the years for those countries.

## The Question at Hand

**_How much does the average life expectancy change over each year?_**

Before answering this question, it is important to make sure that 'Life expectancy is the first column of the DataFrames. The other columns must contain only null or numeric values. Those numeric values must be >= 0. And there must only be one instance for each country. 

Code: [assertions_check.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/code/assert_check.py)

I wrote a quick function to drop all missing row values and check if the remaining values are greater-than or equal to zero. Three assertions are also included in the code to ensure the above mentioned paramaters were met: 
```python 
assert df_le1800.columns[0] == 'Life expectancy'

assert df_le1800.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

assert df_le1800['Life expectancy'].value_counts()[0] == 1
```

I have a feeling I am going to have a love-hate relationship with asertions. Love because they will help me preemptively keep errors from popping up in my code. Hate because they don't actually give a response if they work. I really like to be told when stuff works...

## Assembling and Melting Data

Code: [assert_check.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/code/assert_check.py), 
      [melt_df.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/code/melt_df.py)

I then concatenated the three DataFrames row-wise. 
```python 
gapminder = pd.concat([df_le1800, df_le1900, df_le2000])
```

Then I melted gapminder to have only three columns: 'country', 'year', and 'life_expectancy'
```python
gapminder_melt = pd.melt(gapminder, id_vars = 'Life expectancy')

gapminder_melt.columns = ['country', 'year', 'life_expectancy']
```

After doing so, I ran a quick .head() test on the new DataFrame _gapminder_melt_ to see if the concatenation was successful. The output was:
```python 
                 country  year  life_expectancy
0               Abkhazia  1800              NaN
1            Afghanistan  1800            28.21
2  Akrotiri and Dhekelia  1800              NaN
3                Albania  1800            35.40
4                Algeria  1800            28.82
```
Success! I created a workable tidier DataFrame that has all 218 columns of data from 1800 to 2016 in 3 new columns. 

## Asserting Data Types

Code: [assert_type.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/code/assert_type.py)

Before moving forward, I have to checked if I had all the expected data types in my new columns. The expected data types for the new columns: 'country':'object', 'year':'int64', and 'life_expectancy':'float64.' 

As with all the other assertions written in this case study, if there is no violations of the assertion within the data set, there will be no error given. 

```python
assert gapminder_melt.country.dtypes == np.object

assert gapminder_melt.year.dtypes == np.int64

assert gapminder_melt.life_expectancy.dtypes == np.float64
```

## Checking Country Spelling

Code: [check_spelling.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/code/check_spelling.py) 

With all the data types verified, I moved on to drop any duplicates and check if the country names all contained valid and normal characters. I needed to create a regular expression that matches capital letters at the beginning of country names, any number of lowercase letters, and spaces between words in a name.

```python 
pattern = '^[A-Za-z\.\s]*$'
```

Then I created a boolean vector 'mask' to verify that the country names (converted with .str) contained the pattern. Then I inverted the mask in order to extract the country names that did not match the pattern. 

```python 
mask = countries.str.contains(pattern)

mask_inverse = ~mask

invalid_countries = countries.loc[mask_inverse]
```

The invalid countries were:

```python 
    49            Congo, Dem. Rep.
    50                 Congo, Rep.
    53               Cote d'Ivoire
    73      Falkland Is (Malvinas)
    93               Guinea-Bissau
    98            Hong Kong, China
    118    United Korea (former)\n
    131               Macao, China
    132             Macedonia, FYR
    145      Micronesia, Fed. Sts.
    161            Ngorno-Karabakh
    187             St. Barthélemy
    193     St.-Pierre-et-Miquelon
    225                Timor-Leste
    251      Virgin Islands (U.S.)
    252       North Yemen (former)
    253       South Yemen (former)
    258                      Åland
    Name: country, dtype: object
```

Obviously not all of these names were invalid, they just didn't meet my pattern's standard for consistency, but there were a few cases like 'Åland' that would have been good to investigate for breaking the pattern. 

## More Assertions

Code: [assert_nona.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/code/assert_nona.py)

After the country names were investigated, I made sure 'country' and 'year' did not contain any missing values and dropped rows that contained missing values in the 'life_expectancy' column.

```python 
assert pd.notnull(gapminder_melt.country).all()

assert pd.notnull(gapminder_melt.year).all()

gapminder = gapminder_melt.dropna()
```
This took the rows of the DataFrame down from 169260 to 43857, which is probably not the best thing since that is about 75% of the data. In later courses since, I have learned how to fill in and impute missing values. However in this course, dropping the values was the best option since I did not know these methods yet. 

## Wrapping Up

Code: [plot_wrapup.py](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/code/plot_wrapup.py)

Finally, with this new clean DataFrame, I created two plots: a histogram of life_expectancy, and a line plot of aggregate life_expectancy by year. 

![alt text](https://github.com/noahwill/datascience/blob/master/CleaningCaseStudy/images/Figure_2.png)

From the histogram plot, one can see how most of the world since 1800 has had a life expectancy of around 30-39 years. The line plot shows the trend of almost exponential life expectancy growth starting around 1900 and major historical events like wars drawing life expectancy down.
