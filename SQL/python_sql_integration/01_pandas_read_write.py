# Pandas and SQL: Reading and Writing DataFrames
''' Key Concepts/Topics
pandas.read_sql(query, conn): Executes a SQL query on the given connection object (conn) and returns the results as a DataFrame.
DataFrame.to_sql(table_name, conn): Writes a DataFrame back to a database as a new or existing table.
if_exists='replace': Drop the table if it exists, then insert the DataFrame.
if_exists='append': Add rows to the existing table.
index=False: Prevents Pandas DataFrame index from being stored as an additional column.
Efficient Big Data Handling: For large tables, read data in chunksize (iterator), process each chunk.
Integration with ML Libraries: Data ready in DataFrames can immediately become input for scikit-learn, TensorFlow, PyTorch, etc.
 '''
import pandas as pd
import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'demo.db'
# 1. Setup & connect
conn = setup_db(DB_FILE)
print("Connected to database.")

# 2. Read: Get all products into a DataFrame
print("\nReading all products into a DataFrame:")
df_products = pd.read_sql("SELECT * FROM Products;",conn)
print(df_products)

# 3. Read: Get order totals per customer into a DataFrame (grouped/aggregated)
print("\nOrder totals per customer to DataFrame:")
df_orders = pd.read_sql(""" SELECT customer_id,SUM(total_amount) AS total_spent FROM Orders GROUP BY customer_id ORDER BY total_spent DESC; """,conn)
print(df_orders)

# 4. Write: Save a new DataFrame to the database as a new table
print("\nWriting a mini leaderboard to SQL (table: 'customer_leaderboard')")
leaderboard = df_orders.head(3) # top 3 highest spenders
leaderboard.to_sql('customer_leaderboard',conn , if_exists='replace',index='False')
print("Leaderboard DataFrame written to SQL.")

# 5. Verify write: Read leaderboard back from SQL
print("\nRead leaderboard table from SQL:")
df_leaderboard = pd.read_sql('SELECT * FROM customer_leaderboard;',conn)
print (df_leaderboard)

# 6. Large table demo: Read in chunks
print("\nDemo: Reading Customers in chunks of 2 rows:")
for chunk in pd.read_sql("SELECT * FROM Customers;",conn , chunksize = 2):
    print(chunk,end="\n---\n")
    break 
conn.close()
print("Connection closed.")