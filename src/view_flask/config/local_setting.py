# ローカル環境
from config.base_setting import *

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_URI = "mysql://{user}:{password}@{host}:{port}/scraping".format(
    **{
        "user": "root",
        "password": "InfoNetworking",
        "host": "localhost",
        "port": "3306",
    }
)
SECRET_KEY = "678910"
