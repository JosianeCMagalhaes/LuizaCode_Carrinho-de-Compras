from fastapi import APIRouter, status, HTTPException
from starlette.responses import JSONResponse

from api.controllers.productController import create_product, delete_product, get_all_products, get_product_by_code, update_product
from api.schemas.product import ProductList, ProductSchema, ProductBaseSchema, ProductCodeSchema, ProductUpdatedSchema
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


# busca um produto por código
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


@router.put('/{code}', response_model=ProductSchema)
async def update_product_by_code(code: str, product_to_update: ProductUpdatedSchema):

    valid_price_stock = await check_product_price_stock(product_to_update)
   
    if(valid_price_stock):
        up_product = await update_product(code, product_to_update)

        return JSONResponse(
            status_code=status.HTTP_202_ACCEPTED,
            content={'Produto': up_product}
        ) 

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={'error': 'Dados inválidos, verifique o preço e a quantidade no estoque'}
    )


@router.delete('/{code}')
async def delete_product_by_code(code: str):

    product = await get_product_by_code(code)

    if product:
        delete_prod = await delete_product(code)

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'Mensagem': 'Produto excluído com sucesso' }
        ) 

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={'error': 'Produto não encontrado'}
    )


@router.get('/', response_model=ProductList)
async def get_products():
    products = await get_all_products()
    
    if products:

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'Produtos': products }
        ) 

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )


