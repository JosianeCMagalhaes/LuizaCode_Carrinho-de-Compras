from fastapi import APIRouter
from api.routers import user 

routes = APIRouter()

routes.include_router(user.router)