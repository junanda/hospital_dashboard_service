from ..models.user import User
# from ..entity.employee import Employee as EmployeeEntity
from datetime import datetime as tim

class UserRepository:
    def __init__(self):
        pass
    
    def get_by_traceid(self, id:str):
        return self.model.get_by_id(id)
    
    def get_by_username(self, username: str):
        userdb = User.query.filter_by(username=username).first()
        return userdb
    
    def create(self, data):
        user = User(data.id, data.username, data.password, data.role, tim.now(), tim.now())
        return user.create()
    
    def update(self, id, data):
        return self.model.update(id, data)
    
    def delete(self, id):
        return self.model.delete(id)