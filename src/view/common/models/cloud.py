from application import db


class Cloud(db.Model):
    __tablename__ = "cloud_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img_name = db.Column(db.String(100), nullable=False)
    img = db.Column(db.BLOB, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    tag = db.Column(db.String(50), nullable=False)
    zoom_level = db.Column(db.Integer, nullable=False)