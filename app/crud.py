from sqlalchemy.orm import Session
from . import schema, models
from .schema import CarInfo, UpdateCarInfo,Listing, UpdateBrokerInfo


def save_car_info(db: Session, info: schema.CarInfo):
    car_info_model = models.CarInfo(**info.dict())
    db.add(car_info_model)
    db.commit()
    db.refresh(car_info_model)
    return car_info_model

def get_car_info(db: Session, id: int = None):
    if id is None:
        return db.query(models.CarInfo).all()
    else:
        return db.query(models.CarInfo).filter(models.CarInfo.id == id).first()


def delete_car_info(db: Session, id: int):
    obj = db.query(models.CarInfo).filter(models.CarInfo.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
        return obj


def update_car_info(db: Session, id: int, info: UpdateCarInfo):
    obj = db.query(models.CarInfo).filter(models.CarInfo.id == id).first()
    if obj:
        for attr in obj.attributes():
            if getattr(info, attr) is not None:
                setattr(obj, attr, getattr(info, attr))
        db.commit()
        return obj.as_dict()

def insert_listing(db: Session, info: schema.Listing):
    status_info = models.Listing(**info.dict())
    db.add(status_info)
    db.commit()
    db.refresh(status_info)
    return status_info

def get_listing_info(db: Session, id: int = None):
    if id is None:
        return db.query(models.Listing).all()
    else:
        return db.query(models.Listing).filter(models.Listing.id == id).first()

def save_broker_info(db: Session, info: schema.BrokerInfo):
    broker_info_model = models.BrokerInfo(**info.dict())
    db.add(broker_info_model)
    db.commit()
    db.refresh(broker_info_model)
    return broker_info_model

def get_broker_info(db: Session, id: int = None):
    if id is None:
        return db.query(models.BrokerInfo).all()
    else:
        return db.query(models.BrokerInfo).filter(models.BrokerInfo.id == id).first()


def delete_broker_info(db: Session, id: int):
    obj = db.query(models.BrokerInfo).filter(models.BrokerInfo.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
        return obj


def update_broker_info(db: Session, id: int, info: UpdateBrokerInfo):
    obj = db.query(models.BrokerInfo).filter(models.BrokerInfo.id == id).first()
    if obj:
        for attr in obj.attributes():
            if getattr(info, attr) is not None:
                setattr(obj, attr, getattr(info, attr))
        db.commit()
        return obj.as_dict()

def error_message(message):
    return {
        'error': message
    }
