import requests
from flask import Flask, render_template, request
from weather import (geocoding, 
                     get_weather, 
                     calculate_football_score, 
                     calculate_running_score, 
                     calculate_golf_score, 
                     calculate_basketball_score,
                     calculate_skiing_score, 
                     get_verdict)
app = Flask(__name__)

sports = {
    "Football": calculate_football_score,
    "Running": calculate_running_score,
    "Golf": calculate_golf_score,
    "Basketball": calculate_basketball_score,
    "Skiing": calculate_skiing_score,
}


@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    weather = None
    verdict = None
    chosen_loc = None
    chosen_activity = None
    input_error = False
    api_error = False

    if request.method == "POST":
        chosen_loc = request.form.get("location")
        chosen_activity = request.form.get("activity")
        if not chosen_loc.strip():
            input_error = True
        else:
            try:
                latitude, longitude = geocoding(chosen_loc)
                weather = get_weather(latitude, longitude)

                if chosen_activity in sports:
                    score = sports[chosen_activity](
                    weather["rain"],
                    weather["humidity"],
                    weather["snow"],
                    weather["temperature"],
                    weather["wind_speed"],                    
                    )
                    verdict = get_verdict(score, chosen_activity)

            except ValueError:
                input_error = True 

            except requests.exceptions.RequestException:
                api_error = True


    return render_template("index.html", score=score, 
                           weather=weather, 
                           verdict=verdict, 
                           location=chosen_loc,
                           input_error=input_error,
                           api_error=api_error,
                           activity=chosen_activity,

                           )

if __name__ == "__main__":
    app.run(port=5001, debug=True)

