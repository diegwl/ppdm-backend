from passlib.context import CryptContext

CRYPT = CryptContext(schemes=['bcrypt'], deprecated='auto')

def verify_password(password: str, hash: str) -> bool:
    return CRYPT.verify(password, hash=hash)

def generate_hash(password: str) -> str:
    return CRYPT.hash(password)