# Data Manipulation Language (DML): INSERT, UPDATE, DELETE
'''DML commands are used to manage data within database objects (like tables). They allow you to add new records, change existing data, and remove records. These are the operations that populate and maintain the content of your database.
-> INSERT INTO – Add new rows (records) to a table.
With VALUES to specify the data for each column.
With multiple rows at once (batch insert).
-> UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;: Modifies existing data in one or more rows.
SET clause: Specifies which column(s) to change and their new values.
WHERE clause: CRUCIAL! Specifies which specific rows to update. Without a WHERE clause, the UPDATE statement will affect all rows in the table.
-> DELETE FROM – Remove rows from a table.
Always use WHERE or risk deleting every row!
-> commit() – Save your changes to disk (always after inserting, updating, or deleting!).
WHERE Clause – Filters the rows to be updated or deleted—crucial for data safety!
 '''
import sqlite3
import os
from connecting_sqlite import setup_db # import the helper function

DB_FILE = 'example.db'  # Our main database file
print("--- DML - insert,update,delete ---")

conn = setup_db(DB_FILE)  # Setup and connect to the database
cursor = conn.cursor()  # Create a cursor object to execute SQL commands

try:
    # --- insert 
    cursor.execute(" INSERT INTO Products (product_name, category, price, stock_quantity) VALUES (?, ?, ?, ?); ", ("Laptop", "Electronics", 999.99, 10))
    # insert multiple rows
    new_customers = [("Henry","ford","henry@cars.com",45,"detroit","2023-02-02"),
                     ("will","byers","will@byers.com",40,"san diego","20223-03-11")]
    cursor.executemany(" INSERT INTO Customers (first_name, last_name, email, age, city, registration_date) VALUES (?, ?, ?, ?, ?, ?); ", new_customers)
    conn.commit()  # Save changes
    print("Inserted new product and multiple customers.")

    # --- update
    cursor.execute("UPDATE Products SET price=?,stock_quantity=? WHERE product_name=?;", (899.99,15,"Laptop"))
    conn.commit()
    print("Updated product price and stock quantity.")

    # --- delete
    cursor.execute("DELETE FROM Customers WHERE email = ? ",("henry@cars.com",))
    conn.commit()
    print("Deleted customer with email")

    # print after each step for verification
    cursor.execute("SELECT product_name, price, stock_quantity FROM Products WHERE product_name IN ('Laptop','wireless Mouse');")
    print("\nProduct Verification:")
    for row in cursor.fetchall():
        print(row)
    cursor.execute("SELECT first_name, last_name, email FROM Customers;")
    print("\nCustomers Verification:")
    for row in cursor.fetchall():
        print(row)
finally:
    conn.close()
    print("\ndatabase connection closed.")