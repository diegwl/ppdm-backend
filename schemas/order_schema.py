from typing import Optional, List

from pydantic import BaseModel

from schemas.item_schema import ItemSchema

class OrderItemSchema(BaseModel):
    id: Optional[int] = None
    item_id: int
    order_id: int
    
    class Config:
        orm_mode = True
    
class OrderSchema(BaseModel):
    id: Optional[int] = None
    status: str
    user_id: int
    
    class Config:
        orm_mode = True
    
class OrderWithItemsSchema(OrderSchema):
    items: Optional[List[ItemSchema]]