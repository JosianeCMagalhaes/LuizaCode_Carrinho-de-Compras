from itertools import product
import logging
from uuid import uuid4
from fastapi import HTTPException, status
from api.schemas.product import ProductSchema, ProductBaseSchema, ProductCodeSchema, ProductUpdatedSchema
from api.middlewares.converters import object_id_string, fix_id

from api.server.database import db


async def create_product(product: ProductBaseSchema):
  
    try:
        new_product = product.dict()
       
        # gera o código automaticamente
        new_product['code'] = str(uuid4().int)[:9]
   
        product = await db.product_collection.insert_one(new_product)

        if product.inserted_id:
            product = await get_product(product.inserted_id)
            return product

    except Exception as error:
        logging.exception(f'create_product.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

async def get_product(product_id):
    product = await db.product_collection.find_one({'_id': object_id_string(product_id)})

    if product:
        return fix_id(product)

async def get_product_by_code(product_code: ProductCodeSchema):
    product = await db.product_collection.find_one({'code': product_code})

    if product: 
        return fix_id(product)

async def get_all_products():
    try:

        products_db = db.product_collection.find()
        products = await products_db.to_list(length=10)
        list(map(fix_id, products))
        return products

    except Exception as error:
        logging.exception(f'get_all_product.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


async def update_product(product_code, product_data: ProductUpdatedSchema):

    try:
        product_by_code = await get_product_by_code(product_code)

        product = product_data.dict()
        product = {k: v for k, v in product.items() if v is not None}

        product_db = await db.product_collection.update_one(
            {'_id': object_id_string(product_by_code['_id'])},
            {'$set': product}
        )

        if product_db.modified_count:
            product_updated = await get_product(product_by_code['_id'])
            return product_updated

    except Exception as error:
        logging.exception(f'update_product.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

async def delete_product(product_code: ProductCodeSchema):
    
    try: 
        product = await get_product_by_code(product_code)

        product_db = await db.product_collection.delete_one({'_id': object_id_string(product['_id'])})

        if product_db.deleted_count:
            return {'status': f'Produto excluído com sucesso'}

    except Exception as error:
        logging.exception(f'delete_product.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

