# -*- coding: utf-8 -*-
from sqlalchemy.sql import func
from pprint import pprint

from common.models.cloud import Cloud
from application import session


class DBFunc:
    def __init__(self) -> None:
        pass

    # 最新の画像パスを取得
    def get_latest_img_path(self):
        max_id = session.query(func.max(Cloud.id)).scalar()
        cloud_img_path = (
            session.query(Cloud.img_path).filter(Cloud.id == max_id).scalar()
        )
        return cloud_img_path

    def get_all(self):
        # Userテーブルのnameカラムをすべて取得
        clouds = session.query(Cloud).all()
        data = []
        for cloud in clouds:
            data.append(
                {
                    "id": cloud.id,
                    "img_name": cloud.img_name,
                    "img_path": cloud.img_path,
                    "created_at": cloud.created_at,
                    "tag": cloud.tag,
                    "zoom_level": cloud.zoom_level,
                }
            )
        return data


def main():
    db = db_func()
    pprint(db.get_all())
    pass


if __name__ == "__main__":
    main()