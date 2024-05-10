from typing import Optional

from pydantic import BaseModel

class AddressSchema(BaseModel):
    id: Optional[int] = None
    street: str
    number: str
    neighborhood: str
    complement: Optional[str] = None
    cep: str
    user_id: Optional[int] = None
    
    class Config:
        orm_mode = True