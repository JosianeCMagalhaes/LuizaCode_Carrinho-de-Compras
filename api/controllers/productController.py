import logging
from uuid import uuid4
from fastapi import HTTPException, status
from api.schemas.product import ProductSchema, ProductBaseSchema, ProductCodeSchema
from api.middlewares.converter import converter_object_id, fix_id

from api.server.database import db


async def create_product(product: ProductBaseSchema):
  
    try:
       
        new_product = product.dict()
       
        new_product['code'] = str(uuid4().int)[:9]
   
        product = await db.product_collection.insert_one(new_product)

        if product.inserted_id:
            product = await get_product(product.inserted_id)
            return product

    except Exception as error:
        logging.exception(f'create_product.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


async def get_product(product_id):
    product = await db.product_collection.find_one({'_id': converter_object_id(product_id)})

    if product:
        return fix_id(product)