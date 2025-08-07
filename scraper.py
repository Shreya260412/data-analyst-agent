import pandas as pd
import requests
from bs4 import BeautifulSoup

def scrape_grossing_films():
    url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    table = soup.find("table", {"class": "wikitable"})
    rows = table.find_all("tr")[1:]

    data = []
    for row in rows:
        cols = row.find_all("td")
        if len(cols) < 5:
            continue
        try:
            rank = int(cols[0].text.strip().replace('.', ''))
            title = cols[1].text.strip()
            gross = cols[2].text.strip().replace('$', '').replace(',', '')
            year = int(cols[-1].text.strip())
            data.append({
                "Rank": rank,
                "Title": title,
                "Worldwide gross": float(gross),
                "Year": year
            })
        except:
            continue

    return pd.DataFrame(data)
