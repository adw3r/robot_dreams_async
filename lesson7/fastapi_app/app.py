from functools import partial
import random
from typing import Annotated
from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from pydantic import BaseModel, Field


app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Hello, world!"}


class Item(BaseModel):
    id: int = Field(..., default_factory=partial(random.randint, 1, 10_000))
    name: str
    description: str = None
    price: float
    tax: float = None


class ItemRepo:

    _memory: dict[int, Item] = {}

    def __init__(self):
        self._memory = {}

    def get(self, item_id: int) -> Item:
        return self._memory[item_id]

    def create(self, item: Item) -> Item:
        self._memory[item.id] = item
        return item

    def list(self) -> list[Item]:
        return list(self._memory.values())

    def delete(self, item_id: int) -> Item:
        return self._memory.pop(item_id)


repo = ItemRepo()


def get_repo() -> ItemRepo:
    global repo
    return repo


@app.post("/items/")
async def create_item(
    item: Item, repo: Annotated[ItemRepo, Depends(get_repo)]
) -> Item:
    return repo.create(item)


@app.get("/items/")
async def read_items(
    repo: Annotated[ItemRepo, Depends(get_repo)]
) -> list[Item]:
    return repo.list()


@app.get("/items/{item_id}")
async def read_item(
    item_id: int, repo: Annotated[ItemRepo, Depends(get_repo)]
) -> Item:
    try:
        return repo.get(item_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}")
async def delete_item(
    item_id: int, repo: Annotated[ItemRepo, Depends(get_repo)]
) -> Item:
    try:
        return repo.delete(item_id)
    except KeyError:
        raise HTTPException(status_code=404, detail="Item not found")
