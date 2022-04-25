
import email
from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,TextAreaField,PasswordField,validators
from passlib.hash import sha256_crypt
from functools import wraps

#kullanıcı giriş decorator
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Sayfayı görüntülemek için giriş yapın","danger")
            return redirect(url_for("login"))
    return decorated_function


#kullanıcı kayıt formu
class RegisterForm(Form):
    name = StringField("isim",validators=[validators.length(min=4,max=25)])
    username = StringField("kullanıcı adı",validators=[validators.length(min=5,max=35)])
    email = StringField("email",validators=[validators.Email(message="geçerli email gir")])
    password = PasswordField("parolo",validators=[
        validators.data_required(message="parola belirleyin"),
        validators.EqualTo(fieldname="confirm",message= "hatalı parola")
    ])
    confirm = PasswordField("Parola doğrula")


class LoginForm(Form):
    username = StringField("Kullanıcı Adı")
    password = PasswordField("parola")


app = Flask(__name__)
app.secret_key = "ybblog"


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


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


#kayıt olma
@app.route("/register",methods = ["GET","POST"])
def register():
    form = RegisterForm(request.form)
    
    if request.method == "POST" and form.validate() :
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(form.password.data)
        
        cursor = mysql.connection.cursor()

        sorgu = "Insert into users(name,email,username,password) VALUES(%s,%s,%s,%s)"

        cursor.execute(sorgu,(name,email,username,password))
        mysql.connection.commit()

        cursor.close()
        flash("Başarıyla kayıt oldun...","success") 
        return redirect(url_for("login"))
    else:
        return render_template("register.html",form=form)


@app.route("/article/<string:id>")
def detail(id):
    return "Article ID: "+id

#login işlemi
@app.route("/login",methods = ["GET","POST"])
def login():
    form = LoginForm(request.form)
    if request.method == "POST":
        username = form.username.data
        password_entered = form.password.data

        cursor = mysql.connection.cursor()

        sorgu = "Select * From users where username = %s"
        result = cursor.execute(sorgu,(username,))

        if result >0:
            data = cursor.fetchone()
            real_password = data["password"]
            if sha256_crypt.verify(password_entered,real_password):
                flash("başarıyla giriş yaptınız...","success")

                session["logged_in"] = True
                session["username"] = username



                return redirect(url_for("index"))
            else:
                flash("yanlış parola...","danger")
                return redirect(url_for("login"))
        else:
            flash("Böyle bir kullanıcı yok...","danger")
            return redirect(url_for("login"))
    return render_template("login.html",form = form)


#logout işlemi
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


#makale ekleme
@app.route("/addarticle",methods= ["GET","POST"])
def addarticle():
    form = ArticleForm(request.form)
    if request.method == "POST" and form.validate():
        title = form.title.data
        content = form.content.data
         
        cursor = mysql.connection.cursor()
        sorgu = "Insert into articles(title,author,content) VALUES(%s,%s,%s)"
        cursor.execute(sorgu,(title,session["username"],content))

        mysql.connnection.commit()
        cursor.close()
        flash("makale eklendi...","success")
        return redirect(url_for("dashboard"))
        
    return render_template("addarticle.html",form = form)

#makale form
class ArticleForm(Form):
    title = StringField("Makale Başlığı",validators = [validators.Length(min = 5,max= 100)])
    content = TextAreaField("Makale İçeriği",validators=[validators.Length(min=10)])




if __name__ == "__main__":
    app.run(debug=True)
