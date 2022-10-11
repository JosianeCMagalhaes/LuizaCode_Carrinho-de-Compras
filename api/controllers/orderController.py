import logging
from fastapi import HTTPException, status
from api.controllers.orderItemController import create_order_item
from api.middlewares.converters import datetime_string, object_id_string, fix_id
from api.schemas.cart import CartItemsSchema
from api.schemas.order import OrderSchema
from api.schemas.product import ProductSchema
from api.schemas.user import UserSchema
from api.controllers.addressController import get_address_to_delivery



from api.server.database import db

async def create_cart(user: UserSchema, product: ProductSchema, cart: CartItemsSchema):

    try: 
        # validação se já tem um carrinho aberto
        order_db = await get_order_open(user['_id'])
        print(order_db)

        if order_db:
        # atualiza o pedido com o novo produto
            order = await update_order_price(order_db, cart, product)
            order_item = await create_order_item(order_db, product)

            return order

        cart_to_order = await transform_cart_to_order(user, product, cart)
        cart_db = await db.order_collection.insert_one(cart_to_order)

        if cart_db.inserted_id:
            order = await get_order_open(user['_id'])
            order_item = await create_order_item(order, product)
        return order
    
    except Exception as error: 
        logging.exception(f'create_cart.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


async def get_order_by_id(order_id):
    order = await db.order_collection.find_one({'_id': object_id_string(order_id)})
    if order:
        return fix_id(order)


async def get_order_open(user_id):
    cart = await db.order_collection.find_one({"$and": [{'user._id': user_id}, {'paid': False}]})
    if cart: 
        return fix_id(cart)


async def update_order_price(order: OrderSchema, cart: CartItemsSchema, product: ProductSchema):

    try: 
        order_total_price = order['price']
        order_total_price = order_total_price + (product['price'] * cart.product.quantity)

        new_price ={ 'price': order_total_price}

        order_update = await db.order_collection.update_one(
            {'_id': object_id_string(order['_id'])},
            { '$set': new_price}
        )

        if order_update.modified_count:
            order = await get_order_by_id(order['_id'])
            return order

    except Exception as error: 
        logging.exception(f'update_order_price.error: {error}')
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED)



async def transform_cart_to_order(user: UserSchema, product: ProductSchema, cart: CartItemsSchema):
    price = (product['price'] * cart.product.quantity)
    address = await get_address_to_delivery(user['email'])

    date_db = await datetime_string()
  
    cart_trasform = {
        "user": user,
        "price": price,
        "paid": False, 
        "address": address,
        "created": date_db
    }

    return cart_trasform
