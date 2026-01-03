-- One row per patient for ML
SELECT p.patient_id,
       p.name,
       p.age,
       p.gender,
       p.registered_date,
       COUNT(a.appointment_id) AS n_appts,
       SUM(CASE WHEN a.status='no_show' THEN 1 ELSE 0 END) AS n_no_shows,
       ROUND(100.0*SUM(CASE WHEN a.status='no_show' THEN 1 ELSE 0 END)/COUNT(a.appointment_id),2) AS no_show_pct,(JULIANDAY('now') - JULIANDAY(MAX(a.scheduled_datetime))) AS days_since_last_appt
FROM Patients p
LEFT JOIN Appointments a ON a.patient_id = p.patient_id
GROUP BY p.patient_id
ORDER BY n_appts DESC;
