# Concatenate the DataFrames row-wise
gapminder = pd.concat([df_le1800, df_le1900, df_le2000])

# Print the shape of gapminder
print(gapminder.shape)

# Print the head of gapminder
print(gapminder.head())
