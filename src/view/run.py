from flask import Flask, render_template
from common.models.cloud import Cloud
from application import session

# 実行ディレクトリを上げる
# sys.path.append("../")

app = Flask(__name__)


@app.route("/")
def view():
    # Userテーブルのnameカラムをすべて取得
    clouds = session.query(Cloud).all()
    for cloud in clouds:
        print(cloud.img_name)
    return render_template("test.html")


@app.route("/good")
def good():
    name = "Good"
    return name


## おまじない
if __name__ == "__main__":
    app.run(debug=True)