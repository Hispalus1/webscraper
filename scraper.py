# https://realpython.com/beautiful-soup-web-scraper-python/
# Modul requests (pip install requests)
import requests
# Import knihovny BeautifulSoup4 (pip install beautifulsoup4), která usnadňuje web scraping
from bs4 import BeautifulSoup
import sys
import json

# Konstanta obsahující adresu webu, z něhož chceme získávat data
# Žebříček 250 nejlépe hodnocených filmů podle serveru imdb.com
URL = 'https://myanimelist.net/topanime.php'
# URL = 'https://www.csfd.cz/zebricky/filmy/nejlepsi/'

# Odeslání požadavku metodou get na určenou URL adresu - HTTP server vrací zpět obsah stránky
# page = requests.get(URL, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'})
page = requests.get(URL)
# Vytvoření objektu parseru stránky
soup = BeautifulSoup(page.content, 'html.parser')

anime_name = soup.select('h3.hoverinfo_trigger.fl-l.fs14.fw-b.anime_ranking_h3')
anime_detail = soup.select('div.information.di-ib.mt4')
anime_score = soup.select('div.js-top-ranking-score-col.di-ib.al')

name_anime = [tag.text for tag in anime_name]
detail_anime = [list(map(str.strip, tag.text.split("\n")[1:-1])) for tag in anime_detail]
score_anime = [float(tag.text) for tag in anime_score]


def comma(i):
    if i < 49:
        file.write(",")
    else:
        pass


with open("anime.json", "w", encoding='utf-8') as file:
    file.write('[')
    for i in range(0, 50):
        row = f'"id": {i + 1},\n "title": "{name_anime[i]}",\n"type": "{detail_anime[i][0].split(" ")[0]}",\n"episodes": "{detail_anime[i][0].split(" ")[1].replace(")","").replace("(","")}",\n"aired": "{detail_anime[i][1]}",\n"members": "{detail_anime[i][2][0:].split(" ")[0].replace(",", "")}",\n "score": "{score_anime[i]}"'
        row = '{' + row + '} '
        print(row)
        file.write(row)
        comma(i)
        file.write('\n')
    file.write(']')


