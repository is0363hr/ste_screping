# -*- coding: utf-8 -*-

import cv2
import numpy as np
from PIL import Image


# 縦結合
def map_img_v(input_path, output_path):
    flag = True

    for i in range(1, 3):
        for j in range(1, 3):
            file = input_path + str(i) + "_" + str(j) + "map" + ".png"
            if flag:
                im = cv2.imread(file)
                flag = False
            else:
                tmp = cv2.imread(file)
                im = cv2.vconcat([im, tmp])

        cv2.imwrite(output_path + "mini_" + str(i) + ".png", im)
        flag = True


# 横結合
def map_img_h(input_path, output_path):
    flag = True
    for i in range(1, 3):
        file = input_path + "mini_" + str(i) + ".png"
        if flag:
            im = cv2.imread(file)
            flag = False
        else:
            tmp = cv2.imread(file)
            im = cv2.hconcat([im, tmp])

    cv2.imwrite(output_path + "map_mini_zoom2.png", im)


# 縦結合
def cloud_img_v(input_path, output_path):
    flag = True

    for i in range(1, 3):
        for j in range(1, 3):
            file = input_path + str(i) + "_" + str(j) + "rain.png"
            if flag:
                im = cv2.imread(file, -1)
                flag = False
            else:
                tmp = cv2.imread(file, -1)
                im = cv2.vconcat([im, tmp])

        cv2.imwrite(output_path + str(i) + "rain.png", im)
        flag = True


# 横結合
def cloud_img_h(input_path, output_path):
    flag = True
    for i in range(1, 3):
        file = input_path + str(i) + "rain.png"
        if flag:
            im = cv2.imread(file, -1)
            flag = False
        else:
            tmp = cv2.imread(file, -1)
            im = cv2.hconcat([im, tmp])

    cv2.imwrite(output_path + "cloud_mini_zoom2.png", im)


# 透過画像の合成
def sye(output_path):
    map = cv2.imread("result/mini/map_mini_zoom2.png")
    # height, width = map.shape[0], map.shape[1]
    # map = cv2.resize(map, (int(width * 2.0), int(height * 2.0)))
    cloud = cv2.imread("result/mini/cloud_mini_zoom2.png", -1)
    # 貼り付け先座標の設定。とりあえず左上に
    x1, y1, x2, y2 = 0, 0, cloud.shape[1], cloud.shape[0]

    map[y1:y2, x1:x2] = map[y1:y2, x1:x2] * (1 - cloud[:, :, 3:] / 255) + cloud[
        :, :, :3
    ] * (cloud[:, :, 3:] / 255)

    cv2.imwrite(output_path + "synthe_mini_zoom2.png", map)


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


def main():
    py_sye("result/mini/")
    # img_v('cloud_img/zoom5/', 'result/')
    # img_h('result/', 'result/')
    # map_img_v("map_img/zoom2/", "result/mini/")
    # map_img_h("result/mini/", "result/mini/")
    # cloud_img_v("cloud_img/zoom2/", "result/mini/")
    # cloud_img_h("result/mini/", "result/mini/")


if __name__ == "__main__":
    # img_v('cloud_img/', 'result/')
    # img_h('result/', 'result/')
    main()
