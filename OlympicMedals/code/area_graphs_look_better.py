import pandas as pd
import matplotlib.pyplot as plt
medals = pd.DataFrame(pd.read_csv('summer_1896_2008.csv'))

# This line ensures that the area graph will be consistent with the Olympic rules
medals.Medal = pd.Categorical(values=medals.Medal, categories=['Bronze', 'Silver', 'Gold'], ordered=True)

usa = medals[medals['NOC'] == 'USA']

usa = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

usa_medals_by_year = usa.unstack(level='Medal')

usa_medals_by_year.plot.area()
plt.xlabel('Olympic Edition')
plt.ylabel('Total Medals Won by')
plt.title('Look We Are Good At Sports II')
plt.show()
