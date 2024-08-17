from datetime import datetime
from ..models.employee import Employee
from ..entity.employee import Employee as EmployeeEntity

class EmployeeRepository:
    def __init__(self):
        pass

    def get_by_id(self, id):
        return self.model.get_by_id(id)
    
    def get_all(self):
        return self.model.get_all()
    
    def create(self, data:EmployeeEntity):
        birthday = datetime.strptime(data.birthday, '%Y-%m-%d').date()
        employe = Employee(data.id, data.name, data.gender, data.birthday, data.created_at, data.updated_at)
        employe.register_employee()
        return True
    
    def update(self, id, data):
        return self.model.update(id, data)
    
    def delete(self, id):
        return self.model.delete(id)