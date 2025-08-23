# ✅ For better visual output and interactive coding:
# Use Jupyter Notebook or Google Colab
# If running in Colab, install required packages:
# !pip install pandas
# !pip install numpy

import numpy as np
import pandas as pd

data = {
    "Name": ["alice", "bob", "charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "San Francisco", "Los Angeles"]
}
df = pd.DataFrame(data)

#  Accessing columns
# df["Name"]          --> Single column
# df[["Name","Age"]]  --> Multiple columns

#  Adding a column
# df["Salary"] = [15000, 20000, 14500]

#  Removing a column
# df.drop("Age", axis=1, inplace=True)

#  Accessing a row using label index
# df.loc[1]

# Series: A vertical, labeled 1D array
labels = ["a", "b", "c"]
lst = [10, 20, 30]
pd.Series(data=lst, index=labels)

#  Using dictionary (recommended and clean way)
data = {
    "Name": ["alice", "bob", "charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "San Francisco", "Los Angeles"]
}
df = pd.DataFrame(data)

# df.loc[[1,2],["Age","City"]]  # Access multiple rows and columns

#  Using list of lists
data1 = [
    ["Alice", 25, "New York"],
    ["Bob", 30, "San Francisco"],
    ["Charlie", 35, "Los Angeles"]
]
cols = ["name", "age", "city"]
df = pd.DataFrame(data1, columns=cols)
print(df)

# Creating a DataFrame with NaN values
data = {
    "A": [1, 2, np.nan, 4, 5],
    "B": [6, np.nan, 8, 9, 10],
    "C": [11, 12, np.nan, 14, 15],
    "D": [16, np.nan, 18, 19, np.nan]
}
df = pd.DataFrame(data)

#  Check where values are null
df.isnull()

#  Count of nulls per column
df.isnull().sum()

#  Check if any value is null in each column
df.isnull().any()

#  Drop rows with any NaN value
df.dropna()

#  Drop rows that have at least 2 non-null values
df.dropna(thresh=2)

#  Fill missing values with specified dictionary
values = {"A": 1, "B": 9, "C": 10, "D": 13}
df.fillna(value=values)

#  Fill missing values with mean of each column
df.fillna(df.mean())

# Create 2 DataFrames to demonstrate joins
employees = pd.DataFrame({
    "e_id": [1, 2, 3, 4],
    "name": ["Alice", "Bob", "Charlie", "David"],
    "department": ["HR", "IT", "Finance", "HR"]
})

salary = pd.DataFrame({
    "e_id": [1, 2, 5, 6],
    "salary": [50000, 60000, 55000, 60000],
    "bonus": [2000, 4000, 5000, 7000]
})

#  Outer Join: all rows from both tables
pd.merge(employees, salary, on="e_id", how="outer")

#  Right Join: all from right table + matches from left
pd.merge(employees, salary, on="e_id", how="right")

#  Concatenate two DataFrames vertically or horizontally
df1 = pd.DataFrame({
    "A": ['A1', 'A2', 'A3'],
    "B": ['B1', 'B2', 'B3'],
    "C": ['C1', 'C2', 'C3']
})
df2 = pd.DataFrame({
    "A": ['A4', 'A5', 'A6'],
    "B": ['B4', 'B5', 'B6'],
    "C": ['C4', 'C5', 'C6']
})
pd.concat([df1, df2], axis=1)  # horizontal join

#  Join based on index
d1 = pd.DataFrame({"A": ['A1', 'A2', 'A3']}, index=[1, 2, 3])
d2 = pd.DataFrame({"B": ['B1', 'B2', 'B3']}, index=[2, 3, 4])
d1.join(d2, how="outer")

# grouping and aggregation
data = {
    "category": ["A", "B", "A", "B"],
    "stores": ["x", "x", "y", "y"],
    "sales": [100, 200, 150, 250],
    "Date": pd.date_range("2023-01-01", periods=4)
}
df = pd.DataFrame(data)

#  Group by one column
df.groupby("category")["sales"].sum()

#  Group by two columns
df.groupby(["category", "stores"])["sales"].sum()

#  Aggregation on a single column
df['sales'].agg(['sum', 'mean', 'max', 'min'])



# custom function
d = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
})

#  Define a function to square the input
def square(x):
    return x**2

#  Apply the function to column B and assign to column A
d["A"] = d["B"].apply(square)
print(d)

