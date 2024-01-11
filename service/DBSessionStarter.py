from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///C:\\My Data\\Google Drive\\Programming\\Python\\Shop\\Shop\\identifier.sqlite',
                       echo=True)
Session = sessionmaker(bind=engine)
db_session = Session()
Base = declarative_base()
