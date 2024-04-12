from typing import Optional, List

from pydantic import BaseModel, EmailStr

class UserSchemaBase(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    admin: bool = False
    
    class Config:
        from_attributes = True
        
class UserSchemaCreate(UserSchemaBase):
    password: str