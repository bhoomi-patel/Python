# Subqueries in FROM (Derived Tables) and common table expressions(ctes)
'''Subquery in FROM (Derived Table): Embed a SELECT statement as if it were a table in your FROM clause. You must give it an alias. This lets you do multi-stage queries on query results.
CTE (WITH Clause): A way to define a reusable, temporary "mini-table" (or even several) at the start of your SQL query, making multi-step operations and several references to the same logic much easier to write/read.'''
'''Key Concepts/Topics:
-> Derived Table: FROM (SELECT ...) AS t—think of the inner query as producing a table "on the fly".
-> CTE Syntax:WITH cte_name AS (SELECT ... )
           SELECT * FROM cte_name
-> Multiple CTEs: WITH cte1 AS (...), cte2 AS (...) SELECT ... FROM cte1 JOIN cte2 ...              
-> Recursive CTEs: Used for hierarchical/tree structures or rolling totals (bonus: not primary focus today).
-> Readability: CTEs make very long queries much more understandable (like naming steps in Python functions).'''

import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
print("--- SUBQUERIES in FROM and CTEs ---")
conn = None
try:
    conn = setup_db(DB_FILE)
    cursor = conn.cursor()

    # 1. Subquery in FROM: Get customers and their total order value, filter by total
    print("\n1. Derived Table (Subquery in FROM) - Customers with total order value > $1000:")
    cursor.execute(""" SELECT cust.customer_id,cust.first_name,summary.total_spent FROM Customers AS cust INNER JOIN (SELECT customer_id,SUM(total_amount) AS total_spent FROM Orders GROUP BY customer_id) AS summary ON cust.customer_id=summary.customer_id WHERE summary.total_spent > 1000 ORDER BY summary.total_spent DESC;""")
    for row in cursor.fetchall():
        print(row)

    # 2. CTE for Same Task (simpler to read and reference)
    print("\n2. CTE - Same Customers with high total order value:")
    cursor.execute("""
        WITH CustomerTotals AS (
            SELECT customer_id, SUM(total_amount) AS total_spent
            FROM Orders GROUP BY customer_id
        )
        SELECT c.customer_id, c.first_name, ct.total_spent
        FROM Customers AS c
        INNER JOIN CustomerTotals AS ct ON c.customer_id = ct.customer_id
        WHERE ct.total_spent > 1000
        ORDER BY ct.total_spent DESC;
    """)
    for row in cursor.fetchall():
        print(row)

    # 3. Multiple CTEs to cleanly build up analytics
    print("\n3. Multiple CTEs: High-Value Orders & Customer Info:")
    cursor.execute("""
        WITH HighOrders AS (
           SELECT order_id, customer_id, total_amount
           FROM Orders
           WHERE total_amount > 1000
        ), CustomerInfo AS (
           SELECT customer_id, first_name, city FROM Customers
        )
        SELECT h.order_id, h.total_amount, ci.first_name, ci.city
        FROM HighOrders h
        JOIN CustomerInfo ci ON h.customer_id = ci.customer_id
        ORDER BY ci.first_name;
    """)
    for row in cursor.fetchall():
        print(row)

    # 4. (Bonus) Recursive CTE: Generate numbers 1 to 5 (simple demo)
    print("\n4. Bonus: Recursive CTE to generate numbers 1 to 5:")
    cursor.execute("""
        WITH RECURSIVE numbers(n) AS (
            SELECT 1
            UNION ALL
            SELECT n+1 FROM numbers WHERE n < 5
        )
        SELECT n FROM numbers;
    """)
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")