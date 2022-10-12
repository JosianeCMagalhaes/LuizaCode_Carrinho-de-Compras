from fastapi import HTTPException, status
import logging
from api.schemas.user import UserSchema
from api.middlewares.converters import object_id_string, fix_id

from api.server.database import db


async def create_user(user: UserSchema):
    try: 
        user = await db.users_collection.insert_one(user.dict())

        if user.inserted_id:
            user = await get_user_by_id(user.inserted_id)
            return user

    except Exception as error: 
        logging.exception(f'create_user.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

async def get_user_by_email(email):
  
    user = await db.users_collection.find_one({'email': email})
    
    if user:
        return fix_id(user)

    
async def get_user_by_id(user_id):
    
    user = await db.users_collection.find_one({'_id': object_id_string(user_id)})
    
    if user:
        return fix_id(user)


async def delete_user(user_id):
    try: 
    
        user_db = await db.users_collection.delete_one({'_id': object_id_string(user_id)})

        if user_db.deleted_count:
            return {'status': f'Usuário excluído com sucesso'}

    except Exception as error:
        logging.exception(f'delete_user.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


async def get_all_users():
    try:

        users_db = db.users_collection.find()
        users = await users_db.to_list(length=10)
        list(map(fix_id, users))
        return users

    except Exception as error:
        logging.exception(f'get_all_user.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)