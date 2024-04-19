from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from core.configs import settings

class AddressModel(settings.DBBaseModel):
    __tablename__ = 'address'
    __allow_unmapped__ = True
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    street: str = Column(String(255), nullable=False)
    number: str = Column(String(255), nullable=False)
    neighborhood: str = Column(String(255), nullable=False)
    complement: str = Column(String(255), nullable=True)
    cep: str = Column(String(255), nullable=False)
    user_id: int = Column('user_id', ForeignKey('user.id'))