import uuid
import bcrypt

def generate_id(usr:str) -> str:
    namespace = uuid.UUID('00000000-0000-0000-0000-000000000000')
    uid_obj = str(uuid.uuid3(namespace, usr))
    return uid_obj.replace('-', '')

def hashing_password(password:str) -> str:
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash_pass = bcrypt.hashpw(bytes, salt)
    return str(hash_pass)

def check_password(password:str, hash_pass:str) -> bool:
    bytes = password.encode('utf-8')
    return bcrypt.checkpw(bytes, hash_pass)