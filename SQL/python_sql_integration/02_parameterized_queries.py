# Parameterized Queries: Protecting Against SQL Injection
'''Parameterized queries are a secure method of executing SQL commands where you keep the SQL code separate from the data values. Instead of building SQL strings by concatenating user inputs or Python variables, you use placeholders in the SQL statement and pass the data values as a separate argument.
This prevents a common and dangerous security vulnerability called SQL Injection.
Parameterized Query: Instead of building SQL by string concatenation (dangerous!), you use placeholders (like ?, %s, or :name) for input values, and pass those values separately to the SQL execution function.
Key Concepts/Topics
SQL Injection: A cyberattack where malicious SQL code is injected into input fields, allowing attackers to trick the database into executing unintended commands (e.g., viewing sensitive data, deleting tables, gaining unauthorized access).
Placeholders: Special markers in your SQL query string that indicate where a data value should be inserted.
? (question mark): Common in sqlite3 and psycopg2 (PostgreSQL).
%s (percent s): Used in psycopg2 with execute(query, (val1, val2)).
:name (named parameter): Used in sqlalchemy or cx_Oracle.
cursor.execute(sql_query, (value1, value2, ...)): The Python method for executing parameterized queries. The data values are passed as a tuple (or list/dictionary for named parameters).
Security: Parameterized queries neutralize SQL Injection by treating all input values as literal data, never as executable SQL code.
'''
import pandas as pd
import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'demo.db'
# 1. Setup & connect
conn = setup_db(DB_FILE)
cursor = conn.cursor()

# 1. Secure SELECT with single parameter ("Where city is ?", passed separately)
city_to_find = "New York"
print(f"\nQuerying customers with city = '{city_to_find}' (parameterized):")
cursor.execute("SELECT first_name,last_name,email FROM Customers WHERE city = ?;",(city_to_find,))
for row in cursor.fetchall():
    print(row)

# 2. Secure parameterized UPDATE
new_status = "VIP"
customer_id = 1
print(f"\nParameterized UPDATE: Set status to '{new_status}' for customer_id = {customer_id}")
cursor.execute("UPDATE Customers SET status = ? WHERE customer_id = ?;", (new_status, customer_id))
conn.commit()
cursor.execute("SELECT first_name, status FROM Customers WHERE customer_id = ?;", (customer_id,))
print(cursor.fetchone())

# 3. Parameterized INSERT Example ---
# Always use parameters for INSERTs as well
new_customer_name = "Victor Stone"
new_customer_email = "victor@example.com"
sql_insert_safe = "INSERT INTO Customers (first_name, last_name, email, age, city) VALUES (?, ?, ?, ?, ?);"
print("\nSECURE INSERT (Parameterized) ---")
print(f"SQL: '{sql_insert_safe}'")
cursor.execute(sql_insert_safe, (new_customer_name, "Stone", new_customer_email, 25, "Gotham"))
conn.commit()
print(f"Customer '{new_customer_name}' inserted securely.")

# Verify insertion
cursor.execute("SELECT first_name, email FROM Customers WHERE email = ?;", (new_customer_email,))
print(f"Verified new customer: {cursor.fetchone()}")
customer_id = 1
print(f"\nParameterized UPDATE: Set status to '{new_status}' for customer_id = {customer_id}")
cursor.execute("UPDATE Customers SET status = ? WHERE customer_id = ?;", (new_status, customer_id))
conn.commit()
cursor.execute("SELECT first_name, status FROM Customers WHERE customer_id = ?;", (customer_id,))
print(cursor.fetchone())

# 4. NOT SECURE: Avoid this!
bad_email = "'; DROP TABLE Customers; --"
# DANGEROUS way (don't actually run this!)
print(f"\nInsecure (DO NOT DO THIS!):")
insecure_query = f"SELECT * FROM Customers WHERE email = '{bad_email}';"
print("Insecure query:", insecure_query)
print("If executed, could drop your table if input isn't sanitized! (Don't run in production.)")

# 5. Secure IN with tuple (Python will auto-quote/escape)
print("\nSecure IN clause with tuple of status values:")
statuses = ("VIP", "active")
sql = f"SELECT first_name, status FROM Customers WHERE status IN ({','.join('?' for _ in statuses)});"
cursor.execute(sql, statuses)
print(cursor.fetchall())

conn.close()
print("Connection closed.")