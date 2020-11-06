from bs4 import BeautifulSoup
import requests
import pandas as pd


class Donnee:
    # Read urls from file
    with open('../Urls') as file:
        data = file.read().splitlines()
        for url in data:
            html_content = requests.get(url).text.replace('\n', '')

            # Parse html data
            soup = BeautifulSoup(html_content, "html.parser")

            # TEST ==>  verify that page contains tables
            if soup.find("table", {'class': 'wikitable'}) is not None:

                table = soup.find("table", {'class': 'wikitable'})
                rows = table.find_all("tr")

                columns = [v.text.replace('\n', '') for v in rows[0].find_all("th")]

                df = pd.DataFrame(columns=columns)

                ths = []
                tds = []

                for i in range(1, len(rows)):
                    tds = rows[i].find_all("td")
                    ths = rows[i].find_all("th")
                    data = tds + ths
                    values = [td.text.replace('\n', '') for td in data]
                    if len(data) == len(columns):
                        df = df.append(pd.Series(values, index=columns), ignore_index=True)
                    else:
                        for j in range(0, len(data)):
                            length = j + 1
                        for k in range(length + 1, len(columns) + 1):
                            values.append('')
                    df = df.append(pd.Series(values, index=columns), ignore_index=True)

                title = soup.title.text
                # Generate csv file
                df.to_csv(r'D:\workspace\PDL-2020-2021-EX-GRP7' + '\\' + title + '.csv', index=False)
            else:
                title = soup.title.text
                print("Aucun tableau present dans la page : ", title)
