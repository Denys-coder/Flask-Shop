from service.DBSessionStarter import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    user_login = Column(String(64), ForeignKey('user.login'))
    address = Column(String(128))
    total_price = Column(Integer)
    status = Column(Integer)

    def __init__(self, user_login, address, total_price, status):
        self.user_login = user_login
        self.address = address
        self.total_price = int(total_price)
        self.status = status


Base.metadata.create_all(engine)
