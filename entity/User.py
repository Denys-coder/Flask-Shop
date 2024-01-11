from service.DBSessionStarter import Base, engine
from sqlalchemy import Column, Integer, String, ForeignKey


class User(Base):
    __tablename__ = 'user'

    name = Column(String(64))
    surname = Column(String(64))
    password = Column(String(32))
    phone_number = Column(String(32))
    login = Column(String(32), primary_key=True)

    def __init__(self, name, surname, password, phone_number, login):
        self.name = name
        self.surname = surname
        self.password = password
        self.phone_number = phone_number
        self.login = login


Base.metadata.create_all(engine)
