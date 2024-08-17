from ..entity.employee import Employee as EmployeeEntity, RegisterEmployee
from ..repository.employee_repository import EmployeeRepository
from ..repository.user_repository import UserRepository
from ..utils.utilities import generate_id
from datetime import datetime as tim

class EmployeeService:
    def __init__(self):
        pass

    def get_by_id(self, id):
        return self.model.get_by_id(id)
    
    def get_all(self):
        return self.model.get_all() 
    
    def create(self, data:RegisterEmployee):
        dataEmployee = EmployeeEntity(id=generate_id(data.username), name=data.name, gender=data.gender, birthday=data.birthday, created_at=tim.now(), updated_at=tim.now(), username=data.username, password=data.password, role=data.role)
        userCheck = UserRepository().get_by_username(data.username)
        if not userCheck:
            EmployeeRepository().create(dataEmployee)
            UserRepository().create(dataEmployee)
            return True
        return False
    
    def update(self, id, data):
        return self.model.update(id, data)
    
    def delete(self, id):
        return self.model.delete(id)