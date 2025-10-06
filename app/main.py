from fastapi import FastAPI,HTTPException,status
from scalar_fastapi import get_scalar_api_reference
from typing import Any
from app.schemas import Shipment,ShipmentStatus




app=FastAPI()

shipments = {
    12701: {
        "weight": 1.2,
        "content": "wooden table",
        "status": "in_transit"
    },
    12702: {
        "weight": 0.8,
        "content": "ceramic vase",
        "status": "delivered"
    },
    12703: {
        "weight": 2.5,
        "content": "metal shelf",
        "status": "out_for_delivery"
    },
    12704: {
        "weight": 0.3,
        "content": "books",
        "status": "in_transit"
    },
    12705: {
        "weight": 5.0,
        "content": "office chair",
        "status": "delivered"
    },
    12706: {
        "weight": 3.7,
        "content": "computer monitor",
        "status": "delivered"
    },
    12707: {
        "weight": 1.0,
        "content": "printer cartridge",
        "status": "out_for_delivery"
    },
    12708: {
        "weight": 4.2,
        "content": "filing cabinet",
        "status": "in_transit"
    }
}



# @app.get("/shipment/latest")
# def get_latest_shipment() ->dict[str,Any]:
#     id=max(shipments.keys())
#     return shipments[id]


# # /shipment/1234
# @app.get("/shipment/{id}")
# def get_shipment(id:int) ->dict[str,Any]:
#     if id not in shipments:
#         return {"detail":"Given I'd doesn't exist"}
#     return shipments[id]


@app.get("/shipment/",response_model=Shipment)
def get_shipment(id:int|None=None):
    if not id:
        id=max(shipments.keys())
        shipment=shipments[id]
        return Shipment(**shipment)
    
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Given I'd Doesn't exist"
        )
    shipment=shipments[id]
    return Shipment(**shipment)

# @app.post("/shipment")
# def submit_shipment(content:str,weight:float) -> dict[str,int]:

#     if weight>25:
#         raise HTTPException(
#             status_code=status.HTTP_406_NOT_ACCEPTABLE,
#             detail="Maximum weight limit is 25 Kgs"
#         )

#     new_id=max(shipments.keys())+1
#     shipments[new_id]={   
#         "content":content,
#         "weight":weight,
#         "status":"placed"
#     }
#     return {"id":new_id}

@app.post("/shipment")
def submit_shipment(body:Shipment) -> dict[str,Any]:
    content=body.content
    new_id=max(shipments.keys())+1
    shipments[new_id]={   
        "content":content,
        "weight":body.weight,
        "status":"placed"
    }
    return {"id":new_id}

@app.get("/shipment/{field}")
def get_shipment_field(field:str,id:int) ->Any:
    return shipments[id][field]
    
@app.put("/shipment")
def shipment_update(id:int,content:str,weight:float,status:str) ->dict[str,Any]:
    shipments[id]={
        "content":content,
        "weight":weight,
        "status":status
    }
    return  shipments[id]

# @app.patch("/shipment")
# def patch_shipment(id:int,content:str|None=None,weight:float|None=None,status:str|None=None):
#     shipment=shipments[id]
#     if content is not None:
#         shipment["content"]=content
#     if weight is not None:
#         shipment["weight"]=weight
#     if status is not None:
#         shipment["status"]=status
    
#     shipments[id] = shipment
#     return shipment


@app.patch("/shipment")
def patch_shipment(id:int,body:dict[str,ShipmentStatus]):
    shipments[id].update(body)
    return shipments[id] 

@app.delete("/shipment")
def delete_shipment(id: int) ->dict[str,str]:
    if id in shipments:
        deleted_shipements=shipments.pop(id)
        return {"detail":f"Shipment with id {id} is deleted!"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="I'd doesn't exist already!")


@app.get("/scalar",include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API"
    )