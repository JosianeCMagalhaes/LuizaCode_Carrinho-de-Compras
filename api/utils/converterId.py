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

