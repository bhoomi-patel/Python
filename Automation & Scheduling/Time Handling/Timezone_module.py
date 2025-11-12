''' It will helps users in different parts of the world.'''
''' The Golden Rule: Always store timestamps in your database as UTC. 
This creates a universal standard. When you display the time to a user in New York, you convert it from UTC to their local timezone.'''

# 1 - Naive vs Aware 
'''Naive: A datetime object that has no timezone information. datetime.now() creates a naive object. It's just a time on the clock, but you don't know where that clock is.
   Aware: A datetime object that does have timezone information attached. It represents an unambiguous, specific moment in time.
'''
from datetime import datetime 
from zoneinfo import ZoneInfo # standard library

naive_now=datetime.now()
print(f"Naive: {naive_now} , Timezone:{naive_now.tzinfo}")

aware_utc_now=datetime.now(ZoneInfo("UTC"))
print(f"Aware (UTC) : {aware_utc_now} , Timezone:{aware_utc_now.tzinfo}")

# 2 - astimezone : The astimezone() method converts an aware datetime object from its current timezone to a new one.
from datetime import datetime
from zoneinfo import ZoneInfo 
utc_now = datetime.now(ZoneInfo("UTC"))
print(f"Time in UTC : {utc_now}")

tokyo_time = utc_now.astimezone(ZoneInfo("Asia/Tokyo"))
new_york_time = utc_now.astimezone(ZoneInfo("America/New_York"))
print(f"Time in Tokyo: {tokyo_time}")
print(f"Time in New York: {new_york_time}")

# TASK - A flight departs from London at 2024-08-10 14:00. What is the local time in San Francisco when the flight departs?
from datetime import datetime
from zoneinfo import ZoneInfo

# 1. Create an AWARE datetime for the departure
departure_london_time = datetime(2024, 8, 10, 14, 0, tzinfo=ZoneInfo("Europe/London"))

# 2. Convert it to the target timezone
arrival_sf_time = departure_london_time.astimezone(ZoneInfo("America/Los_Angeles"))

print(f"Departure time in London: {departure_london_time.strftime('%Y-%m-%d %I:%M %p %Z')}")
print(f"Equivalent time in SF: {arrival_sf_time.strftime('%Y-%m-%d %I:%M %p %Z')}")

# 3 - pytz : pytz is a library that provides accurate timezone calculations and is recommended for use with the datetime module.
# Install --> pip install pytz
import pytz
from datetime import datetime

utc_now = datetime.now(pytz.UTC)
print(f"Current UTC time: {utc_now}")
tz = pytz.timezone('America/New_York')
ny_time=datetime.now(tz)
print(f"Current time in New York: {ny_time}")
# List all available timezones
all_timezones = pytz.all_timezones
print(f"Number of available timezones: {len(all_timezones)}")
print(f"Some examples: {all_timezones[:5]}")

# TASK - Create a function that converts a UTC datetime to the local time of a given timezone.
from datetime import datetime
import pytz

def utc_to_local(utc_dt,timezone_str):
    local_tz = pytz.timezone(timezone_str)
    if utc_dt.tzinfo is None:
        utc_dt = pytz.UTC.locallize(utc_dt)
    local_dt = utc_dt.astimezone(local_tz)
    return local_dt

utc_time = datetime.now(pytz.UTC)
print(f"UTC time: {utc_time}")

local_time = utc_to_local(utc_time,'Asia/Tokyo')
print(f"Tokyo time:{local_time}")

local_time =utc_to_local(utc_time,'Europe/London')
print(f"London time: {local_time}")