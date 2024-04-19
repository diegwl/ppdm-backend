from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Double
from sqlalchemy.orm import relationship

from core.configs import settings

class ItemModel(settings.DBBaseModel):
    __tablename__ = 'item'
    __allow_unmapped__ = True
    
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(255), nullable=False)
    value: float = Column(Double, nullable=False)
    details: str = Column(String(255), nullable=False)
    image: str = Column(String(255), nullable=False) 