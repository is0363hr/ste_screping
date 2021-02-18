# -*- coding: utf-8 -*-
import sys

from setting import Base
from setting import ENGINE

from sqlalchemy import Column, Integer, String, DateTime, BLOB


class Cloud(Base):
    __tablename__ = "cloud_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    img_name = Column(String(100), nullable=False)
    img_path = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    tag = Column(String(50), nullable=False)
    zoom_level = Column(Integer, nullable=False)


def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main(sys.argv)