from .database import Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey 
from sqlalchemy.orm import relationship

class CarInfo(Base):
    __tablename__ = 'CarInfo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String)
    year = Column(Integer)
    color = Column(String)
    mileage = Column(Integer)
    status = Column(Integer)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def attributes(self):
        return [column.name for column in self.__table__.columns]

class Listing(Base):
    __tablename__ = 'Listing'
    id = Column(Integer, primary_key=True)
    status = Column(String)


class BrokerInfo(Base):
    __tablename__ = 'BrokerInfo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    branch = Column(String)
    phone = Column(String)
    email = Column(String)

    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def attributes(self):
        return [column.name for column in self.__table__.columns]