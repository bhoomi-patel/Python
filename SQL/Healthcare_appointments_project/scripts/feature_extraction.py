import pandas as pd
from sqlalchemy import create_engine

DB_FILE = "appointments_project.db"
engine = create_engine(f"sqlite:///{DB_FILE}")

# Example: Pull a "patient features" table
df_patient_features = pd.read_sql ("""
SELECT p.patient_id , p.name , p.age , p.gender , p.registered_date,
COUNT (a.appointment_id) AS n_appointments,
SUM(CASE WHEN a.status='no_show' THEN 1 ELSE 0 END) AS n_no_shows,
(JULIANDAY('now') - JULIANDAY(MAX(a.scheduled_datetime))) AS days_since_last_appt FROM Patients p
LEFT JOIN Appointments a ON a.patient_id = p.patient_id GROUP BY p.patient_id;  """,engine)
print(df_patient_features.head())

# Save features for ML
df_patient_features.to_csv("patients_ml_features.csv",index=False)

