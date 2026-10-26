import requests

def geocoding(location):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {
    "name": location
    }
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    if data.get("results"):
        latitude = data["results"][0]["latitude"] 
        longitude = data["results"][0]["longitude"]
        return latitude, longitude 
    else:
        raise ValueError("City not found")

def get_weather(latitude, longitude):
    url2 = "https://api.open-meteo.com/v1/forecast"
    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "wind_speed_unit": "mph",
        "current": "temperature_2m,relative_humidity_2m,is_day,rain,snowfall,wind_speed_10m,"
    }
    weather_response = requests.get(url2, params=weather_params, timeout=10)
    weather_response.raise_for_status()
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

    # Rainfall (maximum 25 points)
    if rain == 0:
        rain_score = 25
    elif rain < 0.5:
        rain_score = 20
    elif rain < 2:
        rain_score = 15
    elif rain < 5:
        rain_score = 5
    else:
        rain_score = 0

    # Humidity (maximum 10 points)
    if 30 <= humidity <= 60:
        humidity_score = 10
    elif humidity < 75:
        humidity_score = 7
    elif humidity < 85:
        humidity_score = 3
    else:
        humidity_score = 0

    # Snowfall (maximum 15 points)
    if snow == 0:
        snow_score = 15
    elif snow < 0.5:
        snow_score = 10
    elif snow < 2:
        snow_score = 5
    else:
        snow_score = 0

    # Temperature (maximum 30 points)
    if 10 <= temp <= 18:
        temp_score = 30
    elif 5 <= temp < 10 or 18 < temp <= 23:
        temp_score = 25
    elif 0 <= temp < 5 or 23 < temp <= 28:
        temp_score = 15
    elif -5 <= temp < 0 or 28 < temp <= 32:
        temp_score = 5
    else:
        temp_score = 0

    # Wind speed in mph (maximum 20 points)
    if speed < 5:
        wind_score = 20
    elif speed < 10:
        wind_score = 17
    elif speed < 15:
        wind_score = 12
    elif speed < 25:
        wind_score = 5
    else:
        wind_score = 0

    return rain_score + humidity_score + snow_score + temp_score + wind_score



def calculate_running_score(rain, humidity, snow, temp, speed):
    # Rainfall (maximum 20 points)
    if rain < 0.5:
        rain_score = 20
    elif rain < 2:
        rain_score = 15
    elif rain < 5:
        rain_score = 5
    else:
        rain_score = 0

    # Humidity (maximum 15 points)
    if 30 <= humidity <= 60:
        humidity_score = 15
    elif humidity < 75:
        humidity_score = 10
    elif humidity < 85:
        humidity_score = 5
    else:
        humidity_score = 0

    # Snowfall (maximum 10 points)
    if snow == 0:
        snow_score = 10
    elif snow < 0.5:
        snow_score = 5
    else:
        snow_score = 0

    # Temperature (maximum 35 points)
    if 8 <= temp <= 16:
        temp_score = 35
    elif 4 <= temp < 8 or 16 < temp <= 20:
        temp_score = 25
    elif 0 <= temp < 4 or 20 < temp <= 25:
        temp_score = 15
    else:
        temp_score = 0

    # Wind speed (maximum 20 points)
    if speed < 10:
        wind_score = 20
    elif speed < 15:
        wind_score = 15
    elif speed < 25:
        wind_score = 5
    else:
        wind_score = 0

    return rain_score + humidity_score + snow_score + temp_score + wind_score

def calculate_golf_score(rain, humidity, snow, temp, speed):
    # Rain (maximum 30 points)
    if rain == 0:
        rain_score = 30
    elif rain < 0.5:
        rain_score = 20
    elif rain < 2:
        rain_score = 10
    else:
        rain_score = 0

    # Humidity (maximum 5 points)
    if humidity < 70:
        humidity_score = 5
    elif humidity < 85:
        humidity_score = 3
    else:
        humidity_score = 0

    # Snow (maximum 10 points)
    if snow == 0:
        snow_score = 10
    elif snow < 0.5:
        snow_score = 5
    else:
        snow_score = 0

    # Temperature (maximum 25 points)
    if 15 <= temp <= 24:
        temp_score = 25
    elif 10 <= temp < 15 or 24 < temp <= 28:
        temp_score = 20
    elif 5 <= temp < 10 or 28 < temp <= 32:
        temp_score = 10
    else:
        temp_score = 0

    # Wind speed (maximum 30 points)
    if speed < 5:
        wind_score = 30
    elif speed < 10:
        wind_score = 25
    elif speed < 15:
        wind_score = 15
    elif speed < 20:
        wind_score = 5
    else:
        wind_score = 0

    return rain_score + humidity_score + snow_score + temp_score + wind_score


def calculate_basketball_score(rain, humidity, snow, temp, speed):
    # Rain (maximum 25 points)
    if rain == 0:
        rain_score = 25
    elif rain < 0.5:
        rain_score = 15
    elif rain < 2:
        rain_score = 5
    else:
        rain_score = 0

    # Humidity (maximum 10 points)
    if 30 <= humidity <= 60:
        humidity_score = 10
    elif humidity < 75:
        humidity_score = 7
    elif humidity < 85:
        humidity_score = 3
    else:
        humidity_score = 0

    # Snow (maximum 15 points)
    if snow == 0:
        snow_score = 15
    elif snow < 0.5:
        snow_score = 5
    else:
        snow_score = 0

    # Temperature (maximum 30 points)
    if 15 <= temp <= 22:
        temp_score = 30
    elif 10 <= temp < 15 or 22 < temp <= 27:
        temp_score = 20
    elif 5 <= temp < 10 or 27 < temp <= 32:
        temp_score = 10
    else:
        temp_score = 0

    # Wind speed (maximum 20 points)
    if speed < 5:
        wind_score = 20
    elif speed < 10:
        wind_score = 15
    elif speed < 15:
        wind_score = 10
    elif speed < 20:
        wind_score = 5
    else:
        wind_score = 0

    return rain_score + humidity_score + snow_score + temp_score + wind_score


def calculate_skiing_score(rain, humidity, snow, temp, speed):
    # Rain (maximum 25 points)
    if rain == 0:
        rain_score = 25
    elif rain < 0.5:
        rain_score = 15
    elif rain < 2:
        rain_score = 5
    else:
        rain_score = 0

    # Humidity (maximum 5 points)
    if humidity < 70:
        humidity_score = 5
    elif humidity < 90:
        humidity_score = 3
    else:
        humidity_score = 0

    # Snowfall (maximum 10 points)
    if 0 <= snow < 0.5:
        snow_score = 10
    elif snow < 2:
        snow_score = 7
    elif snow < 5:
        snow_score = 3
    else:
        snow_score = 0

    # Temperature (maximum 30 points)
    if -10 <= temp <= -2:
        temp_score = 30
    elif -15 <= temp < -10 or -2 < temp <= 2:
        temp_score = 20
    elif -20 <= temp < -15 or 2 < temp <= 5:
        temp_score = 10
    else:
        temp_score = 0

    # Wind speed (maximum 30 points)
    if speed < 10:
        wind_score = 30
    elif speed < 15:
        wind_score = 25
    elif speed < 25:
        wind_score = 15
    elif speed < 35:
        wind_score = 5
    else:
        wind_score = 0

    return rain_score + humidity_score + snow_score + temp_score + wind_score

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
