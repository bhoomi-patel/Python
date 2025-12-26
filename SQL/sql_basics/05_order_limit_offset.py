'''Key Concepts/Topics:
-> ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...: Sorts the result set.
ASC (Ascending): Sorts from lowest to highest (A-Z, 0-9). This is the default.
DESC (Descending): Sorts from highest to lowest (Z-A, 9-0).
-> Multiple Columns: Sorts by the first column specified, then by the second for rows with identical values in the first, and so on.
-> LIMIT number: Restricts the output to a maximum of number rows.
-> OFFSET number: Skips number rows from the beginning of the sorted result set before starting to return rows.
-> Pagination: The technique of displaying a large result set in smaller, manageable pages. ORDER BY, LIMIT, and OFFSET are fundamental for implementing this.
'''
import sqlite3
import os
from connecting_sqlite import setup_db  # import the helper function

DB_FILE = 'example.db'  # Our main database file


print("--- ORDER BY, LIMIT, OFFSET ---")
conn = None
try:
    conn = setup_db(DB_FILE)  # Setup and connect to the database
    cursor = conn.cursor()

    # 1. sort customers by age (youngest first)---
    print("\n1. Customers sorted by age (youngest first):")
    cursor.execute("SELECT first_name,last_name,age FROM Customers ORDER BY age ASC;")
    for row in cursor.fetchall():
        print(row)
    # 2. Products sorted by price (highest first) ---
    print("\n2. Products sorted by price (highest first):")
    cursor.execute("SELECT product_name,price FROM Products ORDER BY price DESC;")
    for row in cursor.fetchall():
        print(row)
    # 3.TOP 3 products with highest inventory ---
    print("\n3. Top 3 products with highest inventory:")
    cursor.execute("SELECT product_name,stock_quantity FROM Products ORDER BY stock_quantity DESC LIMIT 3;")
    for row in cursor.fetchall():
        print(row)
    # 4. Pagination example: Page 2,3 customers per page ---
    print("\n4. Customers page 2(LIMIT 3 OFFSET 3):")
    cursor.execute("SELECT first_name,city FROM Customers ORDER BY customer_id LIMIT 3 OFFSET 3;")
    for row in cursor.fetchall():
        print(row)

    # -- 5. Multi-column sort: first by city, then by age descending --
    print("\n5. Customers ordered by city, then age descending:")
    cursor.execute("SELECT first_name, city, age FROM Customers ORDER BY city, age DESC;")
    for row in cursor.fetchall(): print(row)

    # ------ Task -------
    '''Select order_id, customer_id, total_amount, and order_date from the Orders table.
    Sort results by total_amount DESCENDING, then by order_date ASCENDING.
    Return only the top 4 highest-value orders (use LIMIT).
    Print the results.'''
    print("\n--- Sort and Limit Orders ---")
    cursor.execute(""" 
     SELECT order_id,customer_id,total_amount,order_date From Orders ORDER BY total_amount DESC,order_date ASC LIMIT 4;""")
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")