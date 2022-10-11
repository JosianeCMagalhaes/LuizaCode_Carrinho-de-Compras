from pydantic import BaseModel

from api.schemas.order import OrderSchema
from api.schemas.product import ProductSchema



class OrderItemSchema(BaseModel):
    order: OrderSchema
    product: ProductSchema