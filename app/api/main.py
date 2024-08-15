from fastapi import APIRouter, Depends
from app.api.endpoints import fruit


APIRouter

api_router = APIRouter()
api_router.include_router(fruit.router, prefix='/fruit', tags= ['fruit'], responses={404:{"description": "Not found"}})
