from flask import Flask, render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/90546/Desktop/ToDoApp/todo.db'
db = SQLAlchemy(app)

@app.route("/")
def index():
    todos= Todo.query.all()

    return render_template("index.html",todos=todos)

@app.route("/add",methods=["post"])
def addToDo():
    title = request.form.get("title")
    newToDo = Todo(title= title,complete=False)
    db.session.add(newToDo)
    db.session.commit()

    return redirect(url_for("index"))




class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
    
