# Data Definition Language (DDL): CREATE TABLE and Table Constraints
'''Data Definition Language (DDL) commands are used to define, modify, or delete the structure (schema) of your database. The CREATE TABLE statement is the primary DDL command for building new tables, and table constraints are rules applied to columns that ensure data integrity and prevent invalid data from being stored.'''
'''CREATE TABLE is the SQL command for creating a new collection (table) of structured data.
Each column has a data type and constraints (rules about what values are allowed), such as PRIMARY KEY, NOT NULL, UNIQUE.
--> Key Concepts & Topics
Table and Column Names: Must be unique within the database, and clear.
Data Types: e.g., INTEGER, TEXT, REAL.
Constraints:
PRIMARY KEY: Uniquely identifies each row (cannot be NULL/duplicates).
NOT NULL: Value required in this column.
UNIQUE: All values must be different in this column (good for emails, product SKUs).
DEFAULT: If not specified, what to insert by default.
CHECK: Custom rule (e.g., salary > 0).
FOREIGN KEY: References a primary key in another table (to link tables).
AUTOINCREMENT: For auto-incrementing integer IDs.
DROP TABLE: Removes the whole table (use with caution!).'''
import sqlite3
import os
DB_FILE = 'example.db'  # Our main database file
if os.path.exists(DB_FILE):
    os.remove(DB_FILE) # Remove old db for a clean start
    print(f"Removed existing database file: {DB_FILE}")
# connect and create cursor
conn = sqlite3.connect(DB_FILE)  # Connect to (or create) the database file
cursor = conn.cursor()  # Create a cursor object to execute SQL commands
# 1. Create a properly-constrained products table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT,
    price REAL NOT NULL CHECK(price >= 0),
    stock_quantity INTEGER DEFAULT 0 CHECK(stock_quantity >= 0)
);
""")
print("Table 'products' created.")
# 2. Create a customers table with constraints
cursor.execute(''' CREATE TABLE IF NOT EXISTS Customers(
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER CHECK(age >= 0),
    city TEXT,
    registration_date TEXT DEFAULT CURRENT_DATE
); ''')
print("Table 'customers' created.")
# 3. Drop old temp table (safe cleanup)
cursor.execute("DROP TABLE IF EXISTS TempData;")
print("Dropped table 'TempData' if it existed.")

conn.commit()  # Save changes
conn.close()  # Close the connection