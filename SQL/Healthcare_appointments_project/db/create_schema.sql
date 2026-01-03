-- PATIENTS: Who books appointments
CREATE TABLE Patients(
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    gender TEXT CHECK(gender IN('F','M','O')),
    phone TEXT,
    email TEXT,
    registered_date DATE DEFAULT CURRENT_DATE
);

-- DOCTORS: Who offers appointments
CREATE TABLE Doctors(
    doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty TEXT,
    location TEXT
);

-- APPOINTMENTS: The "fact" table
CREATE TABLE Appointments(
    appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    patient_id INTEGER NOT NULL,
    doctor_id INTEGER NOT NULL,
    scheduled_datetime DATETIME NOT NULL,
    status TEXT CHECK(status IN('completed','no_show','cancelled','scheduled')) NOT NULL DEFAULT 'scheduled',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(patient_id) REFERENCES Patients(patient_id),
    FOREIGN KEY(doctor_id) REFERENCES Doctors(doctor_id)
);

-- Optional: Feedback/Rating
CREATE TABLE Feedback (
    feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
    appointment_id INTEGER,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    comments TEXT,
    FOREIGN KEY(appointment_id) REFERENCES Appointments(appointment_id)
);