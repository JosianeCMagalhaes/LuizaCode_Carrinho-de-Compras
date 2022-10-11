from fastapi import APIRouter
from api.routers import user, address, product, order

routes = APIRouter()

routes.include_router(user.router)
routes.include_router(address.router)
routes.include_router(product.router)
routes.include_router(order.router)