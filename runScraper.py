from bs4 import BeautifulSoup
import requests
from nbaScraper import scrapeNBASite
import pandas as pd
import time
# city-state 08-17-2022-to-08-12-2022/
racesURL = "https://runningintheusa.com/classic/list/{}-{}/{}/half-marathon/"

def main():
    matchups = scrapeNBASite()
    scrapeRunSite(matchups)

def scrapeRunSite(matchups):
    headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }

    for matchup in matchups:
        url = f'{racesURL.format(matchup["city"], matchup["state"], matchup["date"])}'
        # print(url)
        req =  requests.get(url, headers = headers)
        # print(req)
        soup = BeautifulSoup(req.content, 'html.parser')
        tables = soup.find("table", {"class": "table table-bordered table-condensed"})
        if (len(tables) == 3):
            time.sleep(1)
            continue
        df_list = pd.read_html(req.content)
        print(f"# Date Range: {matchup['date']}: {matchup['teams']} on {matchup['gameDate']}")
        print(f"{df_list[0][['Race Date', 'Race']].to_markdown()}")
        print()
        time.sleep(2)


if __name__ == "__main__":
    main()