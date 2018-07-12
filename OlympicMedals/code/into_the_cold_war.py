import pandas as pd
medals = pd.DataFrame(pd.read_csv('summer_1896_2008.csv'))

country_grouped = medals.groupby('NOC')

distinct_sports = country_grouped['Sport'].nunique()

sort_sports = distinct_sports.sort_values(ascending=False)

print(sort_sports.head(15))

# With this technique, I aggregate the number of distinct sports where the USA and USSR won medals during the cold war.
# 1952-1988
# This Boolean series filters for the correct years
during_cold_war = (medals.Edition >= 1952) & (medals.Edition <= 1988)

# This Boolean series filters for the correct countries
is_usa_urs = medals.NOC.isin(['USA', 'URS'])

# New DataFrame generated using boolean series
cold_war_medals = medals.loc[during_cold_war & is_usa_urs]
country_grouped = cold_war_medals.groupby('NOC')

# Series that shows the unique, sorted number or sports
Nsports = country_grouped['Sport'].nunique().sort_values(ascending=False)

print(Nsports)
