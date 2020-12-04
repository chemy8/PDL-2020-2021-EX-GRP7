import time

import flask
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import subprocess
from src.Donnee import Donnee
import pandas as pd


app = Flask(__name__)






@app.route('/')
def index():
    return render_template("index.html")


@app.route("/urlForm/", methods=['POST', 'GET'])
def move_forward():
    if request.method == 'POST':
        url = flask.request.form.get('url')
        ext = flask.request.form.get('extractors')
        if ext == "H" or ext == "W":
            subprocess.call(['java', '-jar',
                               'D:\workspace\PDL_2020-2021_GR7\\target\WikipediaMatrix-0.0.1-SNAPSHOT-jar-with-dependencies.jar',
                             url, ext])
            html_content = requests.get(url).text.replace('\n', '')
            # Parse html data
            soup = BeautifulSoup(html_content, "html.parser")
            title = soup.title.text
            start = time.time()
            #Can't generate table because the title generate from java in not the same generate from python
            while time.time() < start + 5:
                df = pd.read_csv("./output/html/" + title + '.csv', header=None)
                heading = list()
                data = list()
                for j in range(0, len(df.values[0])):
                    heading.append(df.values[0][j])
                for i in range(1, len(df.values)):
                    data.append(df.values[i])

        else:
            Donnee.extraire(url)
            html_content = requests.get(url).text.replace('\n', '')
            # Parse html data
            soup = BeautifulSoup(html_content, "html.parser")
            title = soup.title.text
            df = pd.read_csv("./output/" + title + '.csv', header=None)
            heading = list()
            data = list()
            for j in range(0, len(df.values[0])):
                heading.append(df.values[0][j])
            # print(heading)
            for i in range(1, len(df.values)):
                data.append(df.values[i])
            # print(data)
    return render_template('index.html', heading=heading, data=data)

#Generate veritable csv

@app.route("/validForm/", methods=['POST', 'GET'])
def validation():
    Donnee.extract_table("http://127.0.0.1:5000/")
    return render_template('index.html')

#this is an exemple of comparing two csv
def CompareCsv():
    df = pd.read_csv("Comparison_of_S.M.A.R.T._tools  - Wikipedia.csv", header=None)
    df = pd.read_csv("Comparison of S.M.A.R.T. tools - Wikipedia", header=None)
    # affiche l'ensemble de valeurs sous forme de tableau
    print(df.values)
    # #affiche le nombre de lignes et de colonnes (lignes, colonnes)
    print(df.shape)
    # #Recuperation du nombre de lignes
    nbLignes = df.shape[0]
    # #Recuperation du nombre de colonnes
    nbColonnes = df.shape[1]
    print(nbLignes)

if __name__ == '__main__':
    app.run(port=5000)
