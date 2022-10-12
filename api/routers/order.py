from fastapi import APIRouter, status, HTTPException
from starlette.responses import JSONResponse
from api.controllers.orderController import create_cart, delete_order, get_all_orders, get_order_by_id, get_order_open, get_orders_and_products
from api.controllers.productController import get_product_by_code
from api.controllers.userController import get_user_by_email
from api.schemas.cart import CartItemsSchema

from api.schemas.order import OrderList, OrderSchemaOpen, OrderSchema, OrderSchemaOpen
from api.utils.descriptions import DESCRIPTION_CREATE_CART

# from api.controllers.orderController import 


router = APIRouter(prefix='/pedidos')

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

# consulta os pedidos em aberto. O email deve ser passado no parametro
@router.get('/carrinho', response_model=OrderSchemaOpen)
async def search_order_open(email: str):

    user = await get_user_by_email(email)

    if user:

        order_open = await get_orders_and_products(user['_id'])

        return JSONResponse(
                status_code=status.HTTP_200_OK, 
                content= {'Pedido em aberto': order_open}
        )

    raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'error': 'Email inválido. Usuário não encontrado'}
    )

@router.get('', response_model=OrderList)
async def get_orders():
    orders = await get_all_orders()

    if orders:

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'Pedidos': orders }
        ) 

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )


# exclui um pedido do sistema pelo id que deve ser passado como parametro
@router.delete('/carrinho/{id}')
async def delete_order_by_id(id: str):

    order = await get_order_by_id(id)

    if order: 
        order_delete = await delete_order(order['_id'])

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'Mensagem': 'Pedido excluído com sucesso' }
        ) 

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={'error': 'Pedido não encontrado'}
    )
