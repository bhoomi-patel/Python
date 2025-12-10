from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///project.db"
db = SQLAlchemy(app)

# model definition
# This class represents the 'todo' table in our database.
class Todo(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    task = db.Column(db.String(200),nullable=False)
    done = db.Column(db.Boolean,default=False)
with app.app_context():
    db.create_all()
# READ all task(home page)
@app.route("/")
def home():
    todo_list = db.session.execute(db.select(Todo).order_by(Todo.id)).scalars().all()
    return render_template("todos.html",todo_list=todo_list)
# create new task
@app.route("/add",methods=["POST"])
def add():
    task_text=request.form.get("task")
    new_todo = Todo(task=task_text)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("home"))
# UPDATE a task's status
@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("home"))

# DELETE a task
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = db.get_or_404(Todo, todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)