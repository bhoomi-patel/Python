# Ranking Window Functions: ROW_NUMBER(), RANK(), DENSE_RANK(), NTILE()
'''Simple Definition: Ranking window functions assign a numerical rank, row number, or percentile group to each row within a defined window (either the entire result set or specific partitions). They are essential for ordering and prioritizing data based on certain criteria, without collapsing the individual rows.'''

import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
conn = setup_db(DB_FILE)
cursor = conn.cursor()
# 1. ROW_NUMBER()
'''Assigns a unique, sequential number to each row within the result set (or partition of rows), according to the order specified.'''
print("\nROW_NUMBER(): Top products per category")
sql = """ SELECT category,product_name,price,ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) as category_rank FROM Products ORDER BY category,category_rank; """
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)

# 2. RANK()
'''Same as ROW_NUMBER(), except that for ties (e.g., two products with same price), both get the same rank, and the next number(s) are skipped.'''
print("\nProducts with RANK() per category (ties share rank, next number skipped):")
sql2 = """ SELECT category , product_name,price,RANK() OVER(PARTITION BY category ORDER BY price DESC) AS category_rank FROM Products ORDER BY category,category_rank,product_name; """
cursor.execute(sql2)
for row in cursor.fetchall():
    print(row)

# 3. DENSE_RANK()
'''Almost like RANK(), but with no skipping of ranks after ties. So, ties share a number, and the next in line gets the next sequential rank (no gaps).'''
print("\nProducts with DENSE_RANK() per category (ties share rank, NO gaps):")
sql3 = """ SELECT category,product_name,price,DENSE_RANK() OVER(PARTITION BY category ORDER BY price DESC) AS category_rank FROM Products ORDER BY category,category_rank,product_name; """
cursor.execute(sql3)
for row in cursor.fetchall():
    print(row)

# 4. NTILE(N)
'''NTILE(N) divides the rows within its partition (or the entire result set) into N groups (buckets) and assigns a number (from 1 to N) to each row, indicating which group it belongs to. The groups are as equal in size as possible.'''
print("\n1. Customers divided into 3 age-based terciles:")
sql4= """  SELECT first_name,age,NTILE(3) OVER (ORDER BY age ASC) AS age_tercile FROM Customers ORDER BY age,first_name; """
cursor.execute(sql4)
for row in cursor.fetchall():
    print(row)

conn.close()