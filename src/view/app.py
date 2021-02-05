from datetime import datetime

# import BackgroundScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask

import os
import sys

# 実行ディレクトリを上げる
sys.path.append("../")

from modules import meteorological_img


# define the job
def map_update_job():
    # print("Hello Job! The time is: %s" % datetime.now())
    meteorological_img.main()


def create_app():
    app = Flask(__name__)

    # init BackgroundScheduler job
    scheduler = BackgroundScheduler()
    # in your case you could change seconds to hours
    # TODO
    scheduler.add_job(map_update_job, trigger="interval", seconds=10)
    scheduler.start()

    try:
        # To keep the main thread alive
        return app
    except:
        # shutdown if app occurs except
        scheduler.shutdown()


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)