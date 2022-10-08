import re
import logging

from api.schemas.product import ProductSchema


async def check_email(email):
    if(len(email) < 3):
        return False

    regex = r'^[a-zA-Z0-9._-]+@([a-z0-9]+)(\.[a-z]{2,3})+$'

    if(re.match(regex, email)):
        return True
    
    return False

# validação do preço e da quantidade de estoque do produto
async def check_product_price_stock(product: ProductSchema):
    try:
        if product.price > 0.01 and product.quant_stock > 0:
            return True

        return False

    except Exception as error:
        logging.exception(f'check_product_price_stock.error: {error}')

