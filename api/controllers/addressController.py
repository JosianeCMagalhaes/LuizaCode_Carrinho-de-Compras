import logging
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from api.middlewares.converters import object_id_string, fix_id


from api.schemas.address import Address


from api.server.database import db


async def create_address(user, address):
   
    try: 
        dict_address = dict(
            user=user, 
            address=address
        )

        address = await db.address_collection.insert_one(jsonable_encoder(dict_address))
        
        if address.inserted_id:
            address = await get_address(address.inserted_id)
            print(address)
            return address
    
    except Exception as error: 
        logging.exception(f'create_address.error: {error}')
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)


async def get_address(address_id):
   
    address = await db.address_collection.find_one({'_id': object_id_string(address_id)})
   
    if(address):
        return fix_id(address)


async def get_address_by_email(user_email):
  
    address = await db.address_collection.find_one({'user.email': user_email})
    
    if(address):
        return fix_id(address)

async def add_address_user(user_email, address: Address):
    try: 
        
        dict_address = await dict_address(address)
               
        address_data = dict_address
        address_data = {k: v for k, v in address_data.items() if v is not None}
        # print(address_data)
        new_address = await db.address_collection.find_one({'user.email': user_email})

        new_address['address'].append(address_data)

        add_address = await db.address_collection.update_one(
            {'_id': object_id_string(new_address['_id'])},
            {'$set': new_address}
        )
        
        if add_address.modified_count:
            address = await get_address(new_address['_id'])
            return address

    except Exception as error: 
        logging.exception(f'add_address_user.error: {error}')
        raise HTTPException(status_code=status.HTTP_304_NOT_MODIFIED)

async def get_address_to_delivery(user_email):
    find_address = await get_address_by_email(user_email)
    
    if find_address:
        for add in find_address["address"]:
            if add["is_delivery"]:
                return add
   