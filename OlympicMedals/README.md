# Olympic Medals Case Study - DataFrame Manipulation

Is there a better way to practice manipulating DataFrames in pandas than to learn about the true nature of the Cold War? In this era of questionable political action and international relations, I would think not. In this study, I munge my way to a surpirising discovery and try to code my way to feeling better about it.

This case study may be found at the end of the [Manipulating DataFrames with pandas](https://www.datacamp.com/courses/manipulating-dataframes-with-pandas) course provided by Data Camp. The complete data set used in this study may be found [here](https://assets.datacamp.com/production/course_1650/datasets/all_medalists.csv) on the DataCamp website.

## Table of Contents

* [Ranking by Medals Won](#ranking-by-medals-won)
* [Suspicious Data](#suspicious-data)
* [Into the Cold War!](#into-the-cold-war!)
* [War at the Olympics](#war-at-the-olympics)
* [Graphs Make Me Feel Good](#graphs-make-me-feel-good)
* [Area Graphs Look Better](#area-graphs-look-better)

## Ranking by Medals Won

Code: [ranking.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/ranking.py)

As a light warm up to get ready for the DataFrame gymnastics ahead, I made a simple Series and DataFrame from the data to show medal totals by country. The Series, called medal_counts, was selected from the country name column from a DataFrame, one which I use for the rest of the investigation called medals, counted the occurances of each unique name, and sorted those counts into a list of descending value: 

```python
print(medal_counts.head(5))
USA    4335
URS    2049
GBR    1594
FRA    1314
ITA    1228
Name: NOC, dtype: int64
```

The DataFrame, called counted, used a pivot table with the country names as the index, the athlete who won a medal as the values, the medal type earned as the columns, and aggregated the data by counting. A column called 'totals' was added to the DataFrame that summed along the columns to achieve the total medals won by that country. I then sorted on this 'totals' column to have the same rankings by country as the Series from earlier. 

```python
print(counted.head(5))
Medal  Bronze    Gold  Silver  totals
NOC                                  
USA    1052.0  2088.0  1195.0  4335.0
URS     584.0   838.0   627.0  2049.0
GBR     505.0   498.0   591.0  1594.0
FRA     475.0   378.0   461.0  1314.0
ITA     374.0   460.0   394.0  1228.0
```

Strangely, the medal types are out of their usual olympic order. Later, I make an area graph that first converts the 'Medal' column in the medals DataFrame to categorical data with ordered categories. 

## Suspicious Data

Code: [suspicious_data.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/suspicious_data.py)
## Into the Cold War!

Code: [into_the_cold_war.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/into_the_cold_war.py)
## War at the Olympics

Code: [war_at_the_olympics.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/war_at_the_olympics.py)
## Graphs Make Me Feel Good

Code: [graphs_make_us_better.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/graphs_make_us_better.py)
## Area Graphs Look Better

Code: [area_graphs_look_better.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/area_graphs_look_better.py)
