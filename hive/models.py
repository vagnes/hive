from hive import db
from datetime import datetime


class Message(db.Model):
    __tablename__ = "Messages"

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)


db.create_all()
