import logging
from fastapi import HTTPException, status
from api.middlewares.converters import fix_id

from api.schemas.order import OrderSchema
from api.schemas.product import ProductSchema

from api.server.database import db

async def create_order_item(order: OrderSchema, product: ProductSchema):
    
    try:        

        order_item_data = {
            "order": order,
            "product": [product]
        }

        order_item = await db.order_items_collection.insert_one(order_item_data)

        if order_item.inserted_id:
            order_item_db = await get_order_item(order_item.inserted_id)
            return order_item_db

    except Exception as error: 
        logging.exception(f'create_order_item.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
        

async def get_order_item(order_item_id):
    order_item = await db.order_items_collection.find_one({'_id': order_item_id})

    if order_item:
        return fix_id(order_item)

async def get_orders_items_by_order(order_id):
    orders_items = db.order_items_collection.find({'order._id': order_id})
    list_orders_items = await orders_items.to_list(length=10)
    list(map(fix_id, list_orders_items))
    return list_orders_items


