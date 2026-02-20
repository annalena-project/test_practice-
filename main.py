# a.

import requests 
import json

URL = "https://geocoding-api.open-meteo.com/v1/search"

parameters = {
    "name": "Chicago",         # city 
    "country": "USA",
    "count": 1
}

response = requests.get(URL, params=parameters, timeout=10)  
# response a variable that contains: requests.get: sending a requset to server, URL.
# params=parameters: The server uses them to know what to return.

print(response.status_code)   # Prints the HTTP status code. It shows what response the server sent back (200, 400, 500)
print(response.json())        # Converts the server response to a Python dictionary and prints the data

data = response.json()        # Converts the server response from JSON format to a Python dictionary

results = data["results"]     
# Works with the information that data received from the URL.
# Goes into the dictionary "data" → finds the key "results" → 
# gets the value stored there → saves it in the variable "results".
first_result = results[0]
# Takes the first item from the results list and stores it in the variable first_result

latitude = first_result["latitude"]   # Gets the value of "latitude" / "longitude" from the first_result dictionary
longitude = first_result["longitude"]

print("latitude:", latitude)   # Prints the latitude / longitude value
print("longitude:", longitude)
  
# b. 

FORECAST_URL = "https://api.open-meteo.com/v1/forecast?current_weather=true"

forecast_parameters = {
    "latitude": latitude,
    "longitude": longitude,
}

forecast_response = requests.get(FORECAST_URL, params=forecast_parameters, timeout=10)

forecast_data = forecast_response.json()
print(forecast_response.status_code)

print(json.dumps(forecast_data, indent=2))

# C

class WeatherReport:
    def __init__(self, city, country, latitude, longitude, temperature, elevation, windspeed, observation_time):
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.temperature = temperature
        self.elevation = elevation
        self.windspeed = windspeed
        self.observation_time = observation_time

report = WeatherReport(
    city=parameters["name"],
    country=parameters["country"],
    latitude=forecast_parameters["latitude"],
    longitude=forecast_parameters["longitude"],
    temperature=forecast_data["current_weather"]["temperature"],
    elevation=forecast_data["elevation"],
    windspeed=forecast_data["current_weather"]["windspeed"],
    observation_time=forecast_data["current_weather"]["time"]
)

print("city:", report.city)
print("country:", report.country)
print("latitude:", report.latitude)
print("longitude:", report.longitude)
print("temperature:", report.temperature)
print("elevation:", report.elevation)
print("windspeed:", report.windspeed)
print("time:", report.observation_time)


