# Aggregation Functions - COUNT , SUM , AVG , MIN , MAX
''' Aggregation functions perform calculations across a group of rows, returning a single value per group (or for the entire table). They are essential for summarizing and understanding large datasets.
Key Concepts/Topics:
-> Aggregation: The process of combining multiple rows of data into a single summary row.
-> COUNT(column) / COUNT(*): Counts the number of rows.
-> COUNT(*): Counts all rows, including those with NULL values in any column.
-> COUNT(column_name): Counts rows where column_name is not NULL.
-> COUNT(DISTINCT column_name): Counts only the unique, non-NULL values in column_name.
-> SUM(column): Calculates the total sum of all non-NULL values in a numeric column.
-> AVG(column): Calculates the average (mean) of all non-NULL values in a numeric column.
-> MIN(column): Finds the minimum value in a column.
-> MAX(column): Finds the maximum value in a column.
Ignoring NULLs: All standard aggregation functions (except COUNT(*)) ignore NULL values in their calculations.
'''
import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'

print("--- SQL Aggregation Functions ---")

conn = setup_db(DB_FILE)
cursor = conn.cursor()

try:
    # 1. Total number of products
    print("\n1. COUNT: How many products are there?")
    cursor.execute("SELECT COUNT(*) FROM Products;")
    print(cursor.fetchone()[0])

    # 2. Total sum of stock_quantity in Products table
    print("\n2. SUM: How many items total in stock?")
    cursor.execute("SELECT SUM(stock_quantity) FROM Products;")
    print(cursor.fetchone()[0])

    # 3. AVG price of products in Electronics
    print("\n3. AVG: What is the average price in Electronics?")
    cursor.execute("SELECT AVG(price) FROM Products WHERE category = 'Electronics';")
    print(f"${cursor.fetchone()[0]:.2f}")

    # 4. MIN/MAX price for all products
    print("\n4. MIN & MAX: Cheapest and most expensive product price:")
    cursor.execute("SELECT MIN(price), MAX(price) FROM Products;")
    min_price,max_price = cursor.fetchone()
    print(f"cheapest: ${min_price:.2f}, Most expensive : ${max_price:.2f}")

except sqlite3.Error as e:
    print(f"Database error: {e}")

finally:
    conn.close()
    print("\nDatabase connection closed.")