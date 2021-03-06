"""
Let's visualize some data using seaborn.
"""
import pandas as pd
import seaborn as sns

# Read in the cars csv
CARS = pd.read_csv('assets/cars.csv', sep=';')

# Drop the first row of the dataframe (it just describes the data type.)
CARS = CARS.drop(CARS.index[[0]])

# Change MPG from string into float
CARS['MPG'] = CARS['MPG'].astype(float)

# Create Zero filter
ZERO_MPG_FILTER = CARS['MPG'] != 0

# Filter Cars
FILTERED_CARS = CARS[ZERO_MPG_FILTER]

# Arrange by descending so the highest are at the top
FILTERED_CARS.sort_values(by=('MPG'), inplace=True, ascending=False)

#
sns.set(style='ticks')

# Create integer version of MPG and Cylinder
FILTERED_CARS['mpg_int'] = FILTERED_CARS['MPG'].astype(int)
FILTERED_CARS['cylinders_int'] = FILTERED_CARS['Cylinders'].astype(int)

# Drop duplicates
FILTERED_CARS = FILTERED_CARS.drop_duplicates('Car')

# Create the graph
AX = sns.pointplot(y='cylinders_int', x='mpg_int', data=FILTERED_CARS, palette='muted')

# Do labeling
AX.set_ylabel('Number of Cylinders')
AX.set_xlabel('MPG per Car')
AX.set_title('MPG vs. Number of Cylinders')


# Show the graph
sns.plt.show()
