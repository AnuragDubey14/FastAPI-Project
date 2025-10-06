from pydantic import BaseModel ,Field
from random import randint
from enum import Enum

class ShipmentStatus(str,Enum):
    placed="Placed"
    in_transit="in_transit"
    out_for_delivery="out_for_delivery"
    delivered="delivered"



def random_destination():
    return randint(99999,999999)

class Shipment(BaseModel):
    content:str=Field(max_length=100,description="Contents of the shipment")
    weight:float=Field(le=25,ge=1,description="weight of the shipment in KGs.")
    destination:int | None = Field(default_factory=random_destination,description="destination of the shipment")
    status:ShipmentStatus





