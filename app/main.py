from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    current_dt = now.strftime("%Y-%m-%d %H:%M:%S")

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
        </style>
      </head>
      <body>
        <div class="card">
          <div class="title">LNPR App Runningddd1 ✅</div>
          <div class="subtitle">
            Correct package version · CI/CD working · Updated version · Added 2 lines
          </div>
          <div class="time">Current server time: {current_dt}</div>
                    <div class="title">LNPRd end of the line hello✅ +  dline added +2 line added, hello+3 kline </div>

        </div>
      </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
#
