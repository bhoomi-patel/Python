# Date and Time Functions:
'''Date and time functions are built-in SQL commands that allow you to perform operations on date, time, and timestamp data types. These operations include extracting parts of a date (year, month, day), formatting dates, performing date arithmetic (adding/subtracting days/months/years), and comparing time intervals.'''
'''Common Date Functions:
-> DATE(string): Converts a string to a date (in SQLite, can also be used to manipulate dates).
-> STRFTIME(format, date): Formats date/timestamp values using placeholders (like '%Y-%m-%d' for year-month-day).
-> JULIANDAY(date): Returns the Julian day number (a continuous count of days), useful for date differences.
-> DATETIME(string): Converts or displays in 'YYYY-MM-DD HH:MM:SS' format.
-> CURRENT_DATE, CURRENT_TIME, CURRENT_TIMESTAMP: Built-ins for the current date/time.
-> Date Arithmetic: 'now', 'YYYY-MM-DD', plus/minus intervals: Example: DATE('now', '-7 days') for 7 days ago.
-> Extracting Parts: Use STRFTIME('%Y', date_col) for year, STRFTIME('%m', ...) for month, etc.
-> Comparisons: You can compare date strings directly in the 'YYYY-MM-DD' format—lexical order works!'''
'''
Common Format Codes:
%Y: Year with century (e.g., 2023)
%m: Month (01-12)
%d: Day of the month (01-31)
%H: Hour in 24-hour format (00-23)
%I: Hour in 12-hour format (01-12)
%M: Minute (00-59)
%S: Second (00-59)
%p: AM/PM
%A: Full weekday name (e.g., Sunday)
%B: Full month name (e.g., October)
%w: Day of week (0-6, Sunday is 0)
%W: Week of year (00-53, Monday as first day)
%j: Day of year (001-366)
%Y-%m-%d: Common date format
%H:%M:%S: Common time format
'''

import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from SQL.sql_basics.connecting_sqlite import setup_db
DB_FILE = 'example.db'
conn = None
try:
    conn=setup_db(DB_FILE)
    cursor = conn.cursor()
    # 1. Select, filter, and format dates
    print("\n1. Orders placed in January 2023:")
    cursor.execute(""" SELECT order_id,order_date,total_amount FROM Orders WHERE order_date BETWEEN '2023-01-01' AND '2023-01-31' ORDER BY order_date; """)
    for row in cursor.fetchall():
        print(row)

    # 2. STRFTIME: Extract year and month, group/order
    print("\n2. Orders grouped by month (count per month):")
    cursor.execute(""" SELECT STRFTIME('%Y-%m' , order_date) AS order_month,COUNT(*) AS order_count,SUM(total_amount) AS total_sales FROM Orders GROUP BY order_month ORDER BY order_month; """)
    for row in cursor.fetchall():
        print(row)

    # 3. JULIANDAY: Calculating date differences (days since order)
    print("\n3. Orders and days since that order:")
    cursor.execute(""" SELECT order_id,order_date,JULIANDAY('now') - JULIANDAY(order_date) AS days_since_order FROM Orders ORDER BY order_date DESC; """)
    for row in cursor.fetchall():
        print(row)

    # 4. CURRENT_DATE, DATE arithmetic: Orders from last 14 days
    print("\n4. Orders from the last 14 days (based on CURRENT_DATE):")
    cursor.execute(""" SELECT order_id,order_date,total_amount FROM Orders WHERE order_date >= DATE('now','-14 days') ORDER BY order_date DESC; """)
    for row in cursor.fetchall():
        print(row)
    print("\nCurrent date, time, and timestamp:")
    sql_query_current_datetime = """
        SELECT
            CURRENT_DATE AS current_date_only,
            CURRENT_TIME AS current_time_only,
            CURRENT_TIMESTAMP AS current_full_timestamp; """
    cursor.execute(sql_query_current_datetime)
    print(cursor.fetchone())
    
     # 5. Complex Grouping: Monthly avg order value, current year only
    print("\n5. Average order value per month for the current year:")
    cursor.execute(""" SELECT STRFTIME('%Y-%m',order_date) AS month,AVG(total_amount) AS avg_order_value FROM Orders WHERE STRFTIME('%Y' , order_date) = STRFTIME('%Y','now') GROUP BY month ORDER BY month; """)
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"Database error: {e}")
finally:
    if conn:
        conn.close()
        print("Database connection closed.")