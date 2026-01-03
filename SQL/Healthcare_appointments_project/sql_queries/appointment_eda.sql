-- Top 3 doctors by number of completed appointments this month
WITH AppCount AS (
    SELECT doctor_id,COUNT(*) as completed_appointments
    FROM Appointments
    WHERE status='completed' AND STRTFTIME ('%Y-%m',scheduled_datetime) = STRTFTIME('%Y-%m','now')
    GROUP BY doctor_id
)
SELECT d.name as doctor , d.specialty , d.location , a.completed_appointments
FROM Doctors d
JOIN AppCount a ON d.doctor_id = a.doctor_id
ORDER BY a.completed_appointments DESC LIMIT 3;

-- Calculate Patient No-Show Rate Using Window Function
SELECT p.name, COUNT(a.appointment_id) AS total_appts,
SUM(CASE WHEN a.status='no_show' THEN 1 ELSE 0 END) AS no_shows,
ROUND(100.0 * SUM(CASE WHEN a.status='no_show' THEN 1 ELSE 0 END)/COUNT(a.appointment_id),2) AS percent_no_show
FROM Patients p 
LEFT JOIN Appointments a ON p.patient_id = a.patient_id
GROUP BY p.patient_id
ORDER BY percent_no_show DESC 
LIMIT 10;