import requests
from bs4 import BeautifulSoup
# Webページを取得して解析する

load_url = "https://www.jma.go.jp/bosai/#pattern=forecast&area_type=class20s&area_code=2520600"
# html = requests.get(load_url)
from urllib.request import urlopen
html = urlopen(load_url)
data = html.read()
html = data.decode('utf-8')
# soup = BeautifulSoup(html, "html.parser")
soup = BeautifulSoup(html, "html5lib")

# rain = soup.find(class_="forecast-table")
soup = soup.find(id="bosaitop-main")
soup = soup.find(id="bosaitop-bosaidata")
soup = soup.find(id="bosaitop-forecast_table_window")


# HTML全体を表示する
print(soup)