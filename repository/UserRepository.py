from entity.DBClasses import User
from service.DBSessionStarter import db_session


def save_new_user(user):
    db_session.add(user)
    db_session.commit()


def get_user_by_login(login):
    return db_session.query(User).get(login)


def update_user(user):
    user_in_db = get_user_by_login(user.login)
    user_in_db.name = user.name
    user_in_db.surname = user.surname
    user_in_db.password = user.password
    user_in_db.phone_number = user.phone_number
    user_in_db.email = user.email
