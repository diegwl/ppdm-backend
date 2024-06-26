from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

from core.configs import settings

from typing import List

class OrderItemModel(settings.DBBaseModel):
    __tablename__ = 'item_order'
    __allow_unmapped__ = True
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    item_id: str = Column(String(255), nullable=False)
    order_id: int = Column('order_id', ForeignKey('order.id'))

class OrderModel(settings.DBBaseModel):
    __tablename__ = 'order'
    __allow_unmapped__ = True
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    status: str = Column(String(255), nullable=False)
    user_id: int = Column('user_id', ForeignKey('user.id'))
    items: List[OrderItemModel] = relationship(
        "OrderItemModel", 
        uselist=True, 
        lazy="joined"
    )
    freight: float = Column(Float, nullable=False, default=0)