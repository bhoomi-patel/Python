# Goal : Fetch weather data every hour and log it.
import schedule,time,logging,requests
from datetime import datetime
logging.basicConfig(filename="weather.log",level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
API_URL="https://api.open-meteo.com/v1/forecast"
PARAMS = {"latitude": 40.71, "longitude": -74.01, "hourly": "temperature_2m"}

def fetch_weather():
    try:
        response=requests.get(API_URL,params=PARAMS)
        response.raise_for_status()
        data = response.json()
        temp = data["hourly"]["temperature_2m"][0]
        logging.info(f"Fetched temperature = {temp}°C")
        print(f"[{datetime.now().strftime('%X')}] Logged temperature = {temp}°C")
    except Exception as e:
        logging.error(f"Failed to fetch weather : {e}")
# schedule
schedule.every().hour.do(fetch_weather)
print("Weather Reporter started...")
fetch_weather() 
while True:
    schedule.run_pending()
    time.sleep(60)
