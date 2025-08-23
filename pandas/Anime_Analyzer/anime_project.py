# 🎯 Mini Project: Anime Dataset Analysis using Pandas

import numpy as np
import pandas as pd

# Load the dataset from 'anime.csv'
df = pd.read_csv('anime.csv')

# Display the first 5 rows of the dataframe
df.head()

# Access the title of the anime at index 1
df.loc[1]['Title']

#  Function to extract episode count from anime title (e.g., "Naruto (220 eps) Oct 2002 - Feb 2007")
def extract_ep(txt):
    chk = False
    data = " "
    for i in txt:
        if i == ")":
            chk = False
            return data
        if chk:
            data += i
        if i == "(":
            chk = True
    return data

# Apply the function to extract episode count from the 'Title' column
df["Episodes"] = df['Title'].apply(extract_ep)

# Remove the string 'eps' from extracted values
df["Episodes"] = df['Episodes'].str.replace("eps", " ")

# Convert episode strings to integers
df["Episodes"] = df["Episodes"].astype(int)

# (Optional) View the dataframe
df

# Access the title of the anime at index 3
df.loc[3]["Title"]

#  Function to extract airing period (e.g., "Oct 2002 - Feb 2007") after the closing parenthesis
def extract_time(txt):
    chk = False
    data = " "
    for i in range(len(txt)):
        if txt[i] == ")":
            for j in range(i+1, i+20):  # next 20 chars approx = " Oct 2002 - Feb 2007"
                data += txt[j]
            return data

# Apply the function to extract time period and save to new column
df["Total Time"] = df["Title"].apply(extract_time)

# Show first 5 rows with new columns
df.head()

# Required libraries to calculate time differences in months
from dateutil.relativedelta import relativedelta
from datetime import datetime

#  Function to calculate total months between start and end date
def calculate_total_months(period):
    try:
        start_str, end_str = period.split(" - ")
        start_date = datetime.strptime(start_str.strip(), "%b %Y")  # e.g., "Oct 2002"
        end_date = datetime.strptime(end_str.strip(), "%b %Y")      # e.g., "Feb 2007"
        r = relativedelta(end_date, start_date)
        total_months = (r.years * 12) + r.months
        return total_months
    except:
        return None  # For titles without valid dates

# Apply the function to compute airing duration in months
df["Months"] = df["Total Time"].apply(calculate_total_months)

# Find the anime with the highest score
df[df["Score"] == df["Score"].max()]['Title']

# Show top 5 titles
df['Title'].head()

# Find the anime with the highest number of episodes
ep = df[df['Episodes'] == df['Episodes'].max()]

#  Get top 5 anime by episode count
top_5_episodes = df.sort_values(by='Episodes', ascending=False).head(5)
# Uncomment this in Jupyter: display(top_5_episodes)

#  Find the anime that aired for the longest time (in months)
large = df[df["Months"] == df["Months"].max()]