from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

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


@app.route("/login")
def login():
  return render_template("login.html")


@app.route("/join-now")
def join_now():
  return render_template("join-now.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
