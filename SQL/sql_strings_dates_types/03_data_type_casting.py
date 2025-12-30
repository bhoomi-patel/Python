# Data Type Casting: Using CAST and Type Conversion
'''Data type casting (or type conversion) is the process of explicitly changing the data type of an expression (a column, a literal value, or the result of a function) from one type to another. This ensures that data is stored or processed in the correct format, preventing errors and enabling compatibility with various operations.
Key Concepts/Topics:

Data Types Recap: INTEGER, TEXT, REAL, BLOB (SQLite). Understanding the native type of your data.
CAST(expression AS type): The standard SQL syntax for explicit type conversion. You specify the expression to convert and the target data type.
CONVERT(type, expression): An alternative, non-standard syntax used in some databases like SQL Server and MySQL. (We'll focus on CAST for SQLite/standard SQL).
Implicit vs. Explicit Casting:
Implicit Casting: The database automatically converts data types when it deems it safe and necessary (e.g., INTEGER to REAL in a division, TEXT '123' to INTEGER in a numeric comparison). This can be convenient but sometimes leads to unexpected results or performance issues.
Explicit Casting: You explicitly tell the database to convert the type using CAST(). This is generally safer, clearer, and ensures your intent is met.

Syntax:
CAST(expr AS TYPE)
Examples:
CAST('123' AS INTEGER) = 123
CAST(price AS TEXT) = '19.99'
CAST(order_date AS REAL) (to Julian day in some DBs; see also JULIANDAY())
'''
import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
conn=setup_db(DB_FILE)
cursor = conn.cursor()
# 1. Text Numbers to INTEGER – e.g., after CSV import
print("\nSuppose quantity was imported as string: ")
cursor.execute("SELECT '42' AS quantity_text, CAST('42' AS INTEGER) AS quantity_int; ")
for row in cursor.fetchall():
    print(row)
# 2. Integer Division Issue
print("\nAverage Price (Beware Integer Division!):")
cursor.execute(""" SELECT price,stock_quantity,price/ stock_quantity AS no_cast_avg FROM Products WHERE stock_quantity > 0 LIMIT 1; """)
for row in cursor.fetchall():
    print(row)
print("\nAverage Price FIXED with CAST (real/float):")
cursor.execute(""" SELECT price,stock_quantity,price/CAST(stock_quantity AS REAL)AS avg_per_unit FROM Products WHERE stock_quantity >0 limit 1; """)
for row in cursor.fetchall():
    print(row)
# 3. Formatting money for reporting
print("\nFormat price as string with units:")
cursor.execute(""" SELECT product_name,price,'$' || CAST(price AS TEXT) AS price_label FROM Products LIMIT 3; """)
for row in cursor.fetchall():
    print(row)
# 4. Convert order date to UNIX timestamp integer
print("\nOrder date as UNIX timestamp (INT):")
cursor.execute(""" SELECT order_id,order_date,CAST(STRFTIME('%s',order_date) AS INTEGER) AS order_unix FROM Orders LIMIT 2; """)
for row in cursor.fetchall():
    print(row)
# 5. Quick demo: Numeric test (does customer_id > '3' work?)
print("\nDo comparisons between column types work (customer_id > '3')?")
cursor.execute("SELECT customer_id,first_name FROM Customers WHERE customer_id > '3' ;")
for row in cursor.fetchall():
    print(row)

conn.close()
print("Database connection closed.")