from flask import Flask, render_template, request
from weather import geocoding, get_weather, calculate_football_score, get_verdict
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    score = None
    weather = None
    verdict = None
    chosen_loc = None
    input_error = False
    if request.method == "POST":
        chosen_loc = request.form.get("location")
        try:
            latitude, longitude = geocoding(chosen_loc)
            weather = get_weather(latitude, longitude)
            score = calculate_football_score(
            weather["rain"],
            weather["humidity"],
            weather["snow"],
            weather["temperature"],
            weather["wind_speed"],
            )
            verdict = get_verdict(score, "football")
        except ValueError:
            input_error = True 

    return render_template("index.html", score=score, 
                           weather=weather, 
                           verdict=verdict, 
                           location=chosen_loc,
                           input_error=input_error,
                           
                           )

if __name__ == "__main__":
    app.run(port=5001, debug=True)

