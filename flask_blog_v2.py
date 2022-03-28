import re
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Ana Sayfa"

@app.route("/about")
def about():
    return "Hakkımda"

@app.route("/about/kel")
def kel():
    return "kel hakkında"

if __name__ == "__main__":
    app.run(debug=True)
