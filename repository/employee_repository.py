import logging
from flask import Response, abort
from datetime import datetime
from ..models.employee import Employee
from ..models.user import User
from ..entity.employee import Employee as EmployeeEntity
from ..configuration.database.postgree import db

logger = logging.getLogger(__name__)

class EmployeeRepository:
    def __init__(self):
        pass

    def get_by_id(self, id:str):

        return self.model.get_by_id(id)
    
    def get_all(self):
        return self.model.get_all()
    
    def create(self, data:EmployeeEntity):
        birthday = datetime.strptime(data.birthday, '%Y-%m-%d').date()
        employe = Employee(data.id, data.name, data.gender, birthday, data.created_at, data.updated_at)
        user = User(data.id, data.username, data.password, data.role, data.created_at, data.updated_at)
        try:
            db.session.add(employe)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback() 
            logger.error(f'Error create employee: {e}')
            return False, 'Failed to create employee'
        return True, None
    
    def update(self, id, data):
        return self.model.update(id, data)
    
    def delete(self, id):
        return self.model.delete(id)