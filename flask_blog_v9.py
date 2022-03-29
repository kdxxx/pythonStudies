from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("flask_index_v9.html")

@app.route("/about")
def about():
    return render_template("flask_about_v9.html")


if __name__ == "__main__":
    app.run(debug=True)
