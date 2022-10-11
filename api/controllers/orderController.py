import logging
from fastapi import HTTPException, status
from api.middlewares.converter import converter_object_id, fix_id
from api.schemas.user import UserSchema
from api.controllers.addressController import get_address_by_user
from api.controllers.productController import get_product

from api.server.database import db


