# LEAD() and LAG(): Accessing Previous and Next Rows
'''
-> LAG(column, N) OVER (ORDER BY ...)
For each row, get the value of the column from N rows “before” (earlier in the order).
-> LEAD(column, N) OVER (ORDER BY ...)
For each row, get the value of the column from N rows “after” (later in the order).'''

import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
conn=None
try:
    conn = setup_db(DB_FILE)
    cursor = conn.cursor()
    print("\n1. Order amounts and difference from previous order (per customer):")
    sql = """ SELECT order_id,customer_id,order_date,total_amount,LAG(total_amount,1,0) OVER(PARTITION BY customer_id ORDER BY order_date,order_id) AS previous_order_amount,total_amount - LAG(total_amount,1,0) OVER(PARTITION BY customer_id ORDER BY order_date,order_id) AS amount_diff_from_prev FROM Orders ORDER BY customer_id,order_date,order_id; """
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")

# Window Frames: Controlling the Window's Size
'''Window frames (specified within the OVER() clause, after ORDER BY) give you fine-grained control over which rows are included in the calculation of a window function relative to the current row. This is essential for calculating rolling/moving averages, sums, etc. over a dynamic subset of rows.'''
'''
Key Concepts:
-> Default Frame: When ORDER BY is present, the default frame is RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW. This means it includes all rows from the start of the partition up to the current row (inclusive), which is why SUM() OVER(ORDER BY ...) gives a running total.
   -> ROWS BETWEEN start AND end: Defines the frame by a fixed number of rows.
   -> UNBOUNDED PRECEDING: From the very first row in the partition.
   -> N PRECEDING: N rows before the current row.
   -> CURRENT ROW: Just the current row.
   -> N FOLLOWING: N rows after the current row.
   -> UNBOUNDED FOLLOWING: To the very last row in the partition.
-> RANGE BETWEEN start AND end: Defines the frame based on a range of values in the ORDER BY column. Less common for beginners than ROWS.'''

import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
conn=None
try:
    conn = setup_db(DB_FILE)
    cursor = conn.cursor()
    print("\n2. 3-Order Moving Average of total_amount per customer:")
    sql = """ SELECT order_id,customer_id,order_date,total_amount,AVG(total_amount) OVER(PARTITION BY customer_id ORDER BY order_date,order_id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW ) AS last_3_orders_avg_amount FROM Orders ORDER BY customer_id,order_date,order_id; """
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")

# NTILE(N): Dividing into Buckets (Advanced Examples)
'''NTILE(N) divides the rows within its partition (or the entire result set) into N groups (buckets) as equally sized as possible and assigns a group number (from 1 to N) to each row. This is powerful for segmentation and percentile analysis.'''
import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
conn=None
try:
    conn = setup_db(DB_FILE)
    cursor = conn.cursor()
    print("\n3. Customers divided into 4 spending quartiles (based on total spending):")
    sql = """
        WITH CustomerSpending AS (
            SELECT
                customer_id,
                SUM(total_amount) AS total_customer_spend
            FROM Orders
            GROUP BY customer_id
        )
        SELECT
            cs.customer_id,
            c.first_name,
            cs.total_customer_spend,
            NTILE(4) OVER(ORDER BY cs.total_customer_spend DESC) AS spending_quartile
        FROM CustomerSpending AS cs
        INNER JOIN Customers AS c ON cs.customer_id = c.customer_id
        ORDER BY spending_quartile, cs.total_customer_spend DESC;
    """
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")

# Combining Window Functions with CTEs (Best Practice Recap)
'''For complex queries involving multiple window functions, intermediate results, or filtering based on window function output, using Common Table Expressions (CTEs) is a highly recommended best practice. CTEs break down complex logic into readable, named, and reusable steps.'''
import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
conn=None
try:
    conn = setup_db(DB_FILE)
    cursor = conn.cursor()
    print("\n4. Customers with orders having increased total_amount from previous order (using CTE + LAG):")
    sql = """
        WITH OrderComparison AS (
            SELECT
                order_id,
                customer_id,
                order_date,
                total_amount,
                LAG(total_amount, 1, 0) OVER(
                    PARTITION BY customer_id
                    ORDER BY order_date, order_id
                ) AS previous_order_amount
            FROM Orders
        )
        SELECT
            oc.order_id,
            oc.customer_id,
            c.first_name,
            oc.order_date,
            oc.total_amount,
            oc.previous_order_amount
        FROM OrderComparison AS oc
        INNER JOIN Customers AS c ON oc.customer_id = c.customer_id
        WHERE oc.total_amount > oc.previous_order_amount
        ORDER BY oc.customer_id, oc.order_date;
    """
    cursor.execute(sql)
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")