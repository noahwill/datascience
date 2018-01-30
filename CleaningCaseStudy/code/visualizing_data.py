# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Create the scatter plot
df_le1800.plot(kind='scatter', x=1800, y=1899)

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 1899')

# Specify axis limits
# Remember the descriptive statistics from the README? The MAX/MIN are useful to define these limits
plt.xlim(20, 55)
plt.ylim(20, 55)

# Display the plot
plt.show()
