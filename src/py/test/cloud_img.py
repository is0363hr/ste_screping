import requests
from datetime import datetime


def save_img(url, num):
    req = requests.get(url)
    with open(num+'rain.png', "wb") as w:
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
    time = ''.join(time)

    for i in range(4):
        for j in range(4):
            num = str(i)+'_'+str(j)
            url = 'https://www.jma.go.jp/jp/highresorad/highresorad_tile/HRKSNC/'+time+'/'+time+'/zoom2/'+num+'.png'
            # 地図の画像
            # url = 'https://www.jma.go.jp/jp/highresorad//commonmesh/map_tile/MAP_COLOR/none/anal/zoom2/'+num+'.png'
            save_img(url, num)



get_image()

