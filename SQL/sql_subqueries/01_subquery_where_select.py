#  Subqueries in WHERE and SELECT (Scalar, IN, EXISTS)
'''A subquery (also called an inner query or nested query), A subquery is a “query inside a query.” It’s a way to use the result of one SQL query as input for another—either to compare a single value (scalar subquery), match against a list (IN), or check for existence (EXISTS). '''
'''Key Concepts/Topics:
Scalar Subquery: Returns a single value, can be used like a variable in your outer query.
Subquery in WHERE ... IN (...): Restricts your outer query to values returned from the inner query.
EXISTS / NOT EXISTS: Checks if any row returns from the subquery; often used for "anti-joins" or "filter if something exists".
Correlated Subquery: A subquery that refers to columns from the outer query row-by-row. (Advanced, but covered for completeness.)
Operators with Subqueries: =, !=, >, <, >=, <=, IN, NOT IN, EXISTS, NOT EXISTS '''

import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
print("--- SUBQUERIES in WHERE and SELECT ---")
conn = None
try:
    conn=setup_db(DB_FILE)
    cursor = conn.cursor()
    # 1. Scalar Subquery in SELECT: Add average product price to every product row
    print("\n1. Scalar Subquery: Product price and overall average price:")
    cursor.execute("""  SELECT product_name,price,(SELECT AVG(price) FROM Products) AS avaerage_price FROM Products;""")
    for row in cursor.fetchall():
        print(row)
    
    # 2. Scalar Subquery in WHERE: Products that are priced above the average
    print("\n2. Products priced ABOVE the average (using scalar subquery in WHERE):")
    cursor.execute(""" SELECT product_name,price FROM Products WHERE price > (SELECT AVG(price) FROM Products); """)
    for row in cursor.fetchall():
        print(row)

    # 3. Subquery using IN: Customers who have made at least one order
    print("\n3. Customers who have made at least one order (IN subquery):")
    cursor.execute( """ SELECT first_name,last_name FROM Customers WHERE customer_id IN (SELECT DISTINCT customer_id FROM Orders); """)
    for row in cursor.fetchall():
        print(row)
    
    # 4. Subquery using EXISTS: Customers who have at least one order over $500
    print("\n4. Customers who have any order over $500 (EXISTS subquery):")
    cursor.execute(""" SELECT first_name, last_name FROM Customers AS c WHERE EXISTS (SELECT 1 FROM Orders AS o WHERE o.customer_id = c.customer_id AND o.total_amount >500); """)
    for row in cursor.fetchall():
        print(row)
    
    # 5. Correlated Subquery: Products with price above category average
    print("\n5. Correlated subquery: Products with above-average price in their category:")
    cursor.execute(""" SELECT p1.product_name,p1.category,p1.price FROM Products AS p1 WHERE p1.price > (SELECT AVG(p2.price ) FROM Products AS p2 WHERE p2.category = p1.category) ORDER BY p1.category , p1.price DESC; """)
    for row in cursor.fetchall():
        print(row)
except sqlite3.Error as e:
       print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")
        