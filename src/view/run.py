from flask import Flask, render_template


# 実行ディレクトリを上げる
# sys.path.append("../")

app = Flask(__name__)


@app.route("/")
def view():
    return render_template("test.html")


@app.route("/good")
def good():
    name = "Good"
    return name


## おまじない
if __name__ == "__main__":
    app.run(debug=True)