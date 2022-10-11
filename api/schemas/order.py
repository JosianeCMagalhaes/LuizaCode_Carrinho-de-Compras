
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field
from api.schemas.user import UserSchema
from api.schemas.address import AddressList

class OrderSchema(BaseModel):
    user: UserSchema
    price: Decimal = Field(max_digits=10, decimal_places=2, default=0)
    paid: bool = Field(default=False)
    address: AddressList
    created: str


