from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def index():
    numbers = [1,2,3,4,5]
    numbers2 = (1,2,3,4,5)

    articles = [
        {"id":1,"title":"deneme1","content":"içerik 1"},
        {"id":2,"title":"deneme2","content":"içerik 2"},
        {"id":3,"title":"deneme3","content":"içerik 3"},
    ]



    return render_template("index.html",numbers = numbers,articles =articles )

@app.route("/about")
def about():
    return render_template("flask_about_v11.html")


if __name__ == "__main__":
    app.run(debug=True)
