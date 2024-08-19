from ..models.patient import Patients
from ..configuration.database.postgree import db
from sqlalchemy.orm.exc import NoResultFound
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class PatientRepository:
    def __init__(self):
        pass

    def get_by_id(self, id):
        result = Patients.query.filter_by(id=id).first()
        # medical history dari appointment
        return result
    
    def get_all(self):
        pat_all = Patients.query.all()
        return pat_all
    
    def get_by_ktp(self, no_ktp):
        result = Patients.query.filter_by(no_ktp=no_ktp).first()
        return result
    
    def create(self, data):
        birday = datetime.strptime(data.birthday, '%Y-%m-%d').date()
        patient = Patients(data.name, data.gender, birday, data.no_ktp, data.address, data.vaccine_type, data.vaccine_count, datetime.now(), datetime.now())
        try:
            db.session.add(patient)
            db.session.commit()
        except Exception as e:
            db.session.rollback() 
            logger.error(f'Error create patient: {e}')
            return False, 'failed'
        return True, None
    
    def update(self, id, data):
        birday = datetime.strptime(data.birthday, '%Y-%m-%d').date()
        try:
            patient = Patients.query.filter_by(id=id).first()
            patient.name = data.name
            patient.gender = data.gender
            patient.birthday = birday
            patient.no_ktp = data.no_ktp
            patient.address = data.address
            patient.updated_at = datetime.now()

            db.session.commit()
        except NoResultFound as e:
            logger.info(f'Patient not found: {e}')
            return False
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error update patient: {e}')
            return False
        return True
    
    def delete(self, id):
        try:
            patient = Patients.query.filter_by(id=id).first()
            db.session.delete(patient)
            db.session.commit()
        except Exception as e:
            logger.info(f'Patient not found: {e}')
            return False, 'not found'
        return True, None