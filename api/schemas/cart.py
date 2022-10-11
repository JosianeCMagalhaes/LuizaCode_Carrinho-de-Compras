from typing import List, Optional
from pydantic import BaseModel

from api.schemas.product import ProductCart
from api.schemas.user import UserEmail

class CartItemsSchema(BaseModel):
    user: UserEmail
    product: ProductCart

