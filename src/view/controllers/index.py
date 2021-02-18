from flask import Blueprint, render_template
from common.models.cloud import Cloud

index_page = Blueprint("index_page", __name__)


@index_page.route("/")
def index():

    result = Cloud.query.all()
    # print(result)

    # return render_template("test.html", **context)
    return render_template("test.html")
