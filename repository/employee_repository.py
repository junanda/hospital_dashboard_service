import logging
from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from ..models.employee import Employee
from ..models.user import User
from ..entity.employee import Employee as EmployeeEntity
from ..configuration.database.postgree import db

logger = logging.getLogger(__name__)

class EmployeeRepository:
    def __init__(self):
        pass

    def get_by_id(self, id:str):
        try:
            employee = Employee.query.filter_by(id=id).first()
            return employee
        except NoResultFound as e:
            logger.error(f'Error get employee: {e}')
            return None
    
    def get_all(self):
        emp_all = Employee.query.all()
        return emp_all
    
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
        try:
            employee = Employee.query.filter_by(id=id).first()
            employee.name = data.name
            employee.gender = data.gender
            employee.birthday = datetime.strptime(data.birthday, '%Y-%m-%d').date()
            employee.updated_at = datetime.now()

            db.session.commit()
        except NoResultFound as e:
            logger.info(f'Employee not found: {e}')
            return False
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error update employee: {e}')
            return False
        return True
    
    def delete(self, id):
        try:
            employee = Employee.query.filter_by(id=id).first()
            user = User.query.filter_by(id_trace=id).first()
            db.session.delete(employee)
            db.session.delete(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error delete employee: {e}')
            return False, 'not_found'
        return True, None