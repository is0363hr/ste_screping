import requests
from datetime import datetime
import cv2
import numpy as np


class meteorogical_img:
    def __init__(self, base_path, zoom):
        self.base_path = base_path
        self.tag = ""
        self.zoom = zoom
        self.output_path = ""
        pass

    def get_image(self):
        self.output_path = self.base_path + self.tag + "/" + self.zoom + "/"
        if self.tag == "map":
            for i in range(1, 3):
                for j in range(1, 3):
                    num = str(i) + "_" + str(j)
                    print(num)
                    # 地図画像のURL
                    url = (
                        "https://www.jma.go.jp/jp/commonmesh/map_tile/MAP_COLOR/none/anal/"
                        + self.zoom
                        + "/"
                        + num
                        + ".png"
                    )
                    self.save_img(url, num)

        elif self.tag == "cloud":

            time = list(datetime.now().strftime("%Y%m%d%H%M"))
            hour = time[-4:-2]
            m = int(time[-1])
            tem = 0
            for h in hour:
                tem += int(h)
                time[-4:-2] = "0" + str(tem)
            if m > 0:
                time[-1] = "0"

            time = "".join(time)
            # time = "202101060955"

            for i in range(1, 3):
                for j in range(1, 3):
                    num = str(i) + "_" + str(j)
                    print(num)
                    # 雲画像のURL
                    url = (
                        "https://www.jma.go.jp/jp/highresorad/highresorad_tile/HRKSNC/"
                        + time
                        + "/"
                        + time
                        + "/"
                        + self.zoom
                        + "/"
                        + num
                        + ".png"
                    )
                    self.save_img(url, num)
        else:
            print("error")

    def save_img(self, url, num):
        req = requests.get(url)
        with open(self.output_path + num + ".png", "wb") as w:
            w.write(req.content)
            w.close()

    # 縦結合
    def map_img_v(self, path):
        flag = True

        for i in range(1, 3):
            for j in range(1, 3):
                file = path + str(i) + "_" + str(j) + ".png"
                if flag:
                    im = cv2.imread(file)
                    flag = False
                else:
                    tmp = cv2.imread(file)
                    im = cv2.vconcat([im, tmp])

            cv2.imwrite(path + str(i) + ".png", im)
            flag = True

    # 横結合
    def map_img_h(self, path):
        flag = True
        for i in range(1, 3):
            file = path + str(i) + ".png"
            if flag:
                im = cv2.imread(file)
                flag = False
            else:
                tmp = cv2.imread(file)
                im = cv2.hconcat([im, tmp])

        cv2.imwrite(path + "result.png", im)

    # 縦結合
    def cloud_img_v(self, path):
        flag = True

        for i in range(1, 3):
            for j in range(1, 3):
                file = path + str(i) + "_" + str(j) + ".png"
                if flag:
                    im = cv2.imread(file, -1)
                    flag = False
                else:
                    tmp = cv2.imread(file, -1)
                    im = cv2.vconcat([im, tmp])

            cv2.imwrite(path + str(i) + ".png", im)
            flag = True

    # 横結合
    def cloud_img_h(self, path):
        flag = True
        for i in range(1, 3):
            file = path + str(i) + ".png"
            if flag:
                im = cv2.imread(file, -1)
                flag = False
            else:
                tmp = cv2.imread(file, -1)
                im = cv2.hconcat([im, tmp])

        cv2.imwrite(path + "result.png", im)

    # 透過画像の合成
    def sye(self):
        map_path = self.base_path + "map/" + self.zoom + "/result.png"
        cloud_path = self.base_path + "cloud/" + self.zoom + "/result.png"
        map = cv2.imread(map_path)
        # height, width = map.shape[0], map.shape[1]
        # map = cv2.resize(map, (int(width * 2.0), int(height * 2.0)))
        cloud = cv2.imread(cloud_path, -1)
        # 貼り付け先座標の設定。とりあえず左上に
        x1, y1, x2, y2 = 0, 0, cloud.shape[1], cloud.shape[0]

        map[y1:y2, x1:x2] = map[y1:y2, x1:x2] * (1 - cloud[:, :, 3:] / 255) + cloud[
            :, :, :3
        ] * (cloud[:, :, 3:] / 255)
        output_path = self.base_path + "sye/" + self.zoom + "/result.png"
        cv2.imwrite(output_path, map)
        return output_path

    # 透過画像の合成
    def py_sye(output_path):
        map = cv2.imread("result/mini/py_mini_zoom2.png")
        map = cv2.resize(map, (512, 512))
        # height, width = map.shape[0], map.shape[1]
        # map = cv2.resize(map, (int(width * 2.0), int(height * 2.0)))
        cloud = cv2.imread("result/mini/cloud_mini_zoom2.png", -1)
        # 貼り付け先座標の設定。とりあえず左上に
        x1, y1, x2, y2 = 0, 0, cloud.shape[1], cloud.shape[0]

        map[y1:y2, x1:x2] = map[y1:y2, x1:x2] * (1 - cloud[:, :, 3:] / 255) + cloud[
            :, :, :3
        ] * (cloud[:, :, 3:] / 255)
        cv2.imwrite(output_path + "py_synthe_mini_zoom2.png", map)

    def map_create(self):
        self.tag = "map"
        self.get_image()
        print(self.output_path)
        self.map_img_v(self.output_path)
        self.map_img_h(self.output_path)
        pass

    def cloud_create(self):
        self.tag = "cloud"
        self.get_image()
        print(self.output_path)
        self.cloud_img_v(self.output_path)
        self.cloud_img_h(self.output_path)
        pass


if __name__ == "__main__":
    mete = meteorogical_img("../assets/", "zoom2")
    mete.map_create()
    mete.cloud_create()
    mete.sye()
