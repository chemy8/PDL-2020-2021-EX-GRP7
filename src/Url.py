import re


class Url:

    # Verify that is a wikipedia page
    def estWikiPage(url):
        pattern = re.compile("https://(fr|en).wikipedia.org/(w|wiki)/")
        return pattern.match(url)

    # Verify that the titre not empty
    def estTitreValid(titre):
        pattern = re.compile("(.|\s)*\S(.|\s)*")
        return pattern.match(titre)
