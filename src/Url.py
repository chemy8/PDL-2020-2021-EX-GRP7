import re


class Url:


    url = "https://www.guru99.com/python-regular-expressions-complete-tutorial.html"

    # Verify that is a wikipedia page
    def estWikiPage(url):
        pattern = re.compile("https://(fr|en).wikipedia.org/(w|wiki)/")
        return pattern.match(url)

    print(estWikiPage(url))

    # Verify that the titre not empty
    def estTitreValid(titre):
        pattern = re.compile("(.|\s)*\S(.|\s)*")
        return pattern.match(titre)

    print(estTitreValid(" "))
