from flask import Blueprint, render_template
from sqlalchemy.sql import func

from modules.db_controller import DBFunc

index_page = Blueprint("index_page", __name__)
db_func = DBFunc()


@index_page.route("/")
def index():
    context = {}
    cloud_img_path = db_func.get_latest_img_path()
    cloud_img_time = db_func.get_latest_img_time()
    print(type(cloud_img_time))

    # context["cloud_img_path"] = cloud_img_path.split("./static/")[1]
    context["cloud_img_path"] = cloud_img_path
    context["cloud_img_time"] = cloud_img_time

    return render_template("test.html", **context)
