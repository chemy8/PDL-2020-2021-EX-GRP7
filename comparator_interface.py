import flask
from flask import Flask, render_template, request
import subprocess

from src.Donnee import Donnee

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/urlForm/", methods=['POST', 'GET'])
def move_forward():
    forward_message = "Moving Forward..."
    if request.method == 'POST':
        url = flask.request.form.get('url')
        ext = flask.request.form.get('extractors')
        if ext == "H" or ext == "W":
            subprocess.call(['java', '-jar',
                             'D:\workspace\PDL_2020-2021_GR7\\target\WikipediaMatrix-0.0.1-SNAPSHOT.jar',
                             url, ext])
        else:
            Donnee.extraire(url)

    print(flask.request.form)
    return render_template('index.html', forward_message=forward_message)


if __name__ == '__main__':
    app.run(port=5000)
