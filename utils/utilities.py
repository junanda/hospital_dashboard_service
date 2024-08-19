import uuid
import jwt
from passlib.hash import bcrypt
from datetime import datetime, timedelta
from functools import wraps
from flask import request, jsonify

def generate_id(usr:str) -> str:
    namespace = uuid.UUID('00000000-0000-0000-0000-000000000000')
    uid_obj = str(uuid.uuid3(namespace, usr))
    return uid_obj.replace('-', '')

def hashing_password(password:str) -> str:
    hash_pass = bcrypt.hash(password)
    return hash_pass

def check_password(password:str, hash_pass:str) -> bool:
    try:
        return bcrypt.verify(password, hash_pass)
    except Exception as e:
        print(f'Error Veryify Password: {e}')
        return False

def error_number(err:str) -> int:
    err_lis = dict({'not_found': 404, 'bad_request': 400, 'failed': 500})
    return err_lis[err]

def message_error(err:str, status:str) -> str:
    err_lis = dict(
        {'not_found': 'Data not found', 
         'bad_request': 'Bad request', 
         'failed': 'Failed to {} Data'.format(status), 
         'username_already_exists': 'Username already exists',
         'greater_than': 'Value work_start_time cannot be greater than work_end_time',
         })
    return err_lis[err]

def generate_token(user_id, role) -> str:
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=10),
            'iat': datetime.utcnow(),
            'sub': user_id,
            'role': role
        }
        return jwt.encode(
            payload,
            'secret',
            algorithm='HS256'
        )
    except Exception as e:
        return e

def decode_token(token:str) -> dict:
    try:
        return jwt.decode(token, 'secret', algorithms=['HS256'])
    except Exception as e:
        return e

def authentication(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(' ')[1]
        if not token:
            return jsonify({'status': 'failed', 'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, 'secret', algorithms=['HS256'])
            current_user = {'id': data['sub'], 'role': data['role']}
        except:
            return jsonify({'status': 'failed','message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated
