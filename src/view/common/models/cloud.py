from application import Base
from sqlalchemy import Column, Integer, String, DateTime, BLOB


class Cloud(Base):
    __tablename__ = "cloud_data"

    id = Column(Integer, primary_key=True, autoincrement=True)
    img_name = Column(String(100), nullable=False)
    img_path = Column(String(50), nullable=False)
    created_at = Column(DateTime, nullable=False)
    tag = Column(String(50), nullable=False)
    zoom_level = Column(Integer, nullable=False)