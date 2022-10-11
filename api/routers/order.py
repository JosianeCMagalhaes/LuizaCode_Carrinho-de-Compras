from fastapi import APIRouter, status, HTTPException
from starlette.responses import JSONResponse

from api.schemas.order import OrderSchema

# from api.controllers.orderController import 


router = APIRouter(prefix='/pedidos')