from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///identifier.sqlite', echo=True)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base()
