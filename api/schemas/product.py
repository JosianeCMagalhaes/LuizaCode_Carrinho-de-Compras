from typing import Optional
from unicodedata import category
from pydantic import BaseModel, Field

class ProductBaseSchema(BaseModel):
    name: str = Field(max_length=200)
    description: str
    price: float 
    category: str
    quant_stock: int
    
# passar categorias de mercado, como padaria, alimentos, congelados, hortifruti, etc. 

class ProductCodeSchema(BaseModel):
    code: str = Field(unique=True, index=True)


class ProductSchema(ProductBaseSchema, ProductCodeSchema):
    # Possui todos os campos das duas classes
    ...


class ProductUpdatedSchema(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    category: Optional[str]
    quant_stock: Optional[int]