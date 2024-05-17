from typing import Optional, List

from pydantic import BaseModel

class OrderItemSchema(BaseModel):
    id: Optional[int] = None
    item_id: Optional[str] = None
    order_id: Optional[int] = None
    
    class Config:
        orm_mode = True
    
class OrderSchema(BaseModel):
    id: Optional[int] = None
    status: Optional[str] = None
    user_id: Optional[int] = None
    freight: Optional[float] = 0.0
    
    class Config:
        orm_mode = True
    
class OrderWithItemsSchema(OrderSchema):
    items: Optional[List[OrderItemSchema]]
    
class OrderSchemaPost(OrderSchema):
    items: Optional[List[str]]