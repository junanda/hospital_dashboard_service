from ..entity.employee import Employee as EmployeeEntity, RegisterEmployee, EmployeeResult
from ..repository.employee_repository import EmployeeRepository
from ..repository.user_repository import UserRepository
from ..utils.utilities import generate_id, hashing_password
from datetime import datetime as tim
import json

class EmployeeService:
    def __init__(self):
        pass

    def get_by_id(self, id):
        result = EmployeeRepository().get_by_id(id)
        if result is not None:
            return EmployeeResult(
                id=result.id, 
                name=result.name, 
                gender=result.gender, 
                birthday=str(result.birthday), 
                created_at=str(result.created_at), 
                updated_at=str(result.updated_at)
                ).model_dump()
        return result
    
    def get_all(self):
        result = []
        employees = EmployeeRepository().get_all()
        if len(employees) > 0:
            result = [EmployeeResult(id=empl.id, name=empl.name, gender=empl.gender, birthday=str(empl.birthday), created_at=str(empl.created_at), updated_at=str(empl.updated_at)).model_dump() for empl in employees]
        
        return result
        
    
    def create(self, data:RegisterEmployee):
        result = False
        err = 'Username already exists'

        pass_hash = hashing_password(data.password)
        dataEmployee = EmployeeEntity(id=generate_id(data.username), name=data.name, gender=data.gender, birthday=data.birthday, created_at=tim.now(), updated_at=tim.now(), username=data.username, password=pass_hash, role=data.role)
        userCheck = UserRepository().get_by_username(data.username)
        if not userCheck:
            result, err = EmployeeRepository().create(dataEmployee)
        
        empl_result = EmployeeRepository().get_by_id(dataEmployee.id)

        dataE = EmployeeResult(id=empl_result.id, name=empl_result.name, gender=empl_result.gender, birthday=str(empl_result.birthday), created_at=str(empl_result.created_at), updated_at=str(empl_result.updated_at))
        return result, err, dataE.model_dump()
    
    def update(self, id, data):
        result = EmployeeRepository().update(id, data)
        if result:
            se = EmployeeRepository().get_by_id(id)
            data = EmployeeResult(
                id=se.id, 
                name=se.name, 
                gender=se.gender, 
                birthday=str(se.birthday), 
                created_at=str(se.created_at), 
                updated_at=str(se.updated_at)
                ).model_dump()
            return result, data
        return result, None 
    
    def delete(self, id):
        result, err = EmployeeRepository().delete(id)
        return result, err