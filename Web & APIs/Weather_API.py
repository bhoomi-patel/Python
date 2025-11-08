import requests

def get_weather(city,api_key):
    # get weather data for a  city
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params={'q':city,'appid':api_key,'units':'metric'} # units in Celsius

    try:
        res=requests.get(base_url,params=params,timeout=5)
        res.raise_for_status()  # Raise an error for bad responses

        data = res.json()
        weather_info = {
            'city':data['name'],
            'temp':data['main']['temp'],
            'description':data['weather'][0]['description'],        
            'humidity':data['main']['humidity'],
             'wind_speed':data['wind']['speed']
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    return weather_info

# Example usage
weather = get_weather("London","d0ea34667681252646c8384998046309")
if weather:
    print(f"Weather in {weather['city']}: Temperature: {weather['temp']}°C , Description: {weather['description']} , Humidity: {weather['humidity']}% , Wind Speed: {weather['wind_speed']} m/s")