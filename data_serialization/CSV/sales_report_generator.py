import csv 
import sqlite3
from datetime import datetime

def setup_database(db_path):
    # connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # create sales table 
    cursor.execute(''' create table if not exists sales(
                   id integer primary key autoincrement,
                   product_name text,
                   quantity integer,
                   unit_price real,
                   customer_name text,
                   sale_time text
                   ) ''')
    # insert sample data
    cursor.execute ("delete from sales")  # clear existing data
    sample_sales = [
        ('Laptop', 1, 1200.00, 'Alice', '2024-01-15 10:30:00'),
        ('Smartphone', 2, 800.00, 'Bob', '2024-01-16 11:00:00'),
        ('Tablet', 3, 300.00, 'Charlie', '2024-01-17 12:15:00'),
        ('Headphones', 5, 150.00, 'David', '2024-01-18 14:45:00'),
        ('Smartwatch', 2, 200.00, 'Eve', '2024-01-19 16:20:00')
    ]
    cursor.executemany ('''
          insert into sales (product_name, quantity, unit_price, customer_name, sale_time)
                        values (?, ?, ?, ?, ?)''' , sample_sales)
    
    #  commit changes and close connection
    conn.commit()
    conn.close()
    print ("Database setup complete with sample data.")

def generate_sales_report(db_path,date,output_file):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    query= ''' select product_name, quantity, unit_price, customer_name, sale_time
               from sales where date(sale_time) = ? order by sale_time '''
    cursor.execute(query,(date,))
    sales_data = cursor.fetchall()

    # close connection
    conn.close()
    with open(output_file,'w',newline='',encoding='utf-8') as file:
        fieldnames = ['Product Name', 'Quantity', 'Unit Price', 'Customer Name', 'Sale Time']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for row in sales_data:
            writer.writerow({
                'Product Name': row[0],
                'Quantity': row[1],
                'Unit Price': row[2],
                'Customer Name': row[3],
                'Sale Time': row[4]
            })
        print(f"Sales report for {date} generated: {output_file} with {len(sales_data)} records.")

if __name__ == "__main__":
    db_path = 'sales.db'
    setup_database(db_path)

    # generate report for a specific date
    report_date = input("Enter report date (YYYY-MM-DD): ")
    output_file = f'sales_report_{report_date}.csv'
    generate_sales_report(db_path, report_date, output_file)