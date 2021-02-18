from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from io import BytesIO
from PIL import Image
import os

# 実行ディレクトリを上げる
# import sys
# sys.path.append("../")
from modules import meteorological_img
from common.models.cloud import Cloud

# セッション変数の取得
from application import session


class Map_update:
    def __init__(self) -> None:
        self.scheduler = BlockingScheduler()
        pass

    def sche_set(self, set_time):
        self.scheduler.add_job(self.insert_img, "interval", seconds=set_time)

    def sche_start(self):
        self.scheduler.start()

    def sche_shutdown(self):
        self.scheduler.shutdown()

    def sche_pause(self):
        self.scheduler.pause()

    def img_io(self, path):
        image_data = BytesIO()
        im = Image.open(path)
        im.save(image_data, "png")
        image_data.seek(0)
        image_file = image_data.read()
        return image_file

    def insert_img(self):
        path = meteorological_img.main()
        image_file = self.img_io(path)
        now = datetime.now()
        cloud = Cloud()
        cloud.img_name = os.path.basename(path)
        cloud.img = image_file
        cloud.created_at = now
        cloud.tag = "synthetic"
        cloud.zoom_level = 2
        session.add(cloud)
        session.commit()
        print("insert")


def main():
    print("schedule start")
    map = Map_update()
    map.sche_set(10)
    map.sche_start()


if __name__ == "__main__":
    main()
