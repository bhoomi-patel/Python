# LEFT JOIN, RIGHT JOIN, and Anti-Joins
'''
-> LEFT JOIN (LEFT OUTER JOIN): Returns all rows from the “left” table, and the matching rows from the right table. If there’s no match on the right, SQL fills in NULLs for those columns.
-> RIGHT JOIN (RIGHT OUTER JOIN): (Not directly in SQLite, but we’ll conceptually cover it.) Returns all rows from the "right" table, and the matching ones from the left. If no left match, fills in NULLs for left columns.
-> Anti-Join: A very common use case for LEFT JOIN is to identify records in one table that do not have a corresponding entry in another table. This is done by performing a LEFT JOIN and then filtering WHERE right_table.key IS NULL.
Key Concepts/Topics:
- Left Table: The table before LEFT JOIN.
- Right Table: The table after LEFT JOIN.
- NULL Filling: If no match is found in the right table, those columns are NULL.
- Anti-Join: Find records from one table not present in another (LEFT JOIN ... WHERE right.col IS NULL).
- (In SQLite, no built-in RIGHT JOIN. To simulate it, swap the order of tables in a LEFT JOIN.)
'''
import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
print("--- LEFT JOIN, RIGHT JOIN, and Anti-Joins ---")

conn = None
try:
    conn = setup_db(DB_FILE)
    cursor = conn.cursor()
    # 1. LEFT JOIN: All customers with their orders (even customers with NO orders!)
    print("\n1. All customers and their orders (LEFT JOIN):")
    cursor.execute(""" SELECT c.customer_id,c.first_name,o.order_id,o.order_date FROM Customers AS c 
    LEFT JOIN Orders AS o ON c.customer_id = o.customer_id ORDER BY c.customer_id, o.order_id; """) 
    for row in cursor.fetchall():
        print(row)
    # 2. Anti-Join: Customers who have NEVER placed an order (no match found)
    print("\n2. Customers with NO orders (anti-join pattern):")
    cursor.execute("""
        SELECT c.customer_id, c.first_name, c.last_name
        FROM Customers AS c
        LEFT JOIN Orders AS o ON c.customer_id = o.customer_id
        WHERE o.order_id IS NULL;
    """)
    for row in cursor.fetchall():
        print(row)
    # 3. RIGHT JOIN (conceptual in SQLite): Find orders without a matching customer (should not happen if FK is enforced)
    print("\n3. Simulated RIGHT JOIN: (Orders with no matching customer):")
    cursor.execute("""
        SELECT o.order_id, o.customer_id, c.first_name
        FROM Orders AS o
        LEFT JOIN Customers AS c ON o.customer_id = c.customer_id
        WHERE c.customer_id IS NULL;
    """)
    for row in cursor.fetchall():
        print(row)  # Typically empty unless you have dirty/missing FK data

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")