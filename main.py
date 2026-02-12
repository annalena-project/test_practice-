import requests 

URL = "https://geocoding-api.open-meteo.com/v1/search"

parameters = {
    "name": "Karlstad",         # city 
    "country": "Sweden",
    "count": 1
}

response = requests.get(URL, params=parameters, timeout=10)  
# response a variable that contains: requests.get: sending a requset to server, URL.
# params=parameters: The server uses them to know what to return.

print(response.status_code)   # Prints the HTTP status code. It shows what response the server sent back (200, 400, 500)
print(response.json())        # Converts the server response to a Python dictionary and prints the data

data = response.json()        # Converts the server response from JSON format to a Python dictionary

results = data["results"]     
first_result = results[0]

latitude = first_result["latitude"]   
longitude = first_result["longitude"]

print("latitude:", latitude)   # Prints the latitude / longitude value
print("longitude:", longitude)
