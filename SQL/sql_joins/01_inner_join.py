# Combining Data with INNER JOIN
'''The INNER JOIN (often just called JOIN) combines rows from two or more tables based on a related column between them. It only returns rows where there is a match in the specified common column(s) in both tables.'''
'''Key Concepts/Topics:
Relational Model: Understanding that data is normalized across multiple tables to reduce redundancy and improve data integrity. JOINs bring these related tables back together.
Common Column(s): Tables are joined based on a column (or set of columns) that exists in both tables and represents a relationship (e.g., customer_id links Customers and Orders). This is often a PRIMARY KEY - FOREIGN KEY relationship.
INNER JOIN table2 ON table1.column = table2.column: The syntax for combining tables.
INNER JOIN: Keyword for the join type.
table2: The second table you want to join.
ON condition: Specifies the matching condition (the common column(s)).
Aliasing Tables (AS): Using short nicknames for tables (Customers AS c) is standard practice in joins to make queries more readable and avoid ambiguity when columns have the same name in different tables (e.g., id vs. customer_id).
Result Set: Contains columns from both tables for all rows where the ON condition is met.'''
'''INNER JOIN Syntax:
SELECT columns
FROM table1
JOIN table2 ON table1.key = table2.key
'''
import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
print("--- SQL INNER JOIN ---")

conn = None
try:
    conn = setup_db(DB_FILE)
    cursor = conn.cursor()

    # 1. Orders with Customer Names
    print("\n1. Orders and their Customer Names:")
    cursor.execute(" SELECT o.order_id , o.order_date , c.first_name , c.last_name , o.total_amount FROM Orders AS o INNER JOIN Customers AS c ON o.customer_id = c.customer_id ORDER BY o.order_id;")
    for row in cursor.fetchall():
        print(row)
    
     # 2. Order Items with Product Details
    print("\n2. Order Items with Product Names and Prices:")
    cursor.execute("""
        SELECT oi.order_id, p.product_name, oi.quantity, oi.item_price
        FROM Order_Items AS oi
        INNER JOIN Products AS p ON oi.product_id = p.product_id
        ORDER BY oi.order_id, p.product_name;
    """)
    for row in cursor.fetchall():
        print(row)

    # 3. Joining Three Tables: Order Info with Customer & Product
    print("\n3. Detailed Orders (Order, Customer, Product, Quantity, Price):")
    cursor.execute("""
        SELECT o.order_id, o.order_date, c.first_name, p.product_name, oi.quantity, oi.item_price
        FROM Orders AS o
        INNER JOIN Customers AS c ON o.customer_id = c.customer_id
        INNER JOIN Order_Items AS oi ON o.order_id = oi.order_id
        INNER JOIN Products AS p ON oi.product_id = p.product_id
        ORDER BY o.order_id, p.product_name;
    """)
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")