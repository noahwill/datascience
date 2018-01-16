# Import matplotlib.pyplot
import matplotlib.pyplot as plt

# Create the scatter plot
data.plot(kind='scatter', x='1800', y='2016')

# Specify axis labels
plt.xlabel('Life Expectancy by Country in 1800')
plt.ylabel('Life Expectancy by Country in 2016')

# Specify axis limits
# Remember the descriptive statistics from the README? This is where the MAX/MIN can be found.
plt.xlim(20, 55)
plt.ylim(20, 90)

# Display the plot
plt.show()
