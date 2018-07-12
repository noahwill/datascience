import pandas as pd
medals = pd.DataFrame(pd.read_csv('/Users/noah/Desktop/DFManipulation/Data/summer_1896_2008.csv'))

# So who won the most medals consistently over the Cold War period?
medals_won_by_country = medals.pivot_table(index='Edition', columns='NOC', values='Medal', aggfunc='count')

medals_usa_urs = medals_won_by_country.loc[1952:1988, ['USA', 'URS']]

# This gives the country that won the most medals during the Cold War editions of the Olympics
battle_not_war = medals_usa_urs.idxmax(axis=1)

# This determines the total number of times the countries won more medals
war_winner = battle_not_war.value_counts()

print(war_winner)
