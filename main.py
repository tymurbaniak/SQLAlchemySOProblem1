from sqlalchemy.orm import Session
from sqlalchemy import *
from model import Day
from model import Information


def get_informations_for_day(symbol):
    informations = []
    information_class = Information.get_information_class(symbol)
    informations.append(information_class(content="Some content1"))
    informations.append(information_class(content="Some other content"))
    informations.append(information_class(content="Another content"))
    informations.append(information_class(content="Example string"))
    informations.append(information_class(content="Lorem Ipsum"))
    return informations


def create_tables(symbol):
    engine = create_engine("mysql://trade2:trade2@localhost/trade2", encoding='utf-8')
    metadata = MetaData()

    Table(symbol + '_chart', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('date', DateTime, nullable=False),
                  Column('open', Float),
                  Column('close', Float),
                  Column('max', Float),
                  Column('min', Float),
                  Column('volume', Integer)
                  )

    Table(symbol + '_info', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('date', DateTime, nullable=False),
                 Column('datetime', DateTime, nullable=False),
                 Column('title', String(255)),
                 Column('content', Text),
                 Column('rating', Float),
                 Column('parentId', Integer, ForeignKey(symbol + '_chart.id'), nullable=False),
                 )
    metadata.create_all(engine)


def main():
    symbol = "cmp"
    informations = get_informations_for_day(symbol)
    day_class = Day.get_day_class(symbol)
    days = []
    days.append(day_class(informations=informations[0:2]))
    days.append(day_class(informations=informations[3:4]))
    create_tables(symbol)

    engine = create_engine("mysql://trade2:trade2@localhost/trade2", encoding='utf-8')

    session = Session(engine)
    session.connection()
    session.add_all(days)
    session.commit()
    session.flush()

if __name__ == "__main__":
    main()