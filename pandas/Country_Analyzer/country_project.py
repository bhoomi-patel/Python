# Importing necessary libraries
import numpy as np
import pandas as pd

# Read the dataset from a CSV file named 'Countries.csv' into a DataFrame
df = pd.read_csv('Countries.csv')

# Show the shape of the DataFrame as (rows, columns)
df.shape  

# Show basic info about each column: names, data types, non-null counts, memory usage
df.info() 

# Show summary statistics for numerical columns (count, mean, std, min, max, etc.)
df.describe()  

# Find the country and its capital with the highest population
df[df['population'] == df['population'].max()][['country','capital_city']]

# Sort the DataFrame in-place by 'democracy_score' in descending order
df.sort_values(by='democracy_score', ascending=False, inplace=True)

# Display the first 5 country names (from top after sorting)
df["country"].head()

# Count how many **unique regions** are there in the dataset
df['region'].value_counts().count()

# List all countries that are in the region "Eastern Europe"
df[df['region'] == "Eastern Europe"]["country"]

# Get the second largest population value and filter the country with that population
df[df['population'] == df['population'].nlargest(2).iloc[1]]

# Display the political leader of the country with the second-largest population
df[df['population'] == df['population'].nlargest(2).iloc[1]]['political_leader']

# Find countries where the 'political_leader' field is missing (NaN)
df.loc[df['political_leader'].isna()]["country"]

# Count how many countries have missing (NaN) political leaders
df.loc[df['political_leader'].isna()]["country"].count()

# Initialize a counter to count countries that have "republic" in their name
count = 0

# Define a function that increments the counter if 'republic' appears in the country name
def counting(txt):
    global count
    if 'republic' in txt.lower():   # case-insensitive check
        count += 1
    return txt

# Apply the counting function to the 'country_long' column
df["country_long"] = df["country_long"].apply(counting)

# Print how many countries contain the word "republic" in their long name
print(count)

# Filter all countries that are in the continent "Africa"
africa_df = df[df["continent"] == "Africa"]

# From the African countries, get the country with the highest population
africa_df[africa_df['population'] == africa_df['population'].max()][['country', 'population']]
