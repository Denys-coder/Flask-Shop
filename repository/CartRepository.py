from entity import DBClasses
from service.DBSessionStarter import db_session


def get_cart_by_user_login(user_login):
    cart = db_session.query(DBClasses.Cart).filter_by(user_login=user_login).all()
    return cart


def save_cart(cart):
    db_session.add(cart)


def delete_cart_by_user_login(user_login):
    carts_to_delete = db_session.query(DBClasses.Cart).filter_by(user_login=user_login)
    for cart in carts_to_delete:
        db_session.delete(cart)


def delete_cart_by_user_login_and_item_id(user_login, item_id):
    carts_to_delete = db_session.query(DBClasses.Cart).filter_by(user_login=user_login, item_id=item_id)
    for cart in carts_to_delete:
        db_session.delete(cart)


def get_cart_items_and_quantities_by_user_login(user_login):
    query = (db_session.query(DBClasses.Item, DBClasses.Cart.quantity)
             .join(DBClasses.Cart, DBClasses.Item.id == DBClasses.Cart.item_id)
             .filter(DBClasses.Cart.user_login == user_login))
    cart = query.all()
    return cart
