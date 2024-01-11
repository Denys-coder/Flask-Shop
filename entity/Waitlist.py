from service.DBSessionStarter import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey


class Waitlist(Base):
    __tablename__ = ''

    user_login = Column(String(64), ForeignKey('user.login'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)

    def __init__(self, user_login, item_id):
        self.user_login = user_login
        self.item_id = item_id


Base.metadata.create_all(engine)
