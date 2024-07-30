from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from typing import List, Optional


# Class definition 

app = FastAPI()


class Item(BaseModel):
    id: int
    name : str
    description :Optional[str] = None
    price: float
    is_offer: Optional[str] = None


# database with List

item_list = []

# Root definition
@app.post('/items', response_model=Item)
async def create_Item(item : Item):
    if any(existing_item.id == item.id for existing_item in item_list):
        raise HTTPException(status_code =400, 
                            detail= "id already in use"
                            )
    item_list.append(item)
    return {"message": "item registered"}
    
@app.get('/')

async def root():
    return {"message": "hello"}
