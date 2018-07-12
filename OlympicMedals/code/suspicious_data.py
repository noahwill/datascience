import pandas as pd
medals = pd.DataFrame(pd.read_csv('summer_1896_2008.csv'))

# If you print the column names, you'll see that there are 'Event_gender' and 'Gender columns
print(medals.columns)

# Are there any entries in both columns that do not match?
ev_gen = medals[['Event_gender', 'Gender']]

ev_gen_uniques = ev_gen.drop_duplicates()

# There are 5 unique entry pairs in Event_gender and Gender
print(ev_gen_uniques)

medals_by_gender = medals.groupby(['Event_gender', 'Gender'])

medal_count_by_gender = medals_by_gender.count()

# After grouping by Event_gender and Gender and counting the occurrences of the unique entries, there is only one that
# seems suspicious! I'll call it sus
print(medal_count_by_gender)

sus = (medals.Event_gender == 'W') & (medals.Gender == 'Men')

suspect = pd.DataFrame(medals[sus])

# According to the data, Joyce Chepchumba was a man that won a medal in a women's event.
# I wonder if this was an engineered mistake in the data or if someone making the data set actually made this mistake
print(suspect)
