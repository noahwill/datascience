# MOST OF THE CODE IN THIS FILE AND OTHER /CODE FILES WERE WRITTEN BY DATACAMP FOR THE CASE STUDY
# IN THE "CLEANING DATA IN PYTHON" COURSE
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# IMPORTING_DATA.PY
filename = 'gs18002016.xlsx'

# pd.ExcelFile will load in the desired .xlsx file
data = pd.ExcelFile(filename)

# the .parse() method will select the correct sheet from the loaded .xlsx file
# three dataframes are loaded: Life Expectancy for the 1800s, 1900s, and 2000s
df_le1800 = data.parse('1800s', head=0)
df_le1900 = data.parse('1900s', head=0)
df_le2000 = data.parse('2000s', head=0)


#VISUALIZING_DATA.PY
# Create the scatter plot
df_le1800.plot(kind='scatter', x=1800, y=1899)

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
# Remember the descriptive statistics from the README? The MAX/MIN are useful to define these limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()


#ASSERT_CHECK.PY
def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values, and checks if 
    all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()[1:-1]
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

# Check whether the first column is 'Life expectancy'
assert df_le1800.columns[0] == 'Life expectancy'
assert df_le1900.columns[0] == 'Life expectancy'
assert df_le2000.columns[0] == 'Life expectancy'

# Check whether the values in the row are valid
# Chaining .all() twice ensures that this assertion will be applied over the entire dataframe
assert df_le1800.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()
assert df_le1900.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()
assert df_le2000.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# Check that there is only one instance of each country
assert df_le1800['Life expectancy'].value_counts()[0] == 1
assert df_le1900['Life expectancy'].value_counts()[0] == 1
assert df_le2000['Life expectancy'].value_counts()[0] == 1


#ASSEMBLING_DATA.PY
# Concatenate the DataFrames row-wise
gapminder = pd.concat([df_le1800, df_le1900, df_le2000])

# Print the shape of gapminder
print(gapminder.shape)

# Print the head of gapminder
print(gapminder.head())


#MELT_DF.PY
# Melt gapminder: gapminder_melt
gapminder_melt = pd.melt(gapminder, id_vars = 'Life expectancy')

# Rename the columns
gapminder_melt.columns = ['country', 'year', 'life_expectancy']

# Print the head of gapminder_melt
print(gapminder_melt.head())


#ASSERT_TYPE.PY
# Convert the year column to numeric
gapminder_melt.year = pd.to_numeric(gapminder_melt.year)

# Test if country is of type object
assert gapminder_melt.country.dtypes == np.object

# Test if year is of type int64
assert gapminder_melt.year.dtypes == np.int64

# Test if life_expectancy is of type float64
assert gapminder_melt.life_expectancy.dtypes == np.float64


#CHECK_SPELLING.PY
# Create the series of countries: countries
countries = gapminder_melt.country

# Drop all the duplicates from countries
countries = countries.drop_duplicates()

# Write the regular expression: pattern
pattern = '^[A-Za-z\.\s]*$'

# Create the Boolean vector: mask
mask = countries.str.contains(pattern)

# Invert the mask: mask_inverse
mask_inverse = ~mask

# Subset countries using mask_inverse: invalid_countries
invalid_countries = countries.loc[mask_inverse]

# Print invalid_countries
print(invalid_countries)


#ASSERT_NONA.PY
# Assert that country does not contain any missing values
assert pd.notnull(gapminder_melt.country).all()

# Assert that year does not contain any missing values
assert pd.notnull(gapminder_melt.year).all()

# Drop the missing values
gapminder = gapminder_melt.dropna()

# Print the shape of gapminder
print(gapminder_melt.shape)


#PLOT_WRAPUP.PY
# Add first subplot
plt.subplot(2, 1, 1) 

# Create a histogram of life_expectancy
life_expectancy = gapminder_melt.life_expectancy.plot(kind='hist')

# Group gapminder: gapminder_agg
gapminder_agg = gapminder_melt.groupby('year')['life_expectancy'].mean()

# Print the head of gapminder_agg
print(gapminder_agg.head())

# Print the tail of gapminder_agg
print(gapminder_agg.tail())

# Add second subplot
plt.subplot(2, 1, 2)

# Create a line plot of life expectancy per year
gapminder_agg.plot()

# Add title and specify axis labels
plt.title('Life expectancy over the years')
plt.ylabel('Life expectancy')
plt.xlabel('Year')

# Display the plots
plt.tight_layout()
plt.show()

# Save both DataFrames to csv files
gapminder_melt.to_csv('gapminder.csv', encoding='utf8')
gapminder_agg.to_csv('gapminder_agg.csv', encoding='utf8')























