from pydantic import BaseModel, Field
from typing import List
from api.schemas.user import UserSchema

class Address(BaseModel):
    street: str
    cep: str
    district: str
    city: str
    state: str    
    is_delivery: bool = Field(default=True)

    
class AddressSchema(BaseModel):
    user: UserSchema
    address: List[Address] = []


class AddressList(AddressSchema):
    _id: str
    user: UserSchema

    class Config:
        orm_mode = True
