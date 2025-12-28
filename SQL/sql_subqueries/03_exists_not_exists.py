# Subqueries with EXISTS and NOT EXISTS
'''EXISTS(subquery): Outer row is kept if the subquery returns at least one row for it.
NOT EXISTS(subquery): Outer row is kept if the subquery returns NO rows for it.
Correlated Subquery: The subquery can “see” a value from the outer query and uses it in its WHERE clause.
Short-circuit logic: As soon as EXISTS finds one row, it’s TRUE (doesn’t count all of them—makes it efficient).'''

# ---- Based on Problem ---
''' Find all customers who have placed at least one order (EXISTS)
Find all customers who have never placed any order (NOT EXISTS)
Find all products that have never been sold (NOT EXISTS + anti-join pattern)'''

import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
print("--- SUBQUERIES with EXISTS and NOT EXISTS ---")
conn = None
try:
    conn=setup_db(DB_FILE)
    cursor = conn.cursor()
    
    # 1. Customers who have placed at least one order (EXISTS)
    print("\n1. Customers who have placed at least one order (using EXISTS):")
    cursor.execute("""
        SELECT c.customer_id, c.first_name, c.last_name
        FROM Customers AS c
        WHERE EXISTS (
            SELECT 1 FROM Orders AS o WHERE o.customer_id = c.customer_id
        )
        ORDER BY c.customer_id;
    """)
    for row in cursor.fetchall():
        print(row)
    
    # 2. Customers who have NEVER placed an order (NOT EXISTS)
    print("\n2. Customers who have NEVER placed an order:")
    cursor.execute("""
        SELECT c.customer_id, c.first_name, c.last_name
        FROM Customers AS c
        WHERE NOT EXISTS (
            SELECT 1 FROM Orders AS o WHERE o.customer_id = c.customer_id
        )
        ORDER BY c.customer_id;
    """)
    for row in cursor.fetchall():
        print(row)
    
    # 3. Products NEVER ordered (using NOT EXISTS)
    print("\n3. Products that have NEVER been ordered (never in Order_Items):")
    cursor.execute("""
        SELECT p.product_id, p.product_name
        FROM Products AS p
        WHERE NOT EXISTS (
            SELECT 1 FROM Order_Items AS oi WHERE oi.product_id = p.product_id
        )
        ORDER BY p.product_id;
    """)
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")