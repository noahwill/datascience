# Olympic Medals Case Study - DataFrame Manipulation

Is there a better way to practice manipulating DataFrames in pandas than to learn about the true nature of the Cold War? In this era of questionable political action and international relations, I would think not. In this study, I munge my way to a surprising discovery and try to code my way to feeling better about it.

This case study may be found at the end of the [Manipulating DataFrames with pandas](https://www.datacamp.com/courses/manipulating-dataframes-with-pandas) course provided by Data Camp. The complete data set used in this study may be found [here](https://assets.datacamp.com/production/course_1650/datasets/all_medalists.csv) on the DataCamp website.

## Table of Contents

* [Ranking by Medals Won](#ranking-by-medals-won)
* [Suspicious Data](#suspicious-data)
* [Into the Cold War!](#into-the-cold-war!)
* [War at the Olympics](#war-at-the-olympics)
* [Graphs Make Me Feel Good](#graphs-make-me-feel-good)
* [Area Graphs Look Better](#area-graphs-look-better)
* [Possibilities for Further Study](#possibilities-for-further-study)

## Ranking by Medals Won

Code: [ranking.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/ranking.py)

As a light warm up to get ready for the DataFrame gymnastics ahead, I made a simple Series and DataFrame from the data to show medal totals by country. The Series, called medal_counts, was selected from the country name column from a DataFrame, one which I use for the rest of the investigation called medals, counted the occurances of each unique name, and sorted those counts into a list of descending value: 

```python
USA    4335
URS    2049
GBR    1594
FRA    1314
ITA    1228
Name: NOC, dtype: int64
```

The DataFrame, called counted, used a pivot table with the country names as the index, the athlete who won a medal as the values, the medal type earned as the columns, and aggregated the data by counting. A column called 'totals' was added to the DataFrame that summed along the columns to achieve the total medals won by that country. I then sorted on this 'totals' column to have the same rankings by country as the Series from earlier. 

```python
Medal  Bronze    Gold  Silver  totals
NOC                                  
USA    1052.0  2088.0  1195.0  4335.0
URS     584.0   838.0   627.0  2049.0
GBR     505.0   498.0   591.0  1594.0
FRA     475.0   378.0   461.0  1314.0
ITA     374.0   460.0   394.0  1228.0
```

Strangely, the medal types are out of their usual Olympic order. Later, I make an area graph that first converts the 'Medal' column in the medals DataFrame to categorical data with ordered categories. 

## Suspicious Data

Code: [suspicious_data.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/suspicious_data.py)

Now for some good old data cleaning to see if there are any notable inconsistencies. First, I took a look at the columns of the DataFrame; there were two columns that may have had the same data in them: 'Gender' and 'Event_gender'.

```python
Index(['City', 'Edition', 'Sport', 'Discipline', 'Athlete', 'NOC', 'Gender',
       'Event', 'Event_gender', 'Medal'],
      dtype='object')
```

I tested to see if there were any entries in these columns that did not match by selecting the two columns and dropping all duplicates. The resulting DataFrame, ev_gender_uniques, shows the five different entries that exist when looking at 'Gender' and 'Event_gender' together. One of these entries shows 'W' and 'Men' entries for one event: 

```python
      Event_gender Gender
0                M    Men
348              X    Men
416              W  Women
639              X  Women
23675            W    Men
```

To investigate further, I created a DataFrame that grouped medals by 'Gender' and 'Event_gender' then counted the unique entries in each category. This showed that there is only one occurrance of the 'W' 'Men' pair, which means that the entry was probably a mistake:

```python
                      City  Edition  Sport  ...      NOC  Event  Medal
Event_gender Gender                         ...                       
M            Men     20067    20067  20067  ...    20067  20067  20067
W            Men         1        1      1  ...        1      1      1
             Women    7277     7277   7277  ...     7277   7277   7277
X            Men      1653     1653   1653  ...     1653   1653   1653
             Women     218      218    218  ...      218    218    218

[5 rows x 8 columns]
```

Finally, I created a boolean series that selected the erroneous datum and returned it as a DataFrame. It shows that Joyce Chepchumba was a man that won a medal in a women's event. A Google search shows that she was in fact a woman! I wonder if this was an engineered mistake in the data for the sake of the exercise or if someone making the data set actually made this mistake: 

```python
         City  Edition      Sport Discipline            Athlete  NOC Gender     Event Event_gender   Medal
23675  Sydney     2000  Athletics  Athletics  CHEPCHUMBA, Joyce  KEN    Men  marathon            W  Bronze
```

## Into the Cold War!

Code: [into_the_cold_war.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/into_the_cold_war.py)

With the warm up complete, the investigation with real historical significance begins. In this section, I grouped my medals DataFrame by country and then slected the sports column to create a Series with the number of unique sports each country has won medals in: 

```python 
NOC
USA    34
GBR    31
FRA    28
GER    26
CHN    24
Name: Sport, dtype: int64
```

Next, I created two boolean series to select the years 1952-1988, the years during the Cold War, and the data for the USA and URS. Using the same method as above, I selected the data that matched the boolean series and grouped by the country names. Finally, I selected the number of unique sports the USA and URS won medals in and sorted them in descending order: 

```python
NOC
URS    21
USA    20
Name: Sport, dtype: int64
```

The URS may have won medals in more sports than the USA, but which country won medals more consistently?

## War at the Olympics

Code: [war_at_the_olympics.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/war_at_the_olympics.py)

To anwer the question of who won more medals more times during Cold War Olympics, I used a pivor table indexed on the year of the Olympics, with columns by country name, with the number of medals won during that year as the data. Then I selected only the Cold War years and the data for the USA and URS. On this DataFrame, I used the .idmax() method to return the country that won the most medals each year during the Cold War. Finally, I used the .value_counts() method count the number of times each country won more medals: 

```python 
print(war_winner)
URS    8
USA    2
dtype: int64
```

If winning Olympic medals during the Cold War was as serious as serious as the real life Miracle on Ice and the subsequent two movies made about it, then the USA seriously lost when it came to the Summer Olympics. 

## Graphs Make Me Feel Good

Code: [graphs_make_us_better.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/graphs_make_us_better.py)

To try to help cope with the realization of this loss, I turned to graphs, my comfort of choice when it comes to data. I created a simple plot by selecting just the data for the USA, grouping by Olympic Edition and Medal type, and aggregating the count over athlete names. The resulting DataFrame had two indecies so I used the .unstack method to assign the medal types as columns. This made a DataFrame that was easily translateable to a line plot:

![alt text](https://github.com/noahwill/datascience/blob/master/OlympicMedals/Figure_1.png)

## Area Graphs Look Better

Code: [area_graphs_look_better.py](https://github.com/noahwill/datascience/blob/master/OlympicMedals/code/area_graphs_look_better.py)

That area plot does not really offer any kind of direction for significant interpretation, so maybe an area graph would be better. As an extra step, I made sure that the medal types were ordered categories so the area graph would be stacked 'Bronze', 'Silver', 'Gold'. 

![alt text](https://github.com/noahwill/datascience/blob/master/OlympicMedals/Figure_2.png)

## Possibilitie for Further Study

Of course it is all in fun that I make the claim that the URS having more consistent medal wins over the USA is of historical significance, but I think there is opportunity here for some more interesting historical investigation. Why is there a massive spike in medals won for the USA after 1900? What effect if any did financial crises have on medals won in the Olympics? Did the URS have more athletes competing than the USA in the Cold War editions of the Olympics? What contributes to winning medals in the Olympics? Is it GDP, population, unemployment, or if a country is hosting? Is there a correlation of medals to previous medals in an event? I'd love to revisit this data and try to answer these questions when I am more of a pythonista!

<p align="center">
  <img src="https://github.com/noahwill/datascience/blob/master/OlympicMedals/herb_brooks.gif" alt="Again!"/>
</p>


In the mean time, I'll have Kurt Russell as Herb Brooks, the coach of the US '80 Winter Olympics Hockey Team, to remind me that I need to go again if I hit a wall as I continue to learn. 
