'''Definition: SQLite is a lightweight file-based relational DB. Great for development and small apps.
Files:
schema.sql — SQL DDL (CREATE TABLE) statements
seed.py — Python script to populate DB with initial rows'''
import sqlite3
def seed_db():
    conn = sqlite3.connect("example.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username,email) VALUES (?,?)",("juli","juli@example.com"))
    conn.commit()
    conn.close()
    print("Database seeded!")
if __name__ ==  "__main__":
    seed_db()