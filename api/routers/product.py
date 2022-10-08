from fastapi import APIRouter, status, HTTPException
from starlette.responses import JSONResponse

from api.controllers.productController import create_product
from api.schemas.product import ProductSchema, ProductBaseSchema, ProductCodeSchema
from api.utils.validators import check_product_price_stock


router = APIRouter(prefix='/produtos')

# cadastro de produto
@router.post('/cadastro', response_model=ProductSchema)
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