Sometimes you want the task to run even when Python isn’t continuously running. That’s where cron jobs or Windows Task Scheduler come in.

## Cron
Cron is a background helper on your computer that automatically runs tasks for you on a schedule.

### Real-World Tasks

- Email morning reports.
- Update dashboards nightly.
- Clear cache every Sunday.

### Cron Syntax

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of the month (1 - 31)
│ │ │ ┌───────────── month (1 - 12)
│ │ │ │ ┌───────────── day of the week (0 - 6) (Sunday to Saturday)
│ │ │ │ │
* * * * * command to execute.
```

#### Common Patterns

- `* * * * *` - Every minute
- `0 * * * *` - Every hour (at minute 0)
- `0 0 * * *` - Every day at midnight
- `0 0 * * 0` - Every Sunday at midnight
- `0 9-17 * * 1-5` - Every hour from 9 AM to 5 PM, Monday to Friday
- `*/15 * * * *` - Every 15 minutes

### Coding Task: Create a cron expression for each of the following tasks:

1. Run a backup every day at 2 AM: `0 2 * * * /path/to/backup_script.sh`
2. Weekly report every Monday at 9 AM: `0 9 * * 1 /path/to/weekly_report.py`
3. Server health check every 5 minutes during business hours on weekdays: `*/5 9-17 * * 1-5 /path/to/health_check.py`
4. Monthly cleanup on the 1st at midnight: `0 0 1 * * /path/to/cleanup_script.py`

### Managing User Crontab

- Edit your cron jobs: `crontab -e`
- List your current cron jobs: `crontab -l`
- Remove all your cron jobs: `crontab -r`

#### Example Crontab Entry

```bash
# Backup the database every night at 1 AM
0 1 * * * /usr/bin/python3 /home/user/scripts/db_backup.py >> /home/user/logs/backup.log 2>&1
```

## Windows Task Scheduler

### Definition

Task Scheduler allows Windows users to schedule programs or scripts to run automatically at predefined times or events.

### Key Components

- **Trigger**: When the task should run (time, event, etc.)
- **Action**: What the task should do (run a program, send an email, etc.)
- **Conditions**: Additional requirements for the task to run
- **Settings**: General behavior settings for the task

#### Creating a Basic Task

1. Open Task Scheduler (Start → Windows Administrative Tools → Task Scheduler)
2. Click "Create Basic Task..."
3. Name the task and provide a description
4. Choose a trigger (Daily, Weekly, etc.)
5. Set the schedule details
6. Select "Start a program"
7. Browse to your Python executable and provide the script path as an argument
8. Review and finish

### Coding Task: Write the steps to create a Windows Scheduled Task that runs a Python script every weekday at 9 AM.

#### Solution

1. Create a Python script (e.g., `C:\scripts\daily_task.py`)
2. Open Task Scheduler from the Start menu
3. Click "Create Basic Task..."
4. Name: "Daily Python Task"  
   Description: "Runs my Python script every weekday morning"
5. Trigger: Weekly
6. Start: [Today's date], 9:00 AM  
   Recur every 1 week on: Monday, Tuesday, Wednesday, Thursday, Friday
7. Action: Start a program
8. Program/script: `C:\Path\to\Python\python.exe`  
   Arguments: `C:\scripts\daily_task.py`  
   Start in: `C:\scripts`
9. Check "Open the Properties dialog for this task when I click Finish"
10. Click Finish
11. In the Properties dialog:  
    - Check "Run with highest privileges" if needed  
    - Under the "Settings" tab, configure additional options as needed
12. Click OK to save the task

## Celery - The Distributed Task Queue

### Definition

Celery is a distributed task queue that can process vast numbers of messages, ideal for web applications needing to perform background tasks.

### Key Features
- **Distributed**: Can run tasks across multiple workers and machines
- **Asynchronous**: Non-blocking task execution
- **Persistent**: Can survive service restarts
- **Scheduled & Periodic**: Can both delay tasks and schedule recurring tasks

### Sample Example with Celery

```python
# First, we need a message broker (like Redis)
# pip install celery redis

# app.py
from celery import Celery
from datetime import timedelta
# Create Celery app
app = Celery('tasks', broker='redis://localhost:6379/0')
# Configure Celery
app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    beat_schedule={
        'database-backup-every-day': {
            'task': 'app.backup_database',
            'schedule': timedelta(days=1),
            'args': (),
        },
    },
)
@app.task
def backup_database():
    """Task to back up the database."""
    print("Backing up the database...")
    # Database backup logic here
    return {'status': 'success', 'timestamp': time.time()}

# To run:
# Terminal 1: celery -A app worker --loglevel=info
# Terminal 2: celery -A app beat --loglevel=info
```
### Real-Life Use
Web applications needing background processing, like sending emails, generating reports, processing uploads, or any CPU-intensive task that shouldn't block the web server.