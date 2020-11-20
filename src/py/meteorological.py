import requests
from bs4 import BeautifulSoup #ダウンロードしてなかったらpipでできるからやってね。
import csv
import json


#取ったデータをfloat型に変えるやつ。(データが取れなかったとき気象庁は"/"を埋め込んでいるから0に変える)
def str2float(str):
    try:
        return float(str)
    except:
        return 0.0


class Meteorological:
    def __init__(self, year, place):
        self.year = year
        self.place = place
        self.url = ''


    def get_config(self):
        fname = "../../config/meteorological.json"
        with open(fname, "r") as f:
            cfg = json.load(f)

        index = cfg['place_name'].index(self.place)
        a = cfg['place_codeA'][index]
        b = cfg['place_codeB'][index]
        self.url = cfg['url']

        return a, b


    def csv_out(self, data):
        #都市ごとにデータをファイルを新しく生成して書き出す。(csvファイル形式。名前は都市名)
        with open(self.place + '.csv', 'w') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows(data)


    def all_data(self):
        all_list = [['年月日', '陸の平均気圧(hPa)', '海の平均気圧(hPa)', '降水量(mm)', '平均気温(℃)', '平均湿度(%)', '平均風速(m/s)', '日照時間(h)']]
        place_codeA, place_codeB = self.get_config()

        print(self.place)
        print(self.year)

        for month in range(1,13):
            #2つの都市コードと年と月を当てはめる。
            r = requests.get(self.url%(place_codeA, place_codeB, self.year, month))
            r.encoding = r.apparent_encoding

            # 対象である表をスクレイピング。
            soup = BeautifulSoup(r.text)
            rows = soup.findAll('tr',class_='mtx') #タグ指定してclass名を指定するみたい。

            # 表の最初の1~4行目はカラム情報なのでスライスする。(indexだから初めは0だよ)
            # 【追記】2020/3/11 申し訳ございません。間違えてました。
            rows = rows[4:]

            # 1日〜最終日までの１行を網羅し、取得します。
            for row in rows:
                data = row.findAll('td')

                #１行の中には様々なデータがあるので全部取り出す。
                # ★ポイント
                rowData = [] #初期化
                rowData.append(str(self.year) + "/" + str(month) + "/" + str(data[0].string))
                rowData.append(str2float(data[1].string))
                rowData.append(str2float(data[2].string))
                rowData.append(str2float(data[3].string))
                rowData.append(str2float(data[6].string))
                rowData.append(str2float(data[9].string))
                rowData.append(str2float(data[11].string))
                rowData.append(str2float(data[16].string))

                #次の行にデータを追加
                all_list.append(rowData)

        self.csv_out(all_list)

        print('end')



if __name__ == "__main__":
    m = Meteorological(2019, '高知')
    m.all_data()