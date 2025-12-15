from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

def get_coimbatore_weather():
    try:
        # Coimbatore approx: 11.01, 76.97 [web:41]
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": 11.01,
            "longitude": 76.97,
            "current_weather": True,
            "timezone": "Asia/Kolkata"
        }
        resp = requests.get(url, params=params, timeout=3)
        resp.raise_for_status()
        data = resp.json()
        current = data["current_weather"]  # temp in °C by default [web:38][web:21]
        temp_c = current["temperature"]
        wind_speed = current["windspeed"]
        weather_code = current["weathercode"]
        return f"{temp_c}°C", f"{wind_speed} km/h", f"Code {weather_code}"
    except Exception:
        # Safe fallback if API/network fails
        return "N/A", "N/A", "Unavailable"

@app.route("/")
def home():
    now = datetime.now()
    current_dt = now.strftime("%Y-%m-%d %H:%M:%S")

    temp_c, wind_speed, weather_status = get_coimbatore_weather()

    html = f"""
    <html>
      <head>
        <title>LNPR Status</title>
        <style>
          body {{
            background-color: #121212;
            color: #f5f5f5;
            font-family: Arial, sans-serif;
            padding: 40px;
          }}
          .card {{
            max-width: 800px;
            margin: auto;
            background: #1e1e1e;
            border-radius: 10px;
            padding: 24px 32px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.6);
          }}
          .title {{
            color: #4caf50;
            font-size: 24px;
            margin-bottom: 12px;
          }}
          .subtitle {{
            color: #ff9800;
            font-size: 18px;
            margin-bottom: 8px;
          }}
          .time {{
            color: #03a9f4;
            font-size: 16px;
          }}
          .weather {{
            color: #9c27b0;
            font-size: 16px;
            margin-top: 16px;
            padding: 12px;
            background: rgba(156, 39, 176, 0.1);
            border-radius: 6px;
            border-left: 4px solid #9c27b0;
          }}
        </style>
      </head>
      <body>
        <div class="card">
          <div class="title">LNPR App Running ✅</div>
          <div class="subtitle">
            Correct package version · CI/CD working · Updated version · Added 2 lines
          </div>
          <div class="time">Current server time: {current_dt}</div>

          <div class="weather">
            🌤️ Coimbatore Weather: {temp_c}, Wind: {wind_speed}, Status: {weather_status}
          </div>

          <div class="title">LNPR end of the line ✅ + 1 line added +2 line added</div>
        </div>
      </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
