import datetime
import json
from bson import ObjectId
from fastapi import HTTPException

# função p/ converter o ObjectId do mongo
def object_id_string(id):
    try:
        _id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Id inválido")
    return _id

# função p/ converter o ObjectId em string
def fix_id(data):
    if data.get('_id', False):
        data['_id'] = str(data['_id'])
        return data
    raise ValueError(f'_id não encontrado')
    

async def datetime_string():
    date_now = datetime.now()
    date_db = json.dumps(date_now, indent = 4, sort_keys = True, default = str)

    return date_db


# função p/ converter a lista de endereços em dicionário
async def dict_address(list):
    new_dict = {}
    for i in range(len(list)):
       new_dict = {
        "street": list[i].street,
        "cep,": list[i].cep,
        "district,": list[i].district,
        "city": list[i].city,
        "state": list[i].state,
        "is_delivery": list[i].is_delivery,
       }

    return new_dict


