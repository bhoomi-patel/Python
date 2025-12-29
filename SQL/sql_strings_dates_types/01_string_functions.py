# String Functions: Cleaning, Searching, and Transforming Text Data
'''String functions in SQL allow you to manipulate, analyze, and clean up text data inside your queries. This includes changing case (upper/lower), measuring length, extracting substrings, replacing text, trimming whitespace, searching for patterns, and more.'''
'''Key Concepts/Topics
Case Conversion:
-> UPPER(string): All-caps version
-> LOWER(string): All-lowercase version
-> Length: LENGTH(string): Number of characters
-> Substring Extraction: SUBSTR(string, start, length): Extract a part (e.g. characters 2–5)
-> Replace: REPLACE(string, old, new): Swap every occurrence of old with new
-> Trimming: TRIM(string): Removes leading/trailing whitespace
-> Pattern Matching: LIKE, %, _ (as before)
                   : Modifiers: In some SQLs: INSTR(string, substr) finds position
-> Combining Columns: || operator (CONCAT in some SQLs): Combine text columns with spaces, etc.
'''
import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
conn = setup_db(DB_FILE)
cursor = conn.cursor()

# 1.UPPER,LOWER
print("\n1. All customer LAST names in UPPER, first names in lower:")
cursor.execute(""" SELECT UPPER(last_name) AS upper_last, LOWER(first_name) lower_first FROM Customers; """)
for row in cursor.fetchall():
    print(row)

# 2. LENGTH, SUBSTR
print("\n2. Email addresses and their length, and first 3 letters:")
cursor.execute(""" SELECT email,LENGTH(email) as email_len,SUBSTR(email,1,3) as prefix FROM Customers; """)
for row in cursor.fetchall():
    print(row)

# 3. REPLACE, TRIM
print("\n3. Product names with spaces replaced by underscores and trimmed:")
cursor.execute( """ SELECT product_name,REPLACE(TRIM(product_name)," ","_") as clean_name FROM Products; """ )
for row in cursor.fetchall():
    print(row)

# 4. Combining fields and INSTR
print("\n4. Usernames extracted from email ('first part of email'):")
cursor.execute("""
    SELECT email,
           SUBSTR(email, 1, INSTR(email, '@') - 1) AS username
    FROM Customers;
""")
for row in cursor.fetchall():
    print(row)

# 5. LIKE usage for pattern search (emails ending with 'com')
print("\n5. Emails ending with '.com':")
cursor.execute("""
    SELECT email
    FROM Customers
    WHERE email LIKE '%.com';
""")
for row in cursor.fetchall():
    print(row)

conn.close()