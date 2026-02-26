from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/weather")
def weather():
    city = request.args.get("city")
    country = request.args.get("country")

    # Geocoding
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_params = {
        "name": city,
        "country": country,
        "count": 1
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()

    result = geo_data["results"][0]
    latitude = result["latitude"]
    longitude = result["longitude"]

    return f"{city}, {country} → lat={latitude}, lon={longitude}"


if __name__ == "__main__":
    app.run(debug=True)

    