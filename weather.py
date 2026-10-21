import requests

def geocoding(location):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
    "name": location
    }
    response = requests.get(url, params=params)
    data = response.json()
    latitude = data["results"][0]["latitude"] 
    longitude = data["results"][0]["longitude"]
    return latitude, longitude 

def get_weather(latitude, longitude):
    url2 = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "wind_speed_unit": "mph",
        "current": "temperature_2m,relative_humidity_2m,is_day,rain,snowfall,wind_speed_10m"
    }
    weather_response = requests.get(url2, params=weather_params)
    weather_data = weather_response.json()

    rain = weather_data["current"]["rain"]
    humidity = weather_data["current"]["relative_humidity_2m"]
    snow = weather_data["current"]["snowfall"]
    temperature = weather_data["current"]["temperature_2m"]
    wind_speed = weather_data["current"]["wind_speed_10m"]
    is_day = weather_data["current"]["is_day"]

    return{
        "rain": rain,
        "humidity": humidity,
        "snow": snow,
        "temperature": temperature,
        "wind_speed": wind_speed,
        "is_day": is_day
    }

def calculate_football_score(rain, humidity, snow, temp, speed):
    if rain < 0.6:
        rain_score = 10
    elif rain < 2.5:
        rain_score = 5
    else:
        rain_score = 0

    if humidity < 40:
        humidity_score = 10
    elif humidity < 60:
        humidity_score = 7
    elif humidity < 70:
        humidity_score = 5
    else:
        humidity_score = 0
    
    if snow < 0.3:
        snow_score = 10
    elif snow < 0.6:
        snow_score = 7
    elif snow < 2.5:
        snow_score = 5
    else:
        snow_score = 0 

    if 10 <= temp <= 20:
        temp_score = 10
    elif 20 < temp <= 25:
        temp_score = 7
    elif 5 <= temp <= 10:
        temp_score = 5
    else:
        temp_score = 0

    if speed < 10:
        wind_score = 10
    elif speed < 15:
        wind_score = 7
    elif speed < 20:
        wind_score = 5
    else:
        wind_score = 0

    return (rain_score + humidity_score + snow_score + temp_score + wind_score) * 2

def get_verdict(score, sport):
    if 90 <= score <= 100:
        verdict = f"Excellent conditions for {sport}"
    elif 80 <= score < 90:
        verdict = f"Great conditions for {sport}"
    elif 70 <= score < 80: 
        verdict = f"Good conditions for {sport}"
    elif 60 <= score < 70:
        verdict = f"Tolerable conditions for {sport}"
    elif 50 <= score < 60:
        verdict = f"Not the greatest conditions for {sport}"
    elif 40 <= score < 50:
        verdict = f"Bad conditions for {sport}"
    else:
        verdict = f"Terrible conditions for {sport}"
    return verdict 




# 'current_units': {'cloud_cover': '%',
#                    'interval': 'seconds',
#                    'is_day': '',
#                    'precipitation': 'mm',
#                    'pressure_msl': 'hPa',
#                    'rain': 'mm',
#                    'relative_humidity_2m': '%',
#                    'showers': 'mm',
#                    'snowfall': 'cm',
#                    'temperature_2m': '°C',
#                    'time': 'iso8601',
#                    'weather_code': 'wmo code',
#                    'wind_gusts_10m': 'mp/h',
#                    'wind_speed_10m': 'mp/h'},
