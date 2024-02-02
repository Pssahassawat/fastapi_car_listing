from fastapi import FastAPI, Depends, HTTPException
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from .schema import CarInfo, BrokerInfo, Listing, UpdateCarInfo, UpdateBrokerInfo
from . import crud, models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def db_create_session():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post('/car/info')
def save_car_info(info: CarInfo, db=Depends(db_create_session)):
    status_in_db = crud.get_listing_info(db, info.status)
    if status_in_db:
        object_in_db = crud.get_car_info(db, info.id)
        if object_in_db:
            raise HTTPException(400, detail=crud.error_message('This car info already exists'))
        return crud.save_car_info(db, info)
    else:
        raise HTTPException(400, detail=crud.error_message('No status'))


@app.get('/car/info/{id}')
def get_car_info(id: int, db=Depends(db_create_session)):
    info = crud.get_car_info(db, id)
    if info:
        return info
    else:
        raise HTTPException(404, detail=crud.error_message('No car found for id {}'.format(id)))


@app.get('/car/info')
def get_all_car_info(db=Depends(db_create_session)):
    return crud.get_car_info(db)


@app.delete('/car/delete/{id}')
def delete_car_info(id: int, db=Depends(db_create_session)):
    deleted_info = crud.delete_car_info(db, id)
    if deleted_info:
        return "OK"
    else:
        raise HTTPException(404, detail=crud.error_message('No car found for id {}'.format(id)))


@app.patch('/car/update/{id}')
def update_car_info(id: int, info: UpdateCarInfo, db=Depends(db_create_session)):
    status_in_db = crud.get_listing_info(db, info.status)
    if status_in_db:
        updated_info = crud.update_car_info(db, id, info)
        if updated_info:
            return updated_info
        else:
            raise HTTPException(404, detail=crud.error_message('No device found for id {}'.format(id)))
    else:
         HTTPException(400, detail=crud.error_message('No status'))   


@app.post('/listing/info')
def status_info(info: Listing, db=Depends(db_create_session)):
    object_in_db = crud.get_listing_info(db, info.id)
    if object_in_db:
        raise HTTPException(400, detail=crud.error_message('This device info already exists'))
    return crud.insert_listing(db, info)

@app.get('/listing/info')
def get_all_listing_info(db=Depends(db_create_session)):
    return crud.get_listing_info(db)


@app.post('/broker/info')
def save_broker_info(info: BrokerInfo, db=Depends(db_create_session)):
    object_in_db = crud.get_broker_info(db, info.id)
    if object_in_db:
        raise HTTPException(400, detail=crud.error_message('This broker info already exists'))
    return crud.save_broker_info(db, info)

@app.get('/broker/info/{id}')
def get_broker_info(id: int, db=Depends(db_create_session)):
    info = crud.get_broker_info(db, id)
    if info:
        return info
    else:
        raise HTTPException(404, detail=crud.error_message('No broker found for id {}'.format(id)))

@app.get('/broker/info')
def get_all_broker_info(db=Depends(db_create_session)):
    return crud.get_broker_info(db)

@app.delete('/broker/delete/{id}')
def delete_broker_info(id: int, db=Depends(db_create_session)):
    deleted_info = crud.delete_broker_info(db, id)
    if deleted_info:
        return "OK"
    else:
        raise HTTPException(404, detail=crud.error_message('No broker found for id {}'.format(id)))

@app.patch('/broker/update/{id}')
def update_broker_info(id: int, info: UpdateBrokerInfo, db=Depends(db_create_session)):
    updated_info = crud.update_broker_info(db, id, info)
    if updated_info:
        return updated_info
    else:
        raise HTTPException(404, detail=crud.error_message('No broker found for id {}'.format(id)))
