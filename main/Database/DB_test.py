import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DB_URI
from Players import Base, Player

engine = create_engine(DB_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

new_player = Player(name='John Doe', score=90, level=1, time=formatted_time)
session.add(new_player)
session.commit()

players_list = session.query(Player).all()
for player in players_list:
    print(player)

session.close()