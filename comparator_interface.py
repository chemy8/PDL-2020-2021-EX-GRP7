import flask
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import subprocess
from src.Donnee import Donnee
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("./output/Comparison of S.M.A.R.T. tools - Wikipedia.csv", header=None)
heading = list()
data = list()
for j in range(0, len(df.values[0])):
    heading.append(df.values[0][j])
#print(heading)
for i in range(1, len(df.values)):
    data.append(df.values[i])
#print(data)


@app.route('/')
def index():
    return render_template("index.html", heading=heading, data=data)


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
    #print(flask.request.form)
    return render_template('index.html', forward_message=forward_message)


@app.route("/validForm/", methods=['POST', 'GET'])
def validation():
    Donnee.extract_table("http://127.0.0.1:5000/")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000)
