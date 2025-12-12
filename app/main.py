from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    current_dt = now.strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"LNPR App Running with correct package version! "
        f"Hello Dani! CI/CD working — updated version! , added 2 line "
        f"(Current time: {current_dt})"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
#hello
