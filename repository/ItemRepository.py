from entity.Item import Item
from service.DBSessionStarter import db_session


def get_item_by_id(id):
    items = db_session.query(Item).filter(Item.id == id).first()
    return items


def get_items_by_ids(ids):
    items = db_session.query(Item).filter(Item.id.in_(ids)).all()
    return items


def get_all_items():
    items = db_session.query(Item).all()
    return items
