
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("flask_index_v12.html")

@app.route("/about")
def about():
    return render_template("flask_about_v12.html")

@app.route("/article/<string:id>")
def detail(id):
    return "Article ID: "+id


if __name__ == "__main__":
    app.run(debug=True)
