from sqlalchemy.sql.functions import user

from entity.DBClasses import Item, ItemCategory, ItemStatus, CompareList, User
from repository import UserRepository
from service.DBSessionStarter import db_session


def get_comparable_item_categories_by_user(user):
    database_entries = (db_session.query(ItemCategory.name)
        .join(Item, ItemCategory.id == Item.category)
        .join(CompareList, Item.id == CompareList.item_id)
        .join(User, CompareList.user_login == User.login)
        .filter(User.login == user.login).all())
    item_categories = [name[0] for name in database_entries]
    return item_categories


def add_comparable_item(item_id, user_login):
    compare_list = CompareList(item_id, user_login)
    db_session.add(compare_list)
    db_session.commit()


def get_comparable_items_by_category_by_user(item_category, user_login):
    data = (
        db_session.query(Item)
        .join(CompareList, Item.id == CompareList.item_id)
        .join(User, CompareList.user_login == User.login)
        .join(ItemCategory, Item.category == ItemCategory.id)
        .filter(ItemCategory.name == item_category)
        .filter(User.login == user_login)
    ).all()
    return data









