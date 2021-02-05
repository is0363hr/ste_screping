from datetime import datetime

# import BackgroundScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask


# define the job
def hello_job():
    print("Hello Job! The time is: %s" % datetime.now())


def create_app():
    app = Flask(__name__)

    # init BackgroundScheduler job
    scheduler = BackgroundScheduler()
    # in your case you could change seconds to hours
    scheduler.add_job(hello_job, trigger="interval", seconds=3)
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