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


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'))
    text = Column(String(1024))
    rating = Column(Integer)
    user_login = Column(String(32), ForeignKey('user.login'))

    def __init__(self, id, item_id, text, rating, user_login):
        self.id = id
        self.item_id = item_id
        self.text = text
        self.rating = rating
        self.user_login = user_login


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


class ItemCategory(Base):
    __tablename__ = 'item_category'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    def __init__(self, id, name):
        self.id = id
        self.name = name


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


class OrderItems(Base):
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)

    def __init__(self, order_id, item_id):
        self.order_id = int(order_id)
        self.item_id = int(item_id)


class OrderStatus(Base):
    __tablename__ = 'order_status'

    id = Column(Integer, primary_key=True)
    name = Column(String(64))

    def __init__(self, id, name):
        self.id = id
        self.name = name


class User(Base):
    __tablename__ = 'user'

    name = Column(String(64))
    surname = Column(String(64))
    password = Column(String(32))
    phone_number = Column(String(32))
    login = Column(String(32), primary_key=True)
    email = Column(String(64))

    def __init__(self, name, surname, password, phone_number, login, email):
        self.name = name
        self.surname = surname
        self.password = password
        self.phone_number = phone_number
        self.login = login
        self.email = email


class Waitlist(Base):
    __tablename__ = 'waitlist'

    user_login = Column(String(64), ForeignKey('user.login'), primary_key=True)
    item_id = Column(Integer, ForeignKey('item.id'), primary_key=True)

    def __init__(self, user_login, item_id):
        self.user_login = user_login
        self.item_id = item_id


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


# Base.metadata.create_all(engine)
