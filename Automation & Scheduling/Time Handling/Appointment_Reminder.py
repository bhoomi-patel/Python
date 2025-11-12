'''Goal: Create a script that takes an appointment date and time string in a local timezone, 
checks if it's in the future, and if so, calculates how long until the appointment.'''
from datetime import datetime
from zoneinfo import ZoneInfo

def schedule_appointment(appointment_str: str, local_timezone_str: str):
    """
    Schedules an appointment and calculates the time remaining.

    Args:
        appointment_str: The appointment date/time, e.g., "2024-12-25 09:00"
        local_timezone_str: The IANA timezone name, e.g., "America/New_York"
    """
    try:
        # 1. Parse the string into a naive datetime object (strptime)
        naive_dt = datetime.strptime(appointment_str, "%Y-%m-%d %H:%M")
        
        # 2. Make the datetime object "aware" by attaching the local timezone
        local_tz = ZoneInfo(local_timezone_str)
        local_dt = naive_dt.replace(tzinfo=local_tz)
        print(f"Appointment scheduled for: {local_dt.strftime('%c %Z')}")

        # 3. Convert to UTC for a universal reference (astimezone)
        utc_dt = local_dt.astimezone(ZoneInfo("UTC"))
        
        # 4. Get the current time in UTC to compare
        utc_now = datetime.now(ZoneInfo("UTC"))
        
        # 5. Check if the appointment is in the past or future (timedelta)
        if utc_now > utc_dt:
            print("Error: This appointment is in the past!")
            return

        time_until = utc_dt - utc_now
        print(f"Appointment is in {time_until.days} days and {time_until.seconds // 3600} hours.")

    except (ValueError, KeyError) as e:
        print(f"Error: Could not process the appointment. Details: {e}")

# --- Test Cases ---
print("--- Scheduling Appointment 1 ---")
schedule_appointment("2025-11-15 15:30", "Europe/Paris")

print("\n--- Scheduling Appointment 2 (in the past) ---")
schedule_appointment("2023-01-01 10:00", "Asia/Tokyo")