from service.DBSessionStarter import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey


class OrderStatus(Base):
    __tablename__ = 'order_status'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    def __init__(self, id, name):
        self.id = id
        self.name = name


Base.metadata.create_all(engine)
