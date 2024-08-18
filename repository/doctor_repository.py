from ..models.doctor import Doctors
from ..models.user import User
from ..entity.doctor import Doctors as DoctersEntity
from ..configuration.database.postgree import db
from datetime import datetime as datetime
from sqlalchemy.orm.exc import NoResultFound
import logging

logger = logging.getLogger(__name__)

class DoctorRepository:
    def __init__(self):
        pass

    def get_by_id(self, id):
        result = Doctors.query.filter_by(id=id).first()
        return result
    
    def get_all(self):
        result = Doctors.query.all()
        return result
    
    def create(self, data: DoctersEntity):
        birthday = datetime.strptime(data.birthday, '%Y-%m-%d').date()
        doctor = Doctors(data.id, data.name, data.gender, birthday, data.work_start_time, data.work_end_time, data.created_at, data.updated_at)
        user = User(data.id, data.username, data.password, data.role, data.created_at, data.updated_at)
        try:
            db.session.add(doctor)
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback() 
            logger.error(f'Error create doctor: {e}')
            return False, 'failed'
        return True, None
    
    def update(self, id, data):
        try:
            doctor = Doctors.query.filter_by(id=id).first()
            doctor.name = data.name
            doctor.gender = data.gender
            doctor.birthday = datetime.strptime(data.birthday, '%Y-%m-%d').date()
            doctor.work_start_time = data.work_start_time
            doctor.work_end_time = data.work_end_time
            doctor.updated_at = datetime.now()

            db.session.commit()
        except NoResultFound as e:
            db.session.rollback()
            logger.info(f'Doctor not found: {e}')
            return False, 'not_found'
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error update doctor: {e}')
            return False, 'failed'
        return True, None
    
    def delete(self, id):
        try:
            doctor = Doctors.query.filter_by(id=id).first()
            db.session.delete(doctor)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error delete doctor: {e}')
            return False, 'not_found'
        return True, None