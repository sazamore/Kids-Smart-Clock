import requests
from PIL import Image
from io import BytesIO

def get_weather_data(lat=40.063328, lon=-105.409606):
    # Get location data using ZIP code
    location_url = f"https://api.weather.gov/points/{lat},{lon}"
    response = requests.get(location_url)
    
    if response.status_code != 200:
        print("Error fetching location data")
        return None, None
    
    location_data = response.json()
    forecast_url = location_data['properties']['forecast']
    
    # Get weather data from the forecast URL
    weather_response = requests.get(forecast_url)
    
    if weather_response.status_code != 200:
        print("Error fetching weather data")
        return None, None
    
    weather_data = weather_response.json()
    today_forecast = weather_data['properties']['periods'][0]
    # tonight_forecast = weather_data['properties']['periods'][1]
    
    return today_forecast['temperature'], today_forecast['shortForecast'], today_forecast['icon']

def display_weather_image(icon_url):
    response = requests.get(icon_url)
    if response.status_code == 200:
        img = Image.open(BytesIO(response.content))
        img.show()
    else:
        print("Error fetching weather icon")

def main():
    # zip_code = input("Enter your ZIP code: ")
    
    temperature, weather_condition, icon_url = get_weather_data() #default lat and lon is in Boulder, CO
    
    if temperature and weather_condition:
        print(f"Temperature: {temperature}°F")
        print(f"Weather Condition: {weather_condition}")
        
        display_weather_image(icon_url)
    else:
        print("Could not retrieve weather information. Check Internet connection")

if __name__ == "__main__":
    main()

