from service.DBSessionStarter import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey


class Wishlist(Base):
    __tablename__ = 'wishlist'

    id = Column(Integer, primary_key=True)
    name = Column(Integer)
    user_login = Column(String(32), ForeignKey('user.login'))
    item_id = Column(Integer, ForeignKey('item.id'))

    def __init__(self, name, user_login, item_id):
        self.name = name
        self.user_login = user_login
        self.item_id = item_id


Base.metadata.create_all(engine)
