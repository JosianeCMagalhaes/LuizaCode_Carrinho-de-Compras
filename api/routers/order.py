from fastapi import APIRouter, status, HTTPException
from starlette.responses import JSONResponse
from api.controllers.orderController import create_cart
from api.controllers.productController import get_product_by_code
from api.controllers.userController import get_user_by_email
from api.schemas.cart import CartItemsSchema

from api.schemas.order import OrderSchema
from api.utils.descriptions import DESCRIPTION_CREATE_CART

# from api.controllers.orderController import 


router = APIRouter(prefix='/pedidos')

# validar o user na rota de criação do carrinho

 # validação se o produto adicionado existe

@router.post(
    '/carrinho', 
    description=DESCRIPTION_CREATE_CART,
    response_model=OrderSchema
)
async def create_order_by_cart(cart: CartItemsSchema):

    user = await get_user_by_email(cart.user.email)
    if user:
        product = await get_product_by_code(cart.product.code)
        print(product['quant_stock'])
        if product:

            new_cart = await create_cart(user, product, cart)

            return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content= {'Carrinho': new_cart}
            )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'error': 'Código do produto inválido. Produto não encontrado'}
        )

    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'error': 'Email inválido. Usuário não encontrado'}
    )