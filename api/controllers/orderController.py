import logging
from fastapi import HTTPException, status
from api.middlewares.converters import datetime_string, object_id_string, fix_id
from api.schemas.cart import CartItemsSchema
from api.schemas.product import ProductSchema
from api.schemas.user import UserSchema
from api.controllers.addressController import get_address_to_delivery
from api.controllers.productController import get_product, get_product_by_code
from api.controllers.userController import get_user_by_email


from api.server.database import db

async def create_cart(user: UserSchema, product: ProductSchema, cart: CartItemsSchema):

    try: 
        # validação se já tem um carrinho aberto
        cart_db = await get_order_open(user['_id'])
        
        if cart_db:
        # atualiza o cart com o novo produto
            ...

        cart_to_order = await transform_cart_to_order(user, product, cart)

        cart_db = await db.order_collection.insert_one(cart_to_order)

        if cart_db.inserted_id:
            cart = await get_order_open(user['_id'])
            return cart
    
    except Exception as error: 
        logging.exception(f'create_cart.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

async def get_order_open(user_id):
    cart = await db.order_collection.find_one({"$and": [{'user._id': user_id}, {'paid': False}]})
    if cart: 
        return fix_id(cart)
    


    
     
async def transform_cart_to_order(user: UserSchema, product: ProductSchema, cart: CartItemsSchema):
    price = 0
    price = price + (product['price'] * cart.product.quantity)
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
