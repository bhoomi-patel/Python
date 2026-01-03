'''Key Concepts/Topics:

Relational Database (RDBMS): Stores data in tables with relationships.
SQL (Structured Query Language): The universal language for RDBMS.
SQLite: A self-contained, serverless, zero-configuration SQL database engine (just a .db file).
sqlite3.connect(): Python function to open a connection to an SQLite database file (creates it if it doesn't exist).
Connection Object (conn): Represents the active link to the database. Essential for managing transactions.
Cursor Object (cursor): An object used to execute SQL queries and fetch results from the database.
cursor.execute(sql_query): Runs a single SQL command.
conn.commit(): Crucial! Saves any changes (like INSERT, UPDATE, DELETE, CREATE TABLE) permanently to the database file. Without commit(), changes are temporary.
conn.close(): Closes the database connection. Good practice to always close.
cursor.fetchone() / cursor.fetchall(): Methods to retrieve query results.
fetchone(): Retrieves the next single row of a query result set.
fetchall(): Retrieves all remaining rows of a query result set.'''
# install --> pip install sqlite3
import sqlite3
import os
import datetime

# --- Configuration ---
DB_FILE = 'example.db'  # Our main database file 
def setup_db(db_file = DB_FILE):
    if os.path.exists(db_file):
        os.remove(db_file) # Remove old db for a clean start
        print(f"Removed existing database file: {db_file}")

    conn = sqlite3.connect(db_file)  # Connect to (or create) the database file
    cursor = conn.cursor()  # Create a cursor object to execute SQL commands
    print(f"Connected to database: {db_file}")

    # create customers table
    cursor.execute(''' CREATE TABLE IF NOT EXISTS Customers(customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER,
    city TEXT,
    registration_date TEXT DEFAULT CURRENT_DATE,
    status TEXT DEFAULT 'active'); ''')

    # create products table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT,
    price REAL NOT NULL,
    stock_quantity INTEGER DEFAULT 0
     );
    """)
     # Create Orders table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL, -- YYYY-MM-DD
    total_amount REAL NOT NULL,
    status TEXT DEFAULT 'pending',
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
    );
    """) 
        # Create Order_Items table (details of each item in an order)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Order_Items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    item_price REAL NOT NULL,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
    );
    """)
    conn.commit()  # Save changes
    print("Database setup complete with tables: Customers, Products, Orders, Order_Items.")
    # Insert Sample Data into Customers
    customers_data = [
    ("Alice", "Smith", "alice@example.com", 30, "New York", "2022-01-15"),
    ("Bob", "Johnson", "bob@example.com", 24, "Los Angeles", "2022-03-20"),
    ("Charlie", "Brown", "charlie@example.com", 35, "New York", "2022-05-01"),
    ("David", "Lee", "david@example.com", 28, "Chicago", "2022-07-10"),
    ("Eve", "Davis", "eve@example.com", 40, "Los Angeles", "2022-09-05"),
    ("Frank", "White", "frank@example.com", 40, "New York", "2022-11-11"),
    ("Grace", "Taylor", "grace@example.com", 22, "Miami", "2023-01-01")
        ]
    cursor.executemany("INSERT INTO Customers (first_name, last_name, email, age, city, registration_date) VALUES (?, ?, ?, ?, ?, ?);", customers_data)

    # Insert Sample Data into Products
    products_data = [
    ("Laptop Pro X", "Electronics", 1200.00, 50),
    ("Wireless Mouse", "Electronics", 25.50, 200),
    ("Mechanical Keyboard", "Electronics", 75.00, 100),
    ("Desk Chair Ergo", "Furniture", 250.00, 20),
    ("Coffee Mug AI", "Home Goods", 12.00, 300),
    ("Notebook Pro (A4)", "Office Supplies", 5.50, 150),
    ("USB-C Hub", "Electronics", 40.00, 80)
    ]
    cursor.executemany("INSERT INTO Products (product_name, category, price, stock_quantity) VALUES (?, ?, ?, ?);", products_data)

    # Insert Sample Data into Orders (Customer IDs 1-7)
    orders_data = [
    (1, "2023-01-10", 1212.00, "completed"),  # Alice bought Laptop+Mug
    (2, "2023-01-11", 250.00, "completed"),   # Bob bought Desk Chair
    (1, "2023-01-12", 75.00, "pending"),     # Alice bought Keyboard
    (3, "2023-01-15", 12.00, "completed"),    # Charlie bought Mug
    (2, "2023-01-16", 25.50, "shipped"),     # Bob bought Mouse
    (4, "2023-01-18", 1200.00, "completed"),  # David bought Laptop Pro
    (5, "2023-01-20", 5.50, "pending"),     # Eve bought Notebook
    (6, "2023-01-21", 150.00, "completed"),   # Frank bought something
    (1, "2023-01-22", 40.00, "completed"),    # Alice bought USB-C Hub
    (7, "2023-02-01", 12.00, "pending")      # Grace bought Coffee Mug
     ]
    cursor.executemany("INSERT INTO Orders (customer_id, order_date, total_amount, status) VALUES (?, ?, ?, ?);", orders_data)

    # Insert Sample Data into Order_Items
    order_items_data = [
    (1, 1, 1, 1200.00), (1, 5, 1, 12.00), # Order 1: Laptop, Mug
    (2, 4, 1, 250.00),                    # Order 2: Desk Chair
    (3, 3, 1, 75.00),                     # Order 3: Keyboard
    (4, 5, 1, 12.00),                     # Order 4: Mug
    (5, 2, 1, 25.50),                     # Order 5: Mouse
    (6, 1, 1, 1200.00),                   # Order 6: Laptop
    (7, 6, 1, 5.50),                      # Order 7: Notebook
    (8, 3, 2, 75.00),                     # Order 8: 2 Keyboards (item_price is per unit)
    (9, 7, 1, 40.00),                     # Order 9: USB-C Hub
    (10, 5, 1, 12.00)                     # Order 10: Coffee Mug
    ]
    cursor.executemany("INSERT INTO Order_Items (order_id, product_id, quantity, item_price) VALUES (?, ?, ?, ?);", order_items_data)

    conn.commit()
    print("Sample data inserted into tables.")
    return conn
# --- Main Script Execution ---
print("Setting up the database...")
conn = None # Initialize connection variable to None
try:
    conn = setup_db()  # Setup database and get connection
    # 1. Execute a simple test query (e.g., to get SQLite version)
    cursor = conn.cursor()
    cursor.execute("SELECT sqlite_version();")
    version = cursor.fetchone()[0] # fetchone() returns a tuple, get first element
    print(f"\nSQLite Version: {version}")
    # 2. Verify table creation by listing tables
    print("\nTables created in the database:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ;")
    tables = cursor.fetchall()
    for table in tables:
        print(f"- {table[0]}")

    print("\nInitial database setup complete.")
except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    # 3. Close the connection
    if conn:
        conn.close()
        print("\nDatabase connection closed.")