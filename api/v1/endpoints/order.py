from typing import List
from fastapi import APIRouter, status, Depends, HTTPException, Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.order_model import OrderItemModel, OrderModel
from models.user_model import UserModel

from schemas.order_schema import OrderItemSchema, OrderSchema, OrderWithItemsSchema, OrderSchemaPost
from core.deps import get_session, get_current_user

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=OrderSchema)
async def post_order(order: OrderSchemaPost, user_logged: UserModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    new_order: OrderModel = OrderModel(status="under analysis", user_id=user_logged.id, freight=order.freight)
    
    db.add(new_order)
    await db.commit()
    
    for item in order.items:
        new_order_item: OrderItemModel = OrderItemModel(item_id=str(item), order_id=new_order.id)
        
        db.add(new_order_item)
        await db.commit()
        
    return new_order
    
 
@router.get('/', status_code=status.HTTP_200_OK, response_model=List[OrderWithItemsSchema])
async def get_orders(me: bool = False, status: str = "", user_logged: UserModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    async with db as session:
        if status == "":
            if me:
                query = select(OrderModel).filter(OrderModel.user_id == user_logged.id)
            else:
                query = select(OrderModel)
         
        else:
            if me:
                query = select(OrderModel).filter(OrderModel.user_id == user_logged.id).filter(OrderModel.status == status)
            else:
                query = select(OrderModel).filter(OrderModel.status == status)
               
        result = await session.execute(query)
        orders: List[OrderModel] = result.scalars().unique().all()
        
        return orders

@router.get('/{order_id}/', status_code=status.HTTP_200_OK, response_model=OrderWithItemsSchema)
async def get_order(order_id: int, user_logged: UserModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(OrderModel).filter(OrderModel.id == order_id)
        result = await session.execute(query)
        order: OrderModel = result.scalars().unique().one_or_none()
        
        if order:
            return order
        else:
            raise HTTPException(detail='Order not found.', status_code=status.HTTP_404_NOT_FOUND)

@router.patch('/{order_id}/', status_code=status.HTTP_202_ACCEPTED, response_model=OrderWithItemsSchema)
async def patch_order_status(order_id: int, status: str, user_logged: UserModel = Depends(get_current_user), db: AsyncSession = Depends(get_session)):
    async with db as session:
        if user_logged.admin:
            query = select(OrderModel).filter(OrderModel.id == order_id)
            result = await session.execute(query)
            order_up = result.unique().scalar_one_or_none()
            
            if order_up:
                order_up.status=status
                
                await session.commit()
                
                return order_up
            else:
                raise HTTPException(detail='Order not found.', status_code=status.HTTP_404_NOT_FOUND)
        else:
            raise HTTPException(detail='You dont have that access.', status_code=status.HTTP_401_UNAUTHORIZED)