
from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt


# kayıt formu
class RegisterForm(Form):
    name = StringField("isim",validators=[validators.length(min=4,max=25)])
    username = StringField("kullanıcı adı",validators=[validators.length(min=5,max=35)])
    email = StringField("email",validators=[validators.Email(message="geçerli email gir")])
    password = PasswordField("parolo",validators=[
        validators.data_required(message="parola belirleyin"),
        validators.EqualTo(fieldname="confirm",message= "hatalı parola")
    ])
    confirm = PasswordField("Parola doğrula")





app = Flask(__name__)

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "ybblog"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)



@app.route("/")
def index():

    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/register",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)
    
    if request.method == "POST":
        return redirect(url_for("index"))
    else:
        return render_template("register.html",form=form)


@app.route("/article/<string:id>")
def detail(id):
    return "Article ID: "+id


if __name__ == "__main__":
    app.run(debug=True)
