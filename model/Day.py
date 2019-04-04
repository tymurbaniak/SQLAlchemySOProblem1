from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import Information

Base = declarative_base()
engine = None
session = None


def get_day_class(symbol):
    for c in Base._decl_class_registry.values():
        if hasattr(c, '__tablename__') and c.__tablename__ == symbol:
            return c

    class Day(Base):
        __tablename__ = symbol + '_chart'
        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True)
        informations = relationship(Information.get_information_class(symbol))

    return Day
