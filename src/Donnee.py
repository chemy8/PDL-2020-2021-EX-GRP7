from bs4 import BeautifulSoup
import requests
import pandas as pd


# with <th> & class wikitable
# url = "https://en.wikipedia.org/wiki/Comparison_between_U.S._states_and_countries_by_GDP_(PPP)"
# url= "https://en.wikipedia.org/wiki/Comparison_between_Ido_and_Novial"

# without <th> & without class
# url="https://en.wikipedia.org/wiki/Comparison_of_Canadian-tax_preparation_software_for_personal_use"

class Donnee:

    urls = ["https://en.wikipedia.org/wiki/Comparison_between_Ido_and_Novial",
            "https://en.wikipedia.org/wiki/Comparison_between_U.S._states_and_countries_by_GDP_(PPP)"]
    for j in urls:

        html_content = requests.get(j).text

        soup = BeautifulSoup(html_content, "html.parser")
        # print(soup.prettify())

        table = soup.find("table", {'class': 'wikitable'}).tbody
        rows = table.find_all("tr")
        columns = [v.text.replace('\n', '') for v in rows[0].find_all("th")]

        df = pd.DataFrame(columns=columns)

        for i in range(1, len(rows)):
            tds = rows[i].find_all("td")
            values = [td.text.replace('\n', '') for td in tds]
            # print(j, values)
            df = df.append(pd.Series(values, index=columns), ignore_index=True)
            title = soup.title.text
            df.to_csv(r'D:\workspace\PDL-2020-2021-EX-GRP7' + '\\' + title + '.csv', index=False)
