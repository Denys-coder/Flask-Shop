from entity.DBClasses import Item, ItemCategory, ItemStatus
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


def get_filtered_items(name, status, category, min_price, max_price):
    query = db_session.query(Item).join(ItemCategory, Item.category == ItemCategory.id).join(ItemStatus,
                                                                                             Item.status == ItemStatus.id)
    if name is not None and name != "":
        query = query.filter(Item.name.like(f"%{name}%"))

    if status is not None and status != "":
        query = query.filter(ItemStatus.name == status)

    if category is not None and category != "":
        query = query.filter(ItemCategory.name == category)

    if min_price is not None and min_price != "":
        query = query.filter(Item.price > min_price)

    if max_price is not None and max_price != "":
        query = query.filter(Item.price < max_price)

    return query.all()
