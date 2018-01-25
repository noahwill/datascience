import pandas as pd

filename = 'gs18002016.xlsx'

# pd.ExcelFile will load in the desired .xlsx file
data = pd.ExcelFile(filename)

# the .parse() method will select the correct sheet from the loaded .xlsx file
# three dataframes are loaded: Life Expectancy for the 1800s, 1900s, and 2000s
df_le1800 = data.parse('1800s', head=0)
df_le1900 = data.parse('1900s', head=0)
df_le2000 = data.parse('2000s', head=0)

