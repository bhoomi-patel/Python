'''These 4 topics are used in every real‑world web/API or automation project — they let you build code that’s maintainable, secure, and reliable.'''
# A) Config Files — “Where settings live
'''Instead of hard‑coding paths or settings inside your code, you keep them in a separate configuration file — usually .json (or .yaml, .ini, etc.).
This makes your program easy to maintain and change without editing the code every time.'''
'''Example config.json ""
{
  "data_path": "data",
  "interval_minutes": 60,
  "apis": {
    "coingecko": true,
    "newsapi": true
  },
  "log_file": "app.log"
}'''
import json
# laod config
with open("Automation & Scheduling/Production Patterns/config.json") as f:
    cfg = json.load(f)
# Access config fields
print("Data path:", cfg["data_path"])
print("Refresh interval:", cfg["interval_minutes"], "minutes")
print("CoinGecko API used:", cfg["apis"]["coingecko"])

# B) Environment Variables — “Where secrets live”
'''Configuration files are for non‑secret values.
Secrets (passwords, API keys) must never be saved directly in the file or code!
You store them as environment variables (env vars) so they don’t get pushed to GitHub accidentally.
- Example: Set in your system shell
 -> Windows PowerShell:
bash : setx NEWS_API_KEY "abcd1234"             
-> Linux/macOS:
bash :  export NEWS_API_KEY="abcd1234"
- Access in Python
    import os

    key = os.getenv("NEWS_API_KEY")
    if key:
       print("Key loaded successfully!")
    else:
        print("No API key found, please set NEWS_API_KEY.")

->  Using a .env File (for local dev)
Instead of entering it manually each time, create a .env file in your project root:
NEWS_API_KEY=abcd1234
DATABASE_URL=mysql://user:pass@localhost/db

-> Then load it automatically with python-dotenv:
    # pip install python-dotenv
    from dotenv import load_dotenv
    import os

    load_dotenv()  # Loads from .env
    api_key = os.getenv("NEWS_API_KEY")
    print("Loaded key:", api_key)
'''
# C) Retries & Backoff — “Try again, smarter each time
'''APIs sometimes fail due to:

Internet hiccups
Temporary server overloads
Instead of crashing immediately, we retry the operation after a small wait — and each time we wait a bit more.

This is called exponential backoff.'''
#  Simple Example ― retrying API calls
import time
import requests

def fetch_with_retries(url, tries=3):
    backoff = 1  # start waiting 1 sec, then 2, 4, ...
    
    for i in range(tries):
        try:
            print(f"Attempt {i+1} fetching {url}")
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            print("Success!")
            return response.json()
        
        except Exception as e:
            print(f"Error: {e}")
            if i == tries - 1:
                print("Giving up after max retries.")
                raise
            print(f"Waiting {backoff} seconds before retry...")
            time.sleep(backoff)
            backoff *= 2  # double the delay

# Example Run
fetch_with_retries("https://jsonplaceholder.typicode.com/todos/1")

# D) Idempotency — “Do it once, do it safely”
'''An idempotent operation means you can safely run it multiple times and get the same final result.
(Think of: pressing a light switch twice → still ends up on or off, not duplicated!)

This prevents duplicate actions — like:

Sending the same email twice
Re‑writing the same file multiple times
Making duplicate API records'''
# Example: 
'''If you run this multiple times in the same day, it only creates one file, not many duplicates.'''
import os
from datetime import datetime

def save_data_once(data, folder="data"):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d")
    file_path = f"{folder}/report_{timestamp}.txt"

    if os.path.exists(file_path):
        print("Report already exists, skip writing.")
        return

    with open(file_path, "w") as f:
        f.write(data)
    print("File written successfully:", file_path)

# Run multiple times safely
save_data_once("Daily Report Content")
