import pandas as pd
medals = pd.DataFrame(pd.read_csv('summer_1896_2008.csv'))

# To make a new Series for the rankings, the 'NOC' or Name of Country column is selected
country_names = medals['NOC']

medal_counts = country_names.value_counts()

# This returns the Series of country names with their medal wins counted
print(medal_counts.head(15))

counted = medals.pivot_table(index='NOC', values='Athlete', columns='Medal', aggfunc='count')

counted['totals'] = counted.sum(axis='columns')

counted = counted.sort_values(by='totals', ascending=False)

print(counted.head(15))
