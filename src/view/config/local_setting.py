# ローカル環境
from config.base_setting import *

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "mysql://{user}:{password}@{host}:{port}/flask".format(
    **{"user": "root", "password": "InfoNetworking", "host": "localhost", "port": "82"}
)
SECRET_KEY = "678910"
