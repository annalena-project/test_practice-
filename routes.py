from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Weather Tracker Homepage!"

@app.route("/ingest")
def create_observation():
    return "Create a new weather observation"

@app.route("/observations")
def observations():
    return "Retrieve all the observations"

@app.route("/observations/<int:observation_id>")
def observation(observation_id):
    return f"Retrieve observation {observation_id}"

@app.route("/observations/<int:observation_id>/edit", methods=["GET", "POST"])
def edit_observation(observation_id):
    return f"Update observation {observation_id}"

@app.route("/observations/<int:observation_id>/delete", methods=["GET", "POST"])
def delete_observation(observation_id):
    return f"Delete observation {observation_id}"

if __name__ == "__main__":
    app.run(debug=True)