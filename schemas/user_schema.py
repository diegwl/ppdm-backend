from typing import Optional, List

from pydantic import BaseModel, EmailStr

from schemas.order_schema import OrderSchema
from schemas.address_schema import AddressSchema

class UserSchemaBase(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    admin: bool = False
    
    class Config:
        from_attributes = True
        
class UserSchemaCreate(UserSchemaBase):
    password: str
    
class UserDetailsSchema(UserSchemaBase):
    orders: Optional[List[OrderSchema]] = None
    address: Optional[List[AddressSchema]] = None