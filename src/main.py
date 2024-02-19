import os

from flask import Flask, render_template, request

WORLD = os.getenv("WORLD", "docker")

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello():
    name = None

    if request.method == "POST":
        name = request.form["name"]

    context = {
        "name": name,
        "world": WORLD
    }

    return render_template("index.html", **context)


app.run(host='0.0.0.0', port=8000, debug=True)
