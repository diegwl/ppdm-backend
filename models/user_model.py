from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class UserModel(settings.DBBaseModel):
    __tablename__ = 'user'
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(255), nullable=False)
    email: str = Column(String(255), nullable=False)
    password: str = Column(String(255), nullable=False)
    admin: bool = Column(Boolean, default=False)