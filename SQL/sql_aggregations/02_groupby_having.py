# GROUP BY / HAVING
''' The GROUP BY clause is used with aggregation functions to divide the rows of a table into groups based on common values in one or more specified columns. The HAVING clause then filters these groups (after aggregation), similar to how WHERE filters individual rows.
Key Concepts/Topics:
-> GROUP BY column1, column2, ...: Gathers all rows that have identical values in the specified GROUP BY columns into a single summary group. All aggregation functions (e.g., COUNT, SUM, AVG) will then operate on each of these groups independently.
-> Rule for SELECT with GROUP BY: Any column included in the SELECT list that is not part of an aggregation function (like SUM(price)) must also be listed in the GROUP BY clause. This ensures that for every unique group you see, you can also see the corresponding grouping columns.
-> HAVING condition: Filters the groups created by GROUP BY. This is crucial because WHERE cannot contain aggregation functions. HAVING comes after GROUP BY and before ORDER BY.
WHERE vs. HAVING:
-> WHERE filters individual rows before grouping and aggregation. It cannot use aggregation functions.
-> HAVING filters groups after grouping and aggregation. It can use aggregation functions.
-> Order of Clauses: In a SELECT statement, the logical order of clauses is: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY -> LIMIT/OFFSET.
'''
import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
print("--- SQL GROUP BY / HAVING ---")
conn = None
try:
    conn = setup_db(DB_FILE)
    cursor = conn.cursor()
    # 1. GROUP BY one column
    print("\n1. Total orders per customer_id :")
    cursor.execute("SELECT customer_id,COUNT(*) AS num_orders FROM Orders GROUP BY customer_id;")
    for row in cursor.fetchall():
        print(row)

    # 2. GROUP BY multiple columns
    print("\n2. Order count per customer, per status:")
    cursor.execute("SELECT customer_id,status,COUNT(*) AS num_orders FROM Orders GROUP BY customer_id,status ORDER BY customer_id,status;")
    for row in cursor.fetchall():
        print(row)
    
    # 3. Average order value by city (join Customers and Orders)
    print("\n3. Average order value by city:")
    cursor.execute("SELECT c.city, AVG(o.total_amount) as avg_oredr_value FROM Orders o INNER JOIN Customers c ON o.customer_id = c.customer_id GROUP BY c.city;")
    for row in cursor.fetchall():
        print(row)

    # --- 4. HAVING: Only keep cities with at least 2 orders
    print("\n4. Only cities with at least 2 orders (HAVING):")
    cursor.execute("SELECT c.city,COUNT(o.order_id) as num_orders FROM Orders o INNER JOIN Customers c ON o.customer_id = c.customer_id GROUP BY c.city HAVING num_orders >=2 ;")
    for row in cursor.fetchall():
        print(row)

     # --- 5. Sum of sales per product (show only products with more than 1 unit sold) ---
    print("\n5. Sum of quantity per product (only if sold > 1):")
    cursor.execute("""
        SELECT p.product_name, SUM(oi.quantity) as total_qty
        FROM Order_Items oi
        INNER JOIN Products p ON oi.product_id = p.product_id
        GROUP BY oi.product_id
        HAVING total_qty > 1;
    """)
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")