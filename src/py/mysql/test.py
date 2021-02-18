# -*- coding: utf-8 -*-
from sqlalchemy.sql import func


# セッション変数の取得
from setting import session
from cloud import *


max_id = session.query(func.max(Cloud.id)).scalar()
print(max_id)
cloud_img = session.query(Cloud.img).filter(Cloud.id == max_id).scalar()
print(cloud_img)