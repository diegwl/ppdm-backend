from fastapi import APIRouter

from api.v1.endpoints import user
from api.v1.endpoints import address
from api.v1.endpoints import order

api_router = APIRouter()

api_router.include_router(user.router, prefix='/users', tags=['users'])
api_router.include_router(address.router, prefix='/address', tags=['address'])
api_router.include_router(order.router, prefix='/orders', tags=['orders'])