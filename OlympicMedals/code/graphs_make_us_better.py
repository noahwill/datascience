# Now that we are sad we lost the Cold War, lets make graphs of our performance to make us feel better.

import pandas as pd
import matplotlib.pyplot as plt
medals = pd.DataFrame(pd.read_csv('summer_1896_2008.csv'))

usa = medals[medals['NOC'] == 'USA']

usa = usa.groupby(['Edition', 'Medal'])['Athlete'].count()

usa_medals_by_year = usa.unstack(level='Medal')

usa_medals_by_year.plot()
plt.xlabel('Olympic Edition')
plt.ylabel('Medals Won by USA')
plt.title('Look We Are Good At Sports')
plt.show()
