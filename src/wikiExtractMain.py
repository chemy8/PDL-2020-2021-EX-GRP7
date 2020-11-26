from src.Donnee import Donnee
from src.Url import Url
from flask import Flask

class wikiExtractMain:
    # exemple for test URL
    url = "https://annuel2.framapad.org/p/r.35d94f38fd3cbed4e5664cab60aad1f7"
    title = "test title !"
    validURL = Url.estTitreValid(title) and Url.estWikiPage(url)
    print(validURL)

    # exemple to extract csv
    # to test this code you should comment the part of code (Read 300+ urls from file) in class Donnee
    url = "https://en.wikipedia.org/wiki/Comparison_of_dance_video_games"
    Donnee.extraire(url)

