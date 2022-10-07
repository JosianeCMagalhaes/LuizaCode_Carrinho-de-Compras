
from fastapi import APIRouter, status
from starlette.responses import JSONResponse

from api.controllers.addressController import create_address, get_address_by_email, add_address_user
from api.schemas.user import UserSchema
from api.controllers.userController import get_user_by_email
from api.schemas.address import Address, AddressSchema



router = APIRouter(prefix='/enderecos')


@router.post('/cadastro', response_model=AddressSchema)
async def create(address: AddressSchema):

    # verifica se o usuário existe p/ cadastrar
    user = await get_user_by_email(address.user.email)

    if(user): 

        # conferi se o usuário já tem endereço cadastrado
        user_has_address = await get_address_by_email(user['email'])
       

        if(user_has_address):

            add_address = await add_address_user(user['email'], address.address)

            return JSONResponse(
                status_code=status.HTTP_202_ACCEPTED, 
                content= {'Endereços': add_address}
            )
        else:
            new_address = await create_address(user, address.address)

            return JSONResponse(
                    status_code=status.HTTP_201_CREATED, 
                    content= {'Endereços': new_address}
                )
    
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={'error': 'Usuário não encontrado'}
    )

# busca endereços pelo usuário com base no email que deve ser passado na query

@router.get('', response_model=Address)
async def get_address(email: str):

    user = await get_user_by_email(email)
    
    if(user):
        address = await get_address_by_email(user['email'])
        return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={'Endereços': address['address']}
            )

    return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND, 
            content={'error': 'Usuário não encontrado'}
        )




