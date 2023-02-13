from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from models import db
from os import path

import requests

db = SQLAlchemy()
DB_NAME = "database.db"

#################################################################
# ExerciseDB API INFO
url = "https://exercisedb.p.rapidapi.com/exercises/target/%7Btarget%7D"

headers = {
  "X-RapidAPI-Key": "9ded74f4f8msha4284305d05698dp19f784jsn6e8a645eabe3",
  "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)



#################################################################

app = Flask(__name__)

from models import User, Note

create_database(app)

return app

def create_database(app):
  if not path.exists('gym-buddy-website/' + DB_NAME):
    db.create_all(app=app)
    print('Created Database!')

app.config['SECRET_KEY'] = 'santiago8675309'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db.init_app(app)


@app.route("/")
def home_page():
  return render_template('home.html')


@app.route("/exercise-of-the-day")
def exercise_of_the_day():
  return render_template('exercise-of-the-day.html')


@app.route("/motivation")
def motivation():
  return render_template("motivation.html")


@app.route("/workouts")
def workouts():
  return render_template("workouts.html")


@app.route("/notes")
def notes():
  return render_template("notes.html")


#################################################################
# User signup/login/logout


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
  if request.method == 'POST':
    email = request.form.get('email')
    firstName = request.form.get('firstName')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    if len(email) < 4:
      flash('Email must be greater than 3 characters.', category='error')
    elif len(firstName) < 2:
      flash('First name must be greater than 1 characters.', category='error')
    elif password1 != password2:
      flash('Passwords don\'t match.', category='error')
    elif len(password1) < 7:
      flash('Password must be atleast 7 characters.', category='error')
    else:
      flash('Account created!', category='success')

  return render_template('sign-up.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
  return render_template("login.html", boolean=True)


@app.route("/log-out")
def log_out():
  return render_template("log-out.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
