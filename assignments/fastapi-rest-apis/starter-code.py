from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True
    description: Optional[str] = None

class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query": q}

@app.get("/sum")
def sum_numbers(a: int, b: int):
    return {"a": a, "b": b, "sum": a + b}

@app.post("/items/")
def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}

@app.post("/users/")
def create_user(user: User):
    return {"message": "User registered successfully", "user": user}
