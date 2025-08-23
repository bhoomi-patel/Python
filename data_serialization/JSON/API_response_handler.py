import requests
import json

def get_weather(city):
    # get weather data from API
    api_key = "d0ea34667681252646c8384998046309"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
         "q": city,
         "appid": api_key,
         "units": "metric"
    }
    response = requests.get(url, params=params)
    weather_data = response.json()  # parse JSON response

    return {
        "city": weather_data["name"],
        "temperature": weather_data["main"]["temp"],
        "description": weather_data["weather"][0]["description"]
    }

# configure 

class ConfigManager:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.settings = self.load_config()

    def load_config(self):
        try:
            with open(self.config_file, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {"debug": True, "api_key": "", "timeout": 30}

    def save_config(self):
         # Removed quotes around self.config_file to use the variable
         with open(self.config_file, "w") as file:
             json.dump(self.settings, file, indent=2)

    def get(self, key, default=None):
        return self.settings.get(key, default)

# Main execution block to run the code
if __name__ == "__main__":
    # For demonstration, we'll prompt the user for a city name.
    city = input("Enter a city name to get the weather: ")
    try:
        weather = get_weather(city)
        print(f"\nWeather in {weather['city']}: {weather['temperature']}°C, {weather['description'].capitalize()}")
    except Exception as e:
        print("An error occurred:", e)
