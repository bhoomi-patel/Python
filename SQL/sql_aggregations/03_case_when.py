# Conditional Logic: CASE WHEN Statements
''' The CASE statement (often referred to as CASE WHEN THEN ELSE END) allows you to implement IF-THEN-ELSE logic directly within your SQL queries. It evaluates conditions sequentially and returns a result corresponding to the first condition that is true'''
'''Key Concepts/Topics:
-> CASE: The CASE statement lets you perform if-then-else logic inside SQL
-> WHEN condition THEN result: Defines a condition and the value to return if that condition is true. You can have multiple WHEN clauses.
-> ELSE result: (Optional) Specifies a default value to return if none of the WHEN conditions are met. If omitted and no WHEN condition is true, NULL is returned.
-> END: Terminates the CASE statement.
-> New Column Creation: CASE statements are often used in the SELECT clause to create new, derived columns based on existing data.
-> Conditional Aggregation: CASE can be combined with aggregation functions (e.g., SUM(CASE WHEN ... END)) to count or sum items based on specific criteria within groups.
-> UPDATE with CASE: CASE can be used within an UPDATE statement to apply different changes to different rows based on conditions.
-> Searched CASE vs. Simple CASE:
-> Searched CASE: CASE WHEN condition1 THEN result1 WHEN condition2 THEN result2 ... ELSE default_result END. Conditions can be independent. (This is what we primarily use).
-> Simple CASE: CASE column_name WHEN value1 THEN result1 WHEN value2 THEN result2 ... ELSE default_result END. Compares column_name to specific values. (Less common for complex logic).'''
'''General form:
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ...
    ELSE default_result
END'''
'''Real-life Use
Bucketing: Assigning customers to “age groups” (e.g., 'Youth', 'Adult', 'Senior').
Scoring: Adding “status” labels based on scores/values (“Fail”, “Pass”, “Exceeds”).
Data Cleaning: Converting NULL or negative values to meaningful descriptions.
Transformations: Turning numeric codes into human-friendly text.'''

import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db

DB_FILE = 'example.db'

print("Conditional Logic with CASE WHEN")
conn = None

try:
    conn = setup_db(DB_FILE)
    cursor = conn.cursor()
    # 1. categorize customers by age group
    print("\n1. Customers, bucketed by age group:")
    cursor.execute(''' SELECT first_name,age,CASE WHEN age <25 THEN 'Young' WHEN age BETWEEN 25 AND 35 THEN 'Adult' ELSE 'Senior' END AS age_group FROM Customers ORDER BY age; ''')
    for row in cursor.fetchall():
        print(row)
    # 2. Flag low/high stock for products
    print("\n2. Products with Stock Level Label:")
    cursor.execute("""
        SELECT product_name, stock_quantity,
            CASE
                WHEN stock_quantity < 20 THEN 'Low Stock'
                WHEN stock_quantity BETWEEN 20 AND 99 THEN 'Normal Stock'
                ELSE 'High Stock'
            END AS stock_status
        FROM Products
        ORDER BY stock_quantity;
    """)
    for row in cursor.fetchall():
        print(row)

    # 3. Label Orders by Amount Tier
    print("\n3. Orders with Amount Tier:")
    cursor.execute("""
        SELECT order_id, total_amount,
            CASE
                WHEN total_amount < 100 THEN 'Small'
                WHEN total_amount BETWEEN 100 AND 500 THEN 'Medium'
                ELSE 'Large'
            END AS amount_tier
        FROM Orders
        ORDER BY total_amount;
    """)
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("\nDatabase connection closed.")