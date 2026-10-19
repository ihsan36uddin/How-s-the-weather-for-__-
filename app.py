from flask import Flask, render_template, request
from weather import geocoding, get_weather, calculate_football_score
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    weather = None
    if request.method == "POST":
        chosen_loc = request.form.get("location")
        latitude, longitude = geocoding(chosen_loc)

        weather = get_weather(latitude, longitude)
        score = calculate_football_score(
            weather["rain"],
            weather["humidity"],
            weather["snow"],
            weather["temperature"],
            weather["wind_speed"],

        )

    return render_template("index.html", score=score, weather=weather)

if __name__ == "__main__":
    app.run(port=5001, debug=True)

