from service.DBSessionStarter import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    description = Column(String(1024))
    price = Column(Integer)
    category = Column(Integer, ForeignKey('item_category.id'))
    quantity = Column(Integer)

    def __init__(self, id, name, description, price, category, quantity):
        self.id = id
        self.name = name
        self.description = description
        self.price = int(price)
        self.category = category
        self.quantity = int(quantity)


Base.metadata.create_all(engine)
