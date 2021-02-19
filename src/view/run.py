from flask import Flask, render_template
from sqlalchemy.sql import func

from common.models.cloud import Cloud
from application import session


app = Flask(__name__)


@app.route("/")
def view():
    context = {}
    max_id = session.query(func.max(Cloud.id)).scalar()
    cloud_img_path = session.query(Cloud.img_path).filter(Cloud.id == max_id).scalar()

    # context["cloud_img_path"] = cloud_img_path.split("./static/")[1]
    context["cloud_img_path"] = cloud_img_path
    print(context["cloud_img_path"])
    return render_template("test.html", **context)


@app.route("/good")
def good():
    name = "Good"
    return name


## おまじない
if __name__ == "__main__":
    app.run(debug=True)