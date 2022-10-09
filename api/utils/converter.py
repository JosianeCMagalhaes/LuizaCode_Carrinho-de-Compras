from bson import ObjectId
from fastapi import HTTPException


def converter_object_id(id):
    try:
        _id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="Id inválido")
    return _id

def fix_id(data):
    if data.get('_id', False):
        data['_id'] = str(data['_id'])
        return data
    raise ValueError(f'_id não encontrado')

async def convert_dict_address(list):
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
