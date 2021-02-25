import requests
from datetime import datetime, timedelta
import os
import cv2


def get_map_img(
    tag, line_range_min, line_range_max, column_range_min, column_range_max
):
    if tag == "map":
        base_url = "https://cyberjapandata.gsi.go.jp/xyz/pale/"
    elif tag == "cloud":
        base_url = "https://www.jma.go.jp/bosai/jmatile/data/nowc/20210225111500/none/20210225111500/surf/hrpns/"
    for column in range(column_range_min, column_range_max + 1):
        for line in range(line_range_min, line_range_max + 1):
            url = (base_url + "{}/{}/{}.png").format(
                zoom,
                column,
                line,
            )
            output_path = ("./img/{}/{}/{}_{}.png").format(tag, zoom, column, line)
            dir = os.path.dirname(output_path) + "/"
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            save_img(url, output_path)

    img_connect(
        tag, dir, line_range_min, line_range_max, column_range_min, column_range_max
    )

    sye(zoom)


# 指定したURLの画像を保存
def save_img(url, output_path):
    req = requests.get(url)
    with open(output_path, "wb") as w:
        w.write(req.content)
        w.close()


# 画像結合
def img_connect(
    tag, path, line_range_min, line_range_max, column_range_min, column_range_max
):
    flag = False
    if tag == "cloud":
        flag = True
    v_list = []
    for i in range(column_range_min, column_range_max + 1):
        file = path + str(i) + "_" + str(line_range_min) + ".png"
        if flag:
            base_img = cv2.imread(file, -1)
        else:
            base_img = cv2.imread(file)
        for j in range(line_range_min + 1, line_range_max + 1):
            file = path + str(i) + "_" + str(j) + ".png"
            if flag:
                im = cv2.imread(file, -1)
            else:
                im = cv2.imread(file)
            base_img = cv2.vconcat([base_img, im])
        v_list.append(base_img)
    base_img = v_list[0]
    for v in v_list[1:]:
        base_img = cv2.hconcat([base_img, v])

    cv2.imwrite(path + "result.png", base_img)


# 透過画像の合成
def sye(zoom):
    cartopy = False
    base_path = "./img"
    if cartopy:
        map = "cartopy/"
    else:
        map = "map/"
    map_path = ("{}/{}/{}/result.png").format(base_path, "map", zoom)
    cloud_path = ("{}/{}/{}/result.png").format(base_path, "cloud", zoom)
    map = cv2.imread(map_path)
    # height, width = map.shape[0], map.shape[1]
    # map = cv2.resize(map, (512, 512))
    cloud = cv2.imread(cloud_path, -1)
    # 貼り付け先座標の設定。とりあえず左上に
    x1, y1, x2, y2 = 0, 0, cloud.shape[1], cloud.shape[0]

    map[y1:y2, x1:x2] = map[y1:y2, x1:x2] * (1 - cloud[:, :, 3:] / 255) + cloud[
        :, :, :3
    ] * (cloud[:, :, 3:] / 255)
    output_path = ("{}/{}/{}/result.png").format(base_path, "sye", zoom)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cv2.imwrite(output_path, map)
    return output_path


if __name__ == "__main__":
    zoom = 5
    # /column_line/
    column_range_min = 27
    column_range_max = 29
    line_range_min = 11
    line_range_max = 14
    tag = "map"
    get_map_img(tag, line_range_min, line_range_max, column_range_min, column_range_max)

    pass