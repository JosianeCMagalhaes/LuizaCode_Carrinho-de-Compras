from fastapi import HTTPException, status
import logging
from api.schemas.user import UserSchema
from api.middlewares.converter import converter_object_id, fix_id

from api.server.database import db


async def create_user(user: UserSchema):
    try: 
        user = await db.users_collection.insert_one(user.dict())

        if user.inserted_id:
            user = await get_user(user.inserted_id)
            return user

    except Exception as error: 
        logging.exception(f'create_user.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

async def get_user_by_email(email):
  
    user = await db.users_collection.find_one({'email': email})
    
    if user:
        return fix_id(user)

    
async def get_user(user_id):
    
    user = await db.users_collection.find_one({'_id': converter_object_id(user_id)})
    
    if user:
        return fix_id(user)



   