from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import List, ClassVar

class Settings(BaseSettings):
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'mysql+asyncmy://root@127.0.0.1:3307/loja'
    DBBaseModel: ClassVar = declarative_base()
    
    JWT_SECRET: str = '83398ac3cde0759edcd720cfef61ba7c1d13251548b2b9db524213faa17a5310'
    
    ALGORITHM: str = 'HS256'
    
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        case_sensitive = True
        
settings: Settings = Settings()