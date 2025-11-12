'''datetime module -  Represents a single point in time with both date and time components.
Key Classes: datetime.datetime - Complete Date and Time '''
# Example
from datetime import date,time,datetime
d = date(2024,10,29)
print(f"Date object:{d}")

# Get current datetime
now=datetime.now()
print(f"Current datetime: {now}")
print(f"Year : {now.year} , Hour:{now.hour}")

#  2 - timedelta - Time Duration
''' A timedelta object represents a duration or a difference between two dates or times.
 It's how you add or subtract time.'''
from datetime import datetime,timedelta

now = datetime.now()
print(f"Now: {now}")

# what is the date in 7 days?
in_one_week = now + timedelta(days=7) 
print(f"In one week: {in_one_week}")
# How long until New Year's Day?
new_year = datetime(now.year +1 ,1,1) 
''' creates a datetime for Jan 1 of next year at 00:00:00 
    ( Year = next year , month , day ) '''
time_until_new_year = new_year - now
print(f"Time until New Year: {time_until_new_year} days")

# TASK - Create a function to check if a user's account is older than 30 days.
from datetime import datetime , timedelta
def acc_old(creation_date):
    # Check if the account is older than 30 days
    now = datetime.now()
    thirty_days_ago = now - timedelta(days=30)
    return creation_date < thirty_days_ago
user_creation_date = datetime(2024,9,15,10,30) # creates a datetime for Sep 15, 2024, at 10:30 AM
is_older=acc_old(user_creation_date)
print(f"Account is older than 30 days : {is_older}")

# 3 -Strftime and strptime 
''' strftime: Formats a datetime object into a human-readable string. (Object -> String)
    strptime: Parses a string containing a date/time into a datetime object. (String -> Object)
'''
from datetime import datetime 
now = datetime.now()
# strftime 
formatted_string = now.strftime("%A,%B %d,%Y %I:%M %p")  # # formats current datetime as 'Weekday, Month Day, Year Hour:Minute AM/PM'
print(f"Formatted : {formatted_string}")

# strptime
date_string = "2024-01-15 09:30:00"
parsed_datetime = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(f"Parsed: {parsed_datetime}")

# TASK - Create a function that calculates how many days have passed since a date string in the format "MM/DD/YYYY".
from datetime import datetime,date
def days_since(date_str):
    '''calculate how many days passed since given date string'''
    parsed_date = datetime.strptime(date_str,"%m/%d/%Y").date()
    # calculate difference
    today = date.today()
    days_passed = (today-parsed_date).days

    return days_passed

start_date="01/01/2025"
days = days_since(start_date)
print(f"{days} days have passed since {start_date}")