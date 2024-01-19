from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://postgres:123@database:5432/flask-shop', echo=True)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base()
