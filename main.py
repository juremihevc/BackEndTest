from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    some_text = "Message from the handler!"
    current_year = datetime.datetime.now().year

    cities = ["Boston", "Vienna", "Paris", "Berlin"]

    return render_template("index.html", some_text=some_text, current_year=current_year, cities=cities)

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

if __name__ == '__main__':
    app.run(use_reloader=True)