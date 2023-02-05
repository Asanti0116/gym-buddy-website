from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
  return render_template('home.html')


@app.route("/motivation")
def motivation():
  return render_template("motivation.html")


@app.route("/workouts")
def workouts():
  return render_template("workouts.html")


@app.route("/exerciseOfTheDay")
def exerciseOfTheDay():
  return render_template("exerciseOfTheDay.html")


@app.route("/login")
def login():
  return render_template("login.html")


@app.route("/notes")
def notes():
  return render_template("notes.html")


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
