from collections import UserList
from fastapi import APIRouter, status, HTTPException
from starlette.responses import JSONResponse

from api.controllers.userController import create_user, delete_user, get_all_users, get_user_by_email, get_user_by_id
from api.schemas.user import UserSchema, UserList
from api.middlewares.validators import check_email
from api.utils.descriptions import DESCRIPTION_CREATE_USER


router = APIRouter(prefix='/usuarios')

# cadastro de usuário

@router.post('/cadastro', description=DESCRIPTION_CREATE_USER,response_model= UserSchema)
async def createUser(user: UserSchema):

    valid_email = await check_email(user.email)

    if(valid_email):
    
        user_db = await get_user_by_email(email = user.email)
        if(user_db):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail={'error': 'Email já cadastrado'}
            )
        
    
        new_user = await create_user(user)

        return JSONResponse(
            status_code=status.HTTP_201_CREATED, 
            content= {'Usuário': new_user}
        )

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={'error': 'Email inválido. Informe um email válido'}
    )


# buscar usuário pelo email, o email deve ser passado na query

@router.get('/email', response_model= UserSchema)
async def get_user(email: str):
    
    valid_email = await check_email(email)

    if(valid_email):
        user_db = await get_user_by_email(email)
        
        if(user_db):
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={'Usuário': user_db}
            )

        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail= {'error':'Usuário não encontrado'}
        )

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={'error':'Email inválido. Informe um email válido'}
    )

# busca todos os usuários
@router.get('/', response_model=UserList)
async def get_users():
    users = await get_all_users()
    
    if users:
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'Usuários': users }
        ) 

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST
    )

# deleta o usuário com base no id que deve ser passado na rota
@router.delete('/{id}')
async def delete_user_by_id(id: str):
    
    user = await get_user_by_id(id)

    if user:
        user_delete = await delete_user(user['_id'])

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={'Mensagem': 'Usuário excluído com sucesso' }
        ) 

    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={'error': 'Usuário não encontrado'}
    )