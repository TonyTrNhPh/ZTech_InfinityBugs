from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Player(Base):
    __tablename__ = 'LeaderBoard'

    id = Column(Integer, primary_key= True)
    name = Column(String)
    score = Column(Integer)
    level = Column(Integer)
    time = Column(DateTime)

    def __repr__(self):
        return f"<Player(name='{self.name}', score={self.score}, level={self.level}, time={self.time})>"