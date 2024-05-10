from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.address_model import AddressModel
from models.user_model import UserModel

from schemas.address_schema import AddressSchema
from core.deps import get_session, get_current_user

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=AddressSchema)
async def post_address(address: AddressSchema, user_logged: UserModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    new_address: AddressModel = AddressModel(street=address.street, number=address.number, neighborhood=address.neighborhood, complement=address.complement, cep=address.cep, user_id=user_logged.id)
    
    db.add(new_address)
    await db.commit()
    
    return new_address