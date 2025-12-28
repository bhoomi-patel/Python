#  Window Functions Basics
'''Window functions are a powerful SQL feature that allows you to perform calculations across a set of table rows that are somehow "related" to the current row. This "set of rows" is called a "window." Crucially, unlike standard aggregate functions (like SUM with GROUP BY) which collapse multiple rows into a single summary row, window functions return a value for each individual row, but that value is computed from its specific "window." '''
''' Key Concepts/Topics:
-> OVER() Clause: This is the syntax that defines the window (the set of rows) over which the window function operates. Every window function must have an OVER() clause.
-> PARTITION BY column(s): (Optional) This divides the entire result set into smaller, independent groups or "partitions." When PARTITION BY is used, the window function applies its calculation separately within each partition. It's similar to GROUP BY but does not collapse rows.
-> ORDER BY column(s): (Optional) This specifies the order of rows within each partition. This is critical for "running" or "cumulative" calculations (like running totals or rankings), as it defines the sequence in which the window expands.'''
''' Window Function Types (covered in this and upcoming files):
-> Aggregate Window Functions: Standard aggregates like SUM() OVER(), AVG() OVER(), COUNT() OVER(), MIN() OVER(), MAX() OVER() used in a window context.
-> Ranking Window Functions: ROW_NUMBER(), RANK(), DENSE_RANK(), NTILE() (covered in 02_rank_dense_rank_row_num.py).
-> Analytic Window Functions: LEAD(), LAG(), FIRST_VALUE(), LAST_VALUE() (covered in 03_lead_lag_ntile_frames.py).
-> Crucial Difference from GROUP BY:
-> GROUP BY collapses rows: If you GROUP BY category, you get one row per category. You lose the individual product details.
Window functions do not collapse rows: You get all the original rows, but with an additional calculated column attached to each row. This calculated column's value is derived from the "window" of related rows. '''

import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
conn = setup_db(DB_FILE)
cursor = conn.cursor()

# 1. Show each order amount, AND the "total so far" (running total):
print("\nRunning total of all orders (ordered by date):")
sql = """
SELECT
    order_id,
    order_date,
    total_amount,
    -- Running/cumulative sum of total_amount from the very first row up to this row!
    SUM(total_amount) OVER(ORDER BY order_date, order_id) AS running_revenue
FROM Orders
ORDER BY order_date, order_id;
"""
cursor.execute(sql)
for row in cursor.fetchall():
    print(row)

# 2. Per-Group Running (Using PARTITION BY)
# “Show for every customer: each order, how much they spent up to that order.”
print("\nRunning total of orders PER CUSTOMER (ordered by date):")
sql2 = """ SELECT
    order_id,
    customer_id,
    total_amount,
    SUM(total_amount) OVER(PARTITION BY customer_id ORDER BY order_date, order_id) AS running_customer_spend
FROM Orders
ORDER BY customer_id, order_date; """
cursor.execute(sql2)
for row in cursor.fetchall():
    print(row)

# 3. Average Value Comparison using Window Function
# “For every product, compare to the average price in its category.”
print("\nProducts with their category average price:")
sql3 = """ SELECT
    product_id,
    product_name,
    category,
    price,
    AVG(price) OVER(PARTITION BY category) AS avg_category_price
FROM Products
ORDER BY category, product_name;
"""
cursor.execute(sql3)
for row in cursor.fetchall():
    print(row)

conn.close()
