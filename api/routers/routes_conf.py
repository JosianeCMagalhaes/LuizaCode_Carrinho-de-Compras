from fastapi import APIRouter
from api.routers import user, address

routes = APIRouter()

routes.include_router(user.router)
routes.include_router(address.router)