# simple synthetic loader using Python and sqlite3
# Importing the Faker class from the Faker library, a popular Python package for generating realistic fake data (names, addresses, phone numbers, emails, dates, text, etc.)—great for testing, demos, or seeding databases.
import sqlite3
import random 
from faker import Faker
import datetime
DB_FILE = "appointments_project.db"
fake = Faker()

def create_schema(conn):
    with open("db/create_schema.sql","r") as f:
        sql = f.read()
        conn.executescript(sql)
        print("Schema created.")
def generate_data(conn):
    cursor = conn.cursor()
    # insert doctors
    specialties = ['Dermatology', 'Pediatrics', 'General', 'Cardiology', 'Ortho']
    locations = ['North Clinic', 'South Clinic', 'East Clinic']
    for i in range(8):
        cursor.execute(
            "INSERT INTO Doctors (name, specialty, location) VALUES (?, ?, ?);",
            (fake.name(),random.choice(specialties),random.choice(locations))
        )
     # --- Insert Patients ---
    genders = ['F', 'M', 'O']
    for i in range(25):
        cursor.execute(
            "INSERT INTO Patients (name, age, gender, phone, email, registered_date) VALUES (?, ?, ?, ?, ?, ?);",
            (fake.name(),random.randint(15,90),random.choice(genders),
             fake.phone_number(),fake.email(),(datetime.date.today()-datetime.timedelta(days=random.randint(0,400))).strftime("%Y-%M-%d"))
        )
    # --- Insert Appointments ---
    now = datetime.datetime.now()
    for i in range(80):
        patient_id = random.randint(1,25)
        doctor_id = random.randint(1,8)
        sched_time = now - datetime.timedelta(days=random.randint(0,60),hours=random.randint(0,23),minutes=random.randint(0,59))
        status = random.choices(['completed','no_show','scheduled','cancelled'], [0.6,0.1,0.25,0.05])[0]
        cursor.execute(
            "INSERT INTO Appointments (patient_id, doctor_id, scheduled_datetime, status) VALUES (?, ?, ?, ?);",
            (patient_id, doctor_id, sched_time.strftime('%Y-%m-%d %H:%M:%S'), status)
        )
        