from math import prod
from fastapi import APIRouter, status, HTTPException
from starlette.responses import JSONResponse

from api.controllers.productController import create_product, get_product_by_code
from api.schemas.product import ProductSchema, ProductBaseSchema, ProductCodeSchema
from api.middlewares.validators import check_product_price_stock
from api.utils.descriptions import DESCRIPTION_CREATE_PRODUCT


router = APIRouter(prefix='/produtos')

# cadastro de produto
@router.post('/cadastro', description=DESCRIPTION_CREATE_PRODUCT, response_model=ProductSchema)
async def createProduct(product: ProductBaseSchema):

    valid_price_stock = await check_product_price_stock(product)
   
    if(valid_price_stock):
        new_product = await create_product(product)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={'Produto': new_product}
        ) 

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={'error': 'Dados inválidos, verifique o preço e a quantidade no estoque'}
    )

@router.get('/{code}', response_model=ProductSchema)
async def search_product_code(code: str):

    product = await get_product_by_code(code)

    if product:
        return JSONResponse(
            status_code=status.HTTP_302_FOUND,
            content={'Produto': product}
        ) 

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={'error': 'Produto não encontrado'}
    )