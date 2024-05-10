from typing import Optional

from pydantic import BaseModel

class ItemSchema(BaseModel):
    id: Optional[int] = None
    name: str
    value: float
    details: str
    image: str
    
    class Config:
        orm_mode = True