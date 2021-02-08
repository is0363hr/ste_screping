from apscheduler.schedulers.blocking import BlockingScheduler

# 実行ディレクトリを上げる
# import sys
# sys.path.append("../")
# from modules import meteorological_img
import meteorological_img


class Map_update:
    def __init__(self) -> None:
        self.scheduler = BlockingScheduler()
        pass

    def map_update_job(self):
        # print("Hello Job! The time is: %s" % datetime.now())
        meteorological_img.main()
        print("update")

    def sche_set(self, set_time):
        self.scheduler.add_job(self.map_update_job, "interval", minutes=set_time)

    def sche_start(self):
        self.scheduler.start()

    def sche_shutdown(self):
        self.scheduler.shutdown()

    def sche_pause(self):
        self.scheduler.pause()


def main():
    map = Map_update()
    map.sche_set(3)
    map.sche_start()