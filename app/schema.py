from pydantic import BaseModel
from typing import Optional, List


class Listing(BaseModel):
    id: int
    status: str

    class Config:
        orm_mode = True


class CarInfo(BaseModel):
    id: int
    brand: str
    year: int
    color: str
    mileage: int
    status: int

    class Config:
        orm_mode = True


class UpdateCarInfo(BaseModel):
    id: Optional[int]
    brand: Optional[str]
    year: Optional[int]
    color: Optional[str]
    mileage: Optional[int]
    status: Optional[int]

    class Config:
        orm_mode = True


class BrokerInfo(BaseModel):
    id: int
    name: str
    branch: str
    phone: str
    email: str

    class Config:
        orm_mode = True

class UpdateBrokerInfo(BaseModel):
    id: Optional[int]
    name: Optional[str]
    branch: Optional[str]
    phone: Optional[str]
    email: Optional[str]

    class Config:
        orm_mode = True
