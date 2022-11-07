#python -m pip install fastapi
#python -m pip install unicorn[standard]
# main.py (create file)

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    car: str
    description: Optional[str] = None
    price: float
    link: Optional[float] = None

app = FastAPI()

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

# !uvicorn main:app --reload
# @app.get - /health
# @app.get("/items/{item_id}")