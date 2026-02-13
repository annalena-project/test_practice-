# a.

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
#print(response.json())        # Converts the server response to a Python dictionary and prints the data

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

