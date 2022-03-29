from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    article = dict()
    article["title"] = "deneme"
    article["body"] = "deneme123"
    article["author"] = "sen"


    return render_template("index_v5.html",article=article)


if __name__ == "__main__":
    app.run(debug=True)
