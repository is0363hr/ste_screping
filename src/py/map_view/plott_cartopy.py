# -*- coding: utf-8 -*-

# 地図表示、１時間ごとに観測値をplot

import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

import math
from decimal import Decimal, ROUND_HALF_UP


def dms2deg(hour, minutes):
    # 度分秒から度への変換
    deg = []
    for h, m in zip(hour, minutes):
        deg.append(
            Decimal(str(h + (m / 60))).quantize(
                Decimal("0.0001"), rounding=ROUND_HALF_UP
            )
        )
    return deg


def loaddata(place):
    data = pd.read_csv("../../../data/ame_master.csv", encoding="cp932")
    d = data.query('都府県振興局 == "{}"'.format(place))
    name = d["観測所名"]
    id = d["観測所番号"]
    tlats = d[["緯度(度)", "緯度(分)"]]
    lats = dms2deg(tlats["緯度(度)"], tlats["緯度(分)"])
    tlons = d[["経度(度)", "経度(分)"]]
    lons = dms2deg(tlons["経度(度)"], tlons["経度(分)"])
    return {"name": name, "id": id, "lats": lats, "lons": lons}


def plot_(place, lat, lon):

    fig = plt.figure(figsize=(5, 5))
    plt.rcParams["font.size"] = 18

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([132, 135, 32, 35], crs=ccrs.PlateCarree())
    ax.set_title(place)

    ax.coastlines(resolution="10m")  # 海岸線の解像度を10 mにする
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    ax.stock_img()  # 地図の色を塗る

    # データのプロット
    ax.scatter(lon, lat, color="r", marker="o", s=5)

    plt.show()


def plot_test():

    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
    ax.set_extent([119.3229, 150.6771, 20.5, 47.5], crs=ccrs.PlateCarree())

    ax.coastlines(resolution="10m")  # 海岸線の解像度を10 mにする
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    ax.stock_img()  # 地図の色を塗る

    fig.savefig(
        "py_mini_zoom2.png",
        dpi=300,
        transparent=True,
        bbox_inches="tight",
        pad_inches=0,
    )
    # plt.show()


if __name__ == "__main__":
    # data = loaddata("高知")
    # lat = np.array(data["lats"])
    # lon = np.array(data["lons"])
    # plot_("高知", lat, lon)
    plot_test()
