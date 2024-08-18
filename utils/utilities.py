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

def error_number(err:str) -> int:
    err_lis = dict({'not_found': 404, 'bad_request': 400, 'failed': 500})
    return err_lis[err]

def message_error(err:str, status:str) -> str:
    err_lis = dict({'not_found': 'Data not found', 'bad_request': 'Bad request', 'failed': 'Failed to {} Data'.format(status)})
    return err_lis[err]