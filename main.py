from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/introduce")
def introduce():
    return render_template("introduce.html")

@app.route("/dog")
def dog():
    return render_template('dog.html')

@app.route("/photo")
def photo():
    return render_template('photo.html')



if __name__ == "__main__":
    app.run()
