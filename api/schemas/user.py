from pydantic import BaseModel, Field
from pydantic.networks import EmailStr


class UserSchema(BaseModel):
    name: str
    email: EmailStr = Field(unique=True, index=True)
    password: str
    is_active: bool = Field(default=True)
    is_admin: bool = Field(default=False)

    class Config:
        orm_mode = True

class UserEmail(BaseModel):
    email: EmailStr = Field(unique=True, index=True)