import pandas as pd

filename = 'g18002016.csv'

# header gives which row to use as column labels, sep gives the delimeter, na_values gives string recognized as missing values
data = pd.read_csv(filename, header=0, sep=',', na_values=['NaN'])
