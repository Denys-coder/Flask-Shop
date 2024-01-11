from service.DBSessionStarter import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey


class Cart(Base):
    __tablename__ = 'cart'

    user_login = Column(String(64), ForeignKey('user.login'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)
    quantity = Column(Integer)

    def __init__(self, user_login, item_id, quantity):
        self.user_login = user_login
        self.item_id = item_id
        self.quantity = quantity


Base.metadata.create_all(engine)
