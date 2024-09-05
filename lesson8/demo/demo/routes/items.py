from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from demo import deps
from demo.schemas import Item
from demo.models import Item as ItemModel

items_api = APIRouter(prefix="/items")


@items_api.get("/")
async def read_items() -> list[Item]:
    return [{"name": "Item One", "price": 1}, {"name": "Item Two", "price": 2}]


@items_api.post("/")
async def create_item(item: Item, db: Annotated[AsyncSession, Depends(deps.get_db_session)]):
    im = ItemModel(**item.model_dump())
    db.add(im)
    await db.commit()

    # would not work wihout the refresh
    # refresh the instance to get the default values (pk, etc.)
    await db.refresh(im)  
    return Item.model_validate(im)
