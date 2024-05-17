from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

from typing import List

from models.address_model import AddressModel
from models.order_model import OrderModel

class UserModel(settings.DBBaseModel):
    __tablename__ = 'user'
    __allow_unmapped__ = True
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(255), nullable=False)
    email: str = Column(String(255), nullable=False, unique=True)
    password: str = Column(String(255), nullable=False)
    admin: bool = Column(Boolean, default=False)
    address: List[AddressModel] = relationship(
        "AddressModel",
        uselist=True,
        lazy='joined'
    )
    orders: List[OrderModel] = relationship(
        "OrderModel",
        uselist=True,
        lazy='joined'
    )