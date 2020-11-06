from bs4 import BeautifulSoup
import requests
import pandas as pd
from src.Url import Url


class Donnee:
    # Extraire() method to extract and generate csv
    def extraire(url):
        # TEST === > Verify URL
        if Url.estWikiPage(url) is not None:
            # Get html code
            html_content = requests.get(url).text.replace('\n', '')
            # Parse html data
            soup = BeautifulSoup(html_content, "html.parser")
            # TEST ==>  verify that page contains tables
            if soup.find("table", {'class': 'wikitable'}) is not None:
                # Get table
                table = soup.find("table", {'class': 'wikitable'})
                # Get rows
                rows = table.find_all("tr")
                # Get columns data
                columns = [v.text.replace('\n', '') for v in rows[0].find_all("th")]
                # Create data structure
                df = pd.DataFrame(columns=columns)
                # Initialize tables
                ths = []
                tds = []
                # Get data from rows
                for i in range(1, len(rows)):
                    tds = rows[i].find_all("td")
                    ths = rows[i].find_all("th")
                    # Some rows contains th and td in the same time ; so we create data to recuperate both
                    data = tds + ths
                    # Clean data
                    values = [td.text.replace('\n', '') for td in data]
                    # First case ; Verify that numbers of data(columns by row) and columns (head of table) are
                    # the same ==> So we can index data by columns
                    if len(data) == len(columns):
                        df = df.append(pd.Series(values, index=columns), ignore_index=True)
                    # Second case ; Verify that numbers of data(columns by row) < columns (head of table)
                    # So here to be able to index data by columns we added white spaces to data
                    elif len(data) < len(columns):
                        for j in range(0, len(data)):
                            length = j + 1
                        for k in range(length + 1, len(columns) + 1):
                            values.append('')
                        df = df.append(pd.Series(values, index=columns), ignore_index=True)
                    # Second case ; Verify that numbers of data(columns by row) > columns (head of table)
                    # So here to be able to index data by columns we added white spaces to columns
                    else:
                        for j in range(0, len(columns)):
                            length = j + 1
                        for k in range(length + 1, len(data) + 1):
                            columns.append('')
                        df = pd.DataFrame(columns=columns)
                        df = df.append(pd.Series(values, index=columns), ignore_index=True)
                # Get title of page
                title = soup.title.text
                # Generate csv file
                # You should edit this path with the path of your project ( in your local) to recuperate csv files
                df.to_csv(r'D:\workspace\PDL-2020-2021-EX-GRP7\output' + '\\' + title + '.csv', index=False)
            else:
                title = soup.title.text
                print("Aucun tableau present dans la page : ", title)

        else:
            print("Cet url ne correspond pas à une page wikipedia", url)



    # Read 300+ urls from file
    with open('../Urls') as file:
        data = file.read().splitlines()
        for url in data:
            extraire(url)
