# SELF JOIN, CROSS JOIN, FULL OUTER JOIN
'''
-> SELF JOIN
Joins a table to itself, often used to compare rows within the same table (e.g., hierarchical data, finding records with similar/related attributes).
-> CROSS JOIN
Returns the Cartesian product of two tables: every row in the first table joined to every row in the second. Used rarely, but crucial for generating all combinations.
-> FULL OUTER JOIN (conceptual)
Returns all rows from both tables, matching rows when possible, filling NULLs where there’s no match. (Not supported in SQLite, but we’ll show a simulation.)
'''
'''Key Concepts/Topics:
- Self Join: Requires aliases to distinguish between the two instances of the same table. The ON clause defines the relationship within the table.
- Cross Join: No ON clause is used. It generates a result set where the number of rows is (rows_in_table1 * rows_in_table2). Can be very large!
- Full Outer Join (Conceptual): The union of a LEFT JOIN and a RIGHT JOIN. It's used when you want to see all data from both tables, regardless of whether a match exists. SQLite often requires a workaround using LEFT JOINs and UNION.
- UNION / UNION ALL: (Brief introduction) Combines the result sets of two or more SELECT statements into a single result set. UNION removes duplicates, UNION ALL keeps all rows. Essential for simulating FULL OUTER JOIN.'''

import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
print("--- SELF JOIN, CROSS JOIN, FULL OUTER JOIN ---")
conn = None
try:
    conn = setup_db(DB_FILE)
    cursor = conn.cursor()

    # 1. SELF JOIN: Find pairs of customers from the same city (but not the same person)
    print("\n1. SELF JOIN: Pairs of customers in the same city:")
    cursor.execute("""
        SELECT
            A.first_name || ' ' || A.last_name AS customer_A,
            B.first_name || ' ' || B.last_name AS customer_B,
            A.city
        FROM Customers AS A
        INNER JOIN Customers AS B
            ON A.city = B.city AND A.customer_id < B.customer_id
        ORDER BY A.city, customer_A, customer_B;
    """)
    for row in cursor.fetchall():
        print(row)

    # 2. CROSS JOIN: Every product-category pair (what products could appear with what suppliers, etc.)
    print("\n2. CROSS JOIN: All combinations of city and product category:")
    cursor.execute("""
        SELECT DISTINCT c.city, p.category
        FROM Customers c
        CROSS JOIN Products p
        ORDER BY city, category;
    """)
    for row in cursor.fetchall()[:10]:  # Print only first 10 for display
        print(row)
    

    # 3. FULL OUTER JOIN (simulate using UNION of LEFT and RIGHT joins)
    # Find all product names and order IDs (show products even if never ordered, and orders even if product no longer exists - rare, but concept)
    print("\n3. FULL OUTER JOIN (simulated): All products and their order items, including unmatched on either side:")
    cursor.execute("""
        SELECT p.product_name, oi.order_id
        FROM Products p
        LEFT JOIN Order_Items oi ON p.product_id = oi.product_id
        UNION
        SELECT p.product_name, oi.order_id
        FROM Order_Items oi
        LEFT JOIN Products p ON oi.product_id = p.product_id
        ORDER BY product_name, order_id;
    """)
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")