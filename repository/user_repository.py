from ..models.user import User
# from ..entity.employee import Employee as EmployeeEntity
from datetime import datetime as tim

class UserRepository:
    def __init__(self):
        pass
    
    def get_by_traceid(self, id:str):
        result = User.query.filter_by(id_trace=id).first()
        return result
    
    def get_by_username(self, username: str):
        userdb = User.query.filter_by(username=username).first()
        return userdb
    
    def create(self, data):
        user = User(data.id, data.username, data.password, data.role, tim.now(), tim.now())
        return user.create()