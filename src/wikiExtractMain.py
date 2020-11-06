from src.Url import Url


class wikiExtractMain:
    # exemple for test URL
    url = "https://annuel2.framapad.org/p/r.35d94f38fd3cbed4e5664cab60aad1f7"
    title = "test title !"
    validURL = Url.estTitreValid(title) and Url.estWikiPage(url)
    print(validURL)
