import requests
from datetime import datetime


def save_img(url, num):
    output_path = 'cloud_img/zoom5/'
    req = requests.get(url)
    with open(output_path + num+'.png', "wb") as w:
        w.write(req.content)
        w.close()


def get_image():

    time = list(datetime.now().strftime("%Y%m%d%H%M"))
    hour = time[-4:-2]
    m = int(time[-1])
    tem = 0
    for h in hour:
        tem += int(h)
        time[-4:-2] = '0'+str(tem)
    if m > 0:
        time[-1] = '0'
    # time = ''.join(time)
    time = '202101060955'

    for i in range(26, 36):
        for j in range(26, 34):
            num = str(i)+'_'+str(j)
            print(num)
            # 雲画像のURL
            url = 'https://www.jma.go.jp/jp/highresorad/highresorad_tile/HRKSNC/'+time+'/'+time+'/zoom6/'+num+'.png'
            # 地図画像のURL
            # url = 'https://www.jma.go.jp/jp/commonmesh/map_tile/MAP_COLOR/none/anal/zoom5/'+num+'.png'
            save_img(url, num)



get_image()

