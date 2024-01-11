from service.DBSessionStarter import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey


class OrderItems(Base):
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)

    def __init__(self, order_id, item_id):
        self.order_id = int(order_id)
        self.item_id = int(item_id)


Base.metadata.create_all(engine)
