from sqlalchemy.sql import func
from hive.models import Message
from hive import db


class Query(object):

    @staticmethod
    def add_msg(message):
        message = Message(message=message)
        db.session.add(message)
        db.session.commit()

    @staticmethod
    def random_row():
        row = Message.query.order_by(func.random()).first()
        return {"id": row.id,
                "message": row.message,
                "likes": row.likes,
                "reports": row.reports
                }

    @staticmethod
    def add_like(msg_id):
        row = Message.query.filter_by(id=msg_id).one()
        row.likes += 1
        db.session.add(row)
        db.session.commit()

    @staticmethod
    def add_report(msg_id):
        row = Message.query.filter_by(id=msg_id).one()
        row.reports += 1
        db.session.add(row)
        db.session.commit()

    @staticmethod
    def get_stats(msg_id):
        row = Message.query.filter_by(id=msg_id).one()
        return {"likes": row.likes,
                "reports": row.reports
                }
