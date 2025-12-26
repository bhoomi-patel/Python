'''SELECT is used to fetch data (columns/rows) from tables.
WHERE is used to filter those results—show only the rows that match certain rules.'''
'''-> SELECT column1, column2, ...: Specifies which columns to retrieve.
-> SELECT *: A wildcard to retrieve all columns from the table.
-> FROM table_name: Specifies the table(s) from which to retrieve data.
-> WHERE condition: Filters rows based on a specified condition (or conditions).
-> Comparison operators: =, !=, >, <, >=, <= 
-> Logical Operators:
AND: Combines two or more conditions; all must be true.
OR: Combines two or more conditions; at least one must be true.
NOT: Negates a condition (e.g., NOT status = 'active' is same as status != 'active').
-> Pattern Matching:
LIKE: Used to search for a specified pattern in a column.
%: Wildcard representing zero, one, or multiple characters.
_: Wildcard representing a single character. 
-> List Matching:
IN (value1, value2, ...): Matches if a column's value is in a specified list of values.
NOT IN (value1, value2, ...): Matches if a column's value is not in a specified list of values.
-> Range Matching:
BETWEEN value1 AND value2: Matches if a column's value is within a specified inclusive range.
NOT BETWEEN value1 AND value2: Matches if a column's value is not within a specified inclusive range.
-> NULL Value Checking:
IS NULL: Checks if a column's value is NULL (empty/missing).
IS NOT NULL: Checks if a column's value is NOT NULL.'''

import sqlite3
from connecting_sqlite import setup_db  # import the helper function

DB_FILE = 'example.db'  # Our main database file
conn = setup_db(DB_FILE)  # Setup and connect to the database
cursor = conn.cursor()
print ("--- data query language ---")

# see all the customers
print("\n All Customers:")
cursor.execute("SELECT * FROM Customers;")
for row in cursor.fetchall():
    print(row)

#  1. select all columns from products
print("\n1. All Products:")
cursor.execute("SELECT * FROM Products;")
for row in cursor.fetchall():
    print(row)

# 2. select specific columns,filter where price > 100
print("\n2. Expensive products (price > 100):")
cursor.execute("SELECT product_name, price FROM Products WHERE price > 100;")
for row in cursor.fetchall():
    print(row)

# 3. where using and/or/in
print("\n3. Products that are 'Electronics' and price < 100:")
cursor.execute("SELECT product_name, category, price FROM Products WHERE category = 'Electronics' AND price < 100;")
for row in cursor.fetchall():
    print(row)

# 4. where using between
print("\n4. Orders placed between 2023-01-12 and 2023-01-20:")
cursor.execute("SELECT order_id, customer_id, order_date FROM Orders WHERE order_date BETWEEN '2023-01-12' AND '2023-01-20';")
for row in cursor.fetchall(): 
    print(row)

# 5. Pattern matching with LIKE
print("\n5. Customers with email ending in 'example.com':")
cursor.execute("SELECT first_name, email FROM Customers WHERE email LIKE '%@example.com';")
for row in cursor.fetchall(): 
    print(row)



# -------- Task ---------
'''Task:

Show product_name and price for all Products in the "Electronics" or "Home Goods" categories with price between $10 and $200.
Show all Orders where the status is not 'completed'.'''

print("\nProducts in 'Electronics' or 'Home Goods', $10-$200:")
cursor.execute(" SELECT product_name,price from Products WHERE category IN('Electronics','Home Goods') AND price BETWEEN 10 AND 200; ")
for row in cursor.fetchall():
    print(row)
print("\nOrders with status not 'completed':")
cursor.execute("SELECT order_id,status FROM Orders WHERE status != 'completed'; ")
for row in cursor.fetchall():
    print(row)

conn.close()
print("\ndatabase connection closed.")