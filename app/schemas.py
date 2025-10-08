

# class Shipment(BaseModel):
#     content:str=Field(max_length=100,description="Contents of the shipment")
#     weight:float=Field(le=25,ge=1,description="weight of the shipment in KGs.")
#     destination:int | None = Field(default_factory=random_destination,description="destination of the shipment")
#     status:ShipmentStatus


from enum import Enum
from pydantic import BaseModel, Field


class ShipmentStatus(str, Enum):
    placed = "placed"
    in_transit = "in_transit"
    out_for_delivery = "out_for_delivery"
    delivered = "delivered"


class BaseShipment(BaseModel):
    content: str
    weight: float = Field(le=25)
    destination: int


class ShipmentRead(BaseShipment):
    status: ShipmentStatus

class Order(BaseModel):
    price:int 
    title:str
    description:str 

class ShipmentCreate(BaseShipment):
    pass 
    

class ShipmentUpdate(BaseModel):
    content: str | None = Field(default=None)
    weight: float | None = Field(default=None, le=25)
    destination: int | None = Field(default=None)
    status: ShipmentStatus


