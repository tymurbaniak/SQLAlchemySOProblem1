from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = None
session = None


def get_information_class(symbol):
    for c in Base._decl_class_registry.values():
        if hasattr(c, '__tablename__') and c.__tablename__ == symbol:
            return c

    class Information(Base):
        __tablename__ = symbol + '_info'
        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True)
        content = Column(Text(255))
        parentId = Column(Integer, ForeignKey(symbol + '_chart.id'), nullable=True)

    return Information