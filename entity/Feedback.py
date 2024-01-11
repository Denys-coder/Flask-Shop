from service.DBSessionStarter import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey


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


Base.metadata.create_all(engine)
