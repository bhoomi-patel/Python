# Indexes, Query Planning, and EXPLAIN (SQL Optimization)
'''-> An index is a special data structure that allows the database engine to quickly find rows without scanning the entire table. It’s very much like the index in the back of a book—you can jump straight to the right “page” instead of flipping linearly through every page.
-> The EXPLAIN command shows you what “plan” the SQL engine intends to use to retrieve your data—helping you detect slow queries before they burn your CPU.
-> Query optimization is the practice of designing efficient queries with the help of indexes, using key best practices and the output of EXPLAIN.'''
'''
Key Concepts/Topics
-> CREATE INDEX: Builds an index on one or more columns.
-> Unique Index: Ensures no two rows have the same value in that (those) column(s).
-> Single Column vs. Composite Index: One column vs. multiple columns combined.
-> Using EXPLAIN: EXPLAIN QUERY PLAN SELECT ... shows if your query uses an index, scans the whole table, and what order join operations happen.
-> When to use indexes: On columns used for frequent searches, joins, sorting, or unique constraints. Not needed for small static tables, or on columns rarely filtered/searched.
-> Index drawback:
   -> Takes up space : Slightly slows down writes (INSERT/UPDATE), but dramatically speeds up queries/reads.
'''
import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
conn = setup_db(DB_FILE)
cursor = conn.cursor()
try:
    # 1. Create an index on Customers.email (often searched)
    print("\n1. Create index on Customers.email:")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_customers_email ON Customers(email);")
    conn.commit()
    print("Index created: idx_customers_email\n")
    # 2. See all indexes in the database
    print("2. Show all indexes:")
    cursor.execute("PRAGMA index_list('Customers');")
    for row in cursor.fetchall():
        print(row)
   # 3. Compare EXPLAIN plans: with and without index
    print("\n3. EXPLAIN QUERY PLAN for SELECT with indexed column:")
    query = "SELECT * FROM Customers WHERE email = 'alice@example.com';"
    cursor.execute(f"EXPLAIN QUERY PLAN {query}")
    explain_result = cursor.fetchall()
    for row in explain_result:
        print(row)
   # 4. EXPLAIN for a slow query: missing index (full table scan)
    print("\n4. EXPLAIN QUERY PLAN for SELECT with unindexed column (city):")
    query2 = "SELECT * FROM Customers WHERE city = 'New York';"
    cursor.execute(f"EXPLAIN QUERY PLAN {query2}")
    for row in cursor.fetchall():
        print(row)

    # 5. Create composite index for faster multi-column searches (customer_id in Orders)
    print("\n5. Create index on Orders(customer_id, order_date):")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_orders_customer_date ON Orders(customer_id, order_date);")
    conn.commit()
    print("Index created: idx_orders_customer_date")

    # 6. See effect in EXPLAIN for a JOIN
    print("\n6. EXPLAIN QUERY PLAN for JOIN using indexed columns:")
    join_query = """
        SELECT o.order_id, c.first_name
        FROM Orders AS o
        JOIN Customers AS c ON o.customer_id = c.customer_id
        WHERE o.order_date >= '2023-01-15'
    """
    cursor.execute(f"EXPLAIN QUERY PLAN {join_query}")
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    conn.close()
    print("Database connection closed.")