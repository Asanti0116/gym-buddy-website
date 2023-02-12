from flask import Flask, request, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension

import requests

#################################################################
# API INFO
url = "https://exercisedb.p.rapidapi.com/exercises/target/%7Btarget%7D"

headers = {
  "X-RapidAPI-Key": "9ded74f4f8msha4284305d05698dp19f784jsn6e8a645eabe3",
  "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)

#################################################################

app = Flask(__name__)

app.config['SECRET_KEY'] = 'santiago8675309'
debug = DebugToolbarExtension(app)


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


@app.route('/sign-up')
def sign_up():
  return render_template('sign-up.html')


@app.route("/login")
def login():
  return render_template("login.html")


@app.route("/log-out")
def log_out():
  return render_template("log-out.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
