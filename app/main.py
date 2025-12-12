from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "LNPR App Running with correct package version! Hello Dani! CI/CD working — updated version! , added 2 line"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
#hello