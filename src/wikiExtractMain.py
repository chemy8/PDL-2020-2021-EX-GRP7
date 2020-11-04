from src.Url import Url


class wikiExtractMain:

    url = "https://www.guru99.com/python-regular-expressions-complete-tutorial.html"
    title = "test title !"
    validURL = Url.estTitreValid(title) and Url.estWikiPage(url);
    print(validURL)
