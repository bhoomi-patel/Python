'''Scheduling means setting your program to run automatically at a specified time or interval.
Examples: Run a report generator every day at 6 AM.
          Delete old log files every Sunday.
          Send reminders to users every 30 minutes.
          Trigger an API call once a minute. '''
# schedule library
'''The schedule library allows you to define jobs that run at specific intervals or times, using a clean, human-readable syntax.
install ---> pip install schedule '''
import schedule
import time
def job():
    print("Running scheduled task.....")
schedule.every(5).seconds.do(job)

while True:
    schedule.run_pending() #  Checks if any task is due.
    time.sleep(1)

'''Task: Create a script that reminds you to take a break
          every 30 minutes during work hours (9 AM to 5 PM).'''
import schedule
import time
from datetime import datetime
def take_break():
    current_time = datetime.now().strftime("%H:%M")
    print(f"[{current_time}] Time for a break! Stand up and stretch.")
schedule.every(30).minutes.do(take_break)
print("Break reminder started.....Press Ctrl+C to exit.")
while True:
    # check if current time is between 9 AM - 5 PM
    current_hour=datetime.now().hour
    if 9 <= current_hour < 17 :
        schedule.run_pending()
    time.sleep(1)

'''Real use : Trigger an API call every 10 minutes to update a feed:'''
import schedule,time,requests
def fetch_data():
    r = requests.get("https://dummyjson.com/products")
    print(f"Fetched data at {time.strftime('%X')} with status {r.status_code}")
schedule.every(1).minutes.do(fetch_data)

while True:
    schedule.run_pending()
    time.sleep(1)

# ----- Advanced Scheduling -----
#  1 - Scheduling at a Specific Time Each Day
import schedule,time
def backup_database():
    print("Performing daily database backup...")
schedule.every().day.at("02:00").do(backup_database)
#  2 - Scheduling on Specific Days 
def send_weekly_report():
    print("Sending weekly report to stakeholders...")
schedule.every().monday.do(send_weekly_report)
#  3 - Run at a specific time on a specific day
schedule.every().friday.at("17:00").do(send_weekly_report)
 # 4 - Passing arguments to a job
def greet(name):
    print(f"Hello {name}! It's {time.strftime('%X')}")
schedule.every(10).seconds.do(greet,name="Juli")
 # 5 - Check what’s scheduled
print(schedule.jobs)
# 6 - Multiple Tasks Together
def chk_emails():
    print("Checking inbox........")
def clean_cache():
    print("Cleaning cache.....")
schedule.every(2).minutes.do(chk_emails)
schedule.every().hour.do(clean_cache)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
''' Memory Trick --> “Rule of 3s”: do() defines → run_pending() executes → sleep() sustains.'''

# -----Managing Jobs ------
def job():
    print("I'm working.....")
# create a job and store it
job1 = schedule.every(10).seconds.do(job)
# Run for 30 seconds
end_time = time.time() + 30
while time.time() < end_time:
      schedule.run_pending()
      time.sleep(1)
# cancel the job
schedule.cancel_job(job1)
print("Job cancelled")

#  clear all jobs
schedule.clear()
print("All jobs cleared")

while True:
    schedule.run_pending()
    time.sleep(1)

'''Mini Task :Create a temporary monitoring script that checks a website's availability every minute, but automatically stops after one hour. '''
import schedule , time , requests
from datetime import datetime, timedelta
def chk_website(url):
    try:
        response = requests.get(url,timedelta=5)
        status = "UP" if response.status_code == 200 else f"DOWN (Status code : {response.status_code})"
    except requests.RequestException as e:
        status = f"ERROR ({str(e)})"
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Website {url} is {status}")
    # Set up the monitoring
    url_to_monitor="https://www.example.com"
    monitor_job = schedule.every(1).minutes.do(chk_website,url=url_to_monitor)
    #  Calculate when to stop ( 1 hour from now)
    stop_time = datetime.now()+timedelta(hours=1)
    print(f"Starting website monitoring for {url_to_monitor} every minute for 1 hour...")
    print(f"Monitoring will stop at {stop_time.strftime('%Y-%m-%d %H:%M:%S')}")

    while datetime.now() < stop_time:
        schedule.run_pending()
        time.sleep(1)
    # Clean up
    schedule.cancel_job(monitor_job)
    print("Monitoring complete!")

# Limitations and Considerations of schedule
'''Definition: While convenient, the schedule library has specific constraints that are important to understand for reliable production use.
Key Limitations: Process Must Be Running: If the Python process stops, scheduled jobs won't run.
                 Single-Threaded by Default: Tasks block each other by default.
                 No Persistence: Scheduled jobs aren't saved between program runs.'''
# sample example
import schedule,time,threading
def run_threaded(job_fun,*args,**kwargs):
    job_thread = threading.Thread(target=job_fun,args=args,kwargs=kwargs)
    job_thread.start()
def long_task():
    print("Starting a long task......")
    time.sleep(10) # Simulating a task that takes 10 seconds
    print("Long task completed.")
def quick_task():
    print("Quick task executed.")
# schedule tasks
schedule.every(5).seconds.do(run_threaded,long_task)
schedule.every(2).seconds.do(run_threaded,quick_task)
while True:
    schedule.run_pending()
    time.sleep(1)
# TASK :Modify the website monitoring script to check multiple websites concurrently using threading.
import schedule,time,requests,threading
from datetime import datetime, timedelta

def run_threaded(job_func, *args, **kwargs):
    job_thread = threading.Thread(target=job_func, args=args, kwargs=kwargs)
    job_thread.start()
    return job_thread  # Return the thread for potential future use

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        status = "UP" if response.status_code == 200 else f"DOWN (Status code: {response.status_code})"
    except requests.RequestException as e:
        status = f"ERROR ({str(e)})"
        
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {url} is {status}")

# Set up the monitoring for multiple sites
websites = [
    "https://example.com",
    "https://python.org",
    "https://github.com"
]

# Schedule each website check
for url in websites:
    schedule.every(1).minutes.do(run_threaded, check_website, url)

# Run for one hour
stop_time = datetime.now() + timedelta(hours=1)
print(f"Starting website monitoring for {len(websites)} websites")
print(f"Monitoring will stop at {stop_time.strftime('%H:%M:%S')}")

while datetime.now() < stop_time:
    schedule.run_pending()
    time.sleep(1)

# Clear all scheduled jobs
schedule.clear()
print("Monitoring complete!")
