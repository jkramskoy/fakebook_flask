from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello visitor!Nice to see you on my website!"

@app.route("/about")
def about_me():
    return "I am a SmartNinja student.This is my Fakebook website"

@app.route("/portfolio")
def portfolio():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(port="5000")

