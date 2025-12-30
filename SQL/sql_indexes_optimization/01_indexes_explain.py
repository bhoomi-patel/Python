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
