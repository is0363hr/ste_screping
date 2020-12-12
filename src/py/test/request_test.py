# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


r = requests.get('https://search.yahoo.co.jp/realtime')
r.encoding = r.apparent_encoding

# 対象である表をスクレイピング。
soup = BeautifulSoup(r.text, 'html.parser')
rows = soup.findAll('section', class_='Trend_container__2vkJ-')
trend = rows.findAll('li')
art = trend.findAll('article')
print(art)
