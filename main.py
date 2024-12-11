from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Главная страница</h1>"

@app.route("/page1")
def page1():
    return "<h1>Страница 1</h1>"

@app.route("/coin_flip")
def coin_flip():
    result = "Орел" if random.choice([True, False]) else "Решка"
    return render_template("coin_flip.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
