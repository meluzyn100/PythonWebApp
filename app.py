from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is a sample Python Web App running on Flask Framework!!!"

@app.route("/name")
def name():
    return "Hello name"

