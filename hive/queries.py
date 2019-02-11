from sqlalchemy.sql import func
from hive.models import Message


class Query(object):

    @staticmethod
    def random_message():
        row = Message.query.order_by(func.random()).first()
        return row.message
