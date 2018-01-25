import pandas as pd

filename = 'gs18002016.xlsx'

# pd.ExcelFile will load in the desired .xlsx file
data = pd.ExcelFile(filename)

# the .parse() method will select the correct sheet from the loaded .xlsx file
df_gs = data.parse('Data')
