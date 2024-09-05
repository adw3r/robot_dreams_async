from fastapi import APIRouter
from .items import items_api

api = APIRouter(prefix="/api")
api.include_router(items_api)

api_v2 = APIRouter(prefix="/api/v2")
api_v2.include_router(items_api)