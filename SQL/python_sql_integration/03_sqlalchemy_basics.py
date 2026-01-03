# SQLAlchemy: Core and ORM Basics
'''SQLAlchemy is a powerful Python SQL toolkit and Object Relational Mapper (ORM). It allows Python programs to communicate with relational databases efficiently and robustly.
SQLAlchemy is the industry-standard Python toolkit for working with databases. It provides two main ways to use SQL in Python:
-> Core (Engines, Connections, SQL Strings): Control over SQL, robust but familiar to anyone who's used sqlite3.
-> ORM (Object-Relational Mapping): Treat database tables like Python classes/objects, and rows like Python objects—write Python, not SQL, and let SQLAlchemy generate the SQL for you.
Key Concepts/Topics
-> create_engine(): The entry point to SQLAlchemy. It creates an Engine object which is responsible for database communication. The connection string (URL) specifies the database type, user, password, host, and database name.
-> Engine: Represents the database. Handles connection pooling and dialect (how to speak to specific DBs like SQLite, PostgreSQL, MySQL).
-> Connection Object: Obtained from the engine, represents an active session with the database.
-> Textual SQL (text()): A function from sqlalchemy (often aliased as pd.text when used with Pandas) that explicitly marks a string as raw SQL, allowing SQLAlchemy to send it directly to the database.
-> conn.execute(sql_command): Executes a SQL statement via the connection.
-> conn.commit() / conn.rollback(): (With begin() or transaction blocks) Manages transactions for DML/DDL.
-> ORM (Object Relational Mapper) - Basics:
-> Declarative Base: A base class for your Python models that will map to database tables.
-> Column, Integer, String, Float: SQLAlchemy types that map to SQL data types.
-> relationship(): Defines connections between your Python models (e.g., a Customer has many Orders).
-> Session: The primary way to interact with the database through ORM (add objects, query objects, commit changes).
'''
import pandas as pd
import sqlite3
import os
import sys
from sqlalchemy import create_engine, inspect,text,Column,Integer,String,Float
from sqlalchemy.orm import declarative_base,Session
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'demo.db'

# 1. Create an engine (connection factory)
engine = create_engine(f'sqlite:///{DB_FILE}',echo=False,future=True)
print(f"SQLAlchemy engine created. - {engine.url}")

# 2. Core: Read products with raw SQL
with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM Products WHERE price > :min_price"),{"min_price":50.0})
    print("\nProducts with price > $50 (using Core):")
    for row in result:
        print(row)

# 3. With Pandas: can use engine too!
df = pd.read_sql("SELECT * FROM Customers WHERE city LIKE 'NEW%' ",engine)
print("\nCustomers from cities starting with 'New':")
print(df)

# 4. Core: Insert new customer
with engine.begin() as conn: 
    import datetime
    unique_email = f"juli.patel{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}@example.com"
    conn.execute(text("INSERT INTO Customers(first_name,last_name,email,age,city) VALUES (:fn, :ln, :em, :ag, :cty)"),{"fn":"Juli","ln":"Patel","em":unique_email,"ag":22,"cty":"Boston"})
    print("Inserted new customer with Core SQLAlchemy.")

# 5. Executing DDL/DML (e.g., ALTER TABLE)
print("\n2. Altering 'Customers' table (add 'loyalty_status') via SQLAlchemy:")
with engine.connect() as conn:
    try:
        conn.execute(text("ALTER TABLE Customers ADD COLUMN loyalty_status TEXT DEFAULT 'Bronze';"))
        conn.commit()
        print("  'loyalty_status' column added.")
    except Exception as e: # Catch if column already exists
            print(f"  Column 'loyalty_status' likely already exists: {e}")
    conn.execute(text("UPDATE Customers SET loyalty_status = 'GOLD' WHERE customer_id= :id;"),{"id":1})
    conn.commit()
    print("  Customer ID 1 updated to 'Gold' status.")
 # Verify the changes using Pandas (reads from the engine) 
print("\nVerifying 'Customers' table (Pandas read_sql with engine):")
df_customers_updated = pd.read_sql("SELECT customer_id,first_name,loyalty_status FROM Customers WHERE customer_id<=3;",engine)
print(df_customers_updated)

# 6. Inspecting Database Metadata 
# The 'inspect' object can show database structure, useful for dynamic schema analysis
inspector = inspect(engine)
table_names = inspector.get_table_names()
print(f"\n4. Tables in the database (using SQLAlchemy Inspector): {table_names}")
# Example:columns in table
columns_in_customers = inspector.get_columns('Customers')
print(f"  Columns in 'Customers' table:")
for col in columns_in_customers:
        print(f"    - {col['name']} ({col['type']})")
    
# 7. ORM: Define Python classes (“models”) representing tables
Base = declarative_base()
class Product(Base):
     __tablename__ = 'Products'
     product_id = Column(Integer,primary_key=True)
     product_name = Column(String)
     category = Column(String)
     price = Column(Float)
     stock_quantity = Column(Integer)

# 8. ORM: Query with Python syntax
with Session(engine) as session:
     print("\nProducts where stock_quantity > 50 (using ORM):")
     products = session.query(Product).filter(Product.stock_quantity>50).order_by(Product.price.desc()).all()
     for prod in products:
          print(f"{prod.product_id} | {prod.product_name} | {prod.price} | {prod.stock_quantity}")