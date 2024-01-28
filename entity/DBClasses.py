from service.DBSessionStarter import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey
from service.DBSessionStarter import db_session



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

    id = Column(Integer, primary_key=True, autoincrement=True)
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

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    description = Column(String(1024))
    price = Column(Integer)
    category = Column(Integer, ForeignKey('item_category.id'))
    quantity = Column(Integer)
    status = Column(Integer, ForeignKey('item_status.id'))

    def __init__(self, id, name, description, price, category, quantity, status):
        self.id = id
        self.name = name
        self.description = description
        self.price = int(price)
        self.category = category
        self.quantity = int(quantity)
        self.status = status


class ItemStatus(Base):
    __tablename__ = 'item_status'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))

    def __init__(self, id, name):
        self.id = id
        self.name = name


class ItemCategory(Base):
    __tablename__ = 'item_category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64))

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, autoincrement=True)
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

    id = Column(Integer, primary_key=True, autoincrement=True)
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

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Integer)
    user_login = Column(String(32), ForeignKey('user.login'))
    item_id = Column(Integer, ForeignKey('item.id'))

    def __init__(self, name, user_login, item_id):
        self.name = name
        self.user_login = user_login
        self.item_id = item_id

class CompareList(Base):
    __tablename__ = 'compare_list'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_login = Column(String(32), ForeignKey('user.login'))
    item_id = Column(Integer, ForeignKey('item.id'))

    def __init__(self, id, user_login, item_id):
        self.id = id
        self.user_login = user_login
        self.item_id = item_id





# status_out_of_stock = ItemStatus(1, "out of stock")
# status_available = ItemStatus(2, "available")
# status_unavailable = ItemStatus(3, "unavailable")
# status_waiting = ItemStatus(4, "waiting")
#
# category_laptop = ItemCategory(1, "laptop")
# category_tablet = ItemCategory(2, "tablet")
# category_phone = ItemCategory(3, "phone")
# category_tv = ItemCategory(4, "tv")

# item1 = Item(1, "Galaxy S24 Ultra", "latest Samsung flagship", 58_000, category_phone.id, 5, status_waiting.id)
# item2 = Item(2, "Mac Book Pro 16 2024", "latest Mac Book Pro", 150_000, category_laptop.id, 2, status_available.id)
#
# db_session.add(status_out_of_stock)
# db_session.add(status_available)
# db_session.add(status_unavailable)
# db_session.add(status_waiting)
#
# db_session.add(category_laptop)
# db_session.add(category_tablet)
# db_session.add(category_laptop)
# db_session.add(category_phone)
# db_session.add(category_tv)

# db_session.add(item1)
# db_session.add(item2)
#
# db_session.commit()

# Base.metadata.create_all(engine)
