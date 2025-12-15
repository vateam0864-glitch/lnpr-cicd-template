from flask import Flask
from datetime import datetime
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    current_dt = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Fetch Coimbatore weather (lat: 11.0168, lon: 76.9558)
    try:
        weather_url = "https://api.open-meteo.com/v1/forecast?latitude=11.0168&longitude=76.9558&current_weather=true&temperature_unit=fahrenheit&wind_speed_unit=kmh&precipitation_unit=mm"
        response = requests.get(weather_url, timeout=5)
        weather_data = response.json()
        current_weather = weather_data['current']
        temp_c = round((current_weather['temperature_2m'] - 32) * 5/9, 1)
        wind_speed = current_weather['windspeed_10m']
        precip = current_weather['precipitation']
        weather_status = "Clear" if precip == 0 else f"{precip}mm rain"
    except:
        temp_c = "N/A"
        wind_speed = "N/A"
        weather_status = "Unavailable"
    
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
            🌤️ Coimbatore Weather: {temp_c}°C, Wind: {wind_speed}km/h, {weather_status}
          </div>
          
          <div class="title">LNPR end of the line ✅ + 1 line added +2 line added</div>
        </div>
      </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
