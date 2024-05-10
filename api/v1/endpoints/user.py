from typing import List, Optional, Any

from fastapi import APIRouter, status, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError

from models.user_model import UserModel
from schemas.user_schema import UserSchemaBase, UserSchemaCreate, UserDetailsSchema

from core.deps import get_session, get_current_user
from core.security import generate_hash
from core.auth import authenticate, create_access_token

router = APIRouter()

@router.get('/logged/', response_model=UserSchemaBase)
def get_logged(user: UserModel = Depends(get_current_user)):
    return user

@router.get('/logged/details/', response_model=UserDetailsSchema)
def get_logged(user: UserModel = Depends(get_current_user)):
    return user

@router.post('/signup/', status_code=status.HTTP_201_CREATED, response_model=UserSchemaBase)
async def post_user(user: UserSchemaCreate, db: AsyncSession = Depends(get_session)):
    new_user: UserModel = UserModel(
        name=user.name,
        email=user.email,
        password=generate_hash(user.password),
        admin=user.admin
    )
    
    async with db as session:
        try:
            session.add(new_user)
            await session.commit()
            
            return new_user
        except IntegrityError:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, detail="Already exists this user email.")
    
@router.post('/login/')
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_session)):
    user = await authenticate(email=form_data.username, password=form_data.password, db=db)
    
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Wrong access data.')
    
    return JSONResponse(content={"access_token": create_access_token(sub=user.id), "token_type": "bearer"}, status_code=status.HTTP_200_OK)