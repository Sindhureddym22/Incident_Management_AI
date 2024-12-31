from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Ticket(Base):
    __tablename__ = 'tickets'
    id = Column(Integer, primary_key=True)
    query = Column(String, unique=True)  # Ensure unique queries
    response = Column(String)


def init_db():
    engine = create_engine('sqlite:///db/support_tickets.db')
    Base.metadata.create_all(engine)


def get_db():
    engine = create_engine('sqlite:///db/support_tickets.db')
    Session = sessionmaker(bind=engine)
    return Session()
