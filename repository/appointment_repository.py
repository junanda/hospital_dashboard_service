from ..models.appointment import Appointment
from ..configuration.database.postgree import db
from datetime import datetime as tim
import logging

logger = logging.getLogger(__name__)

class AppointmentRepository:
    def __init__(self):
        pass

    def get_by_id(self, id):
        result = Appointment.query.filter_by(id=id).first()
        return result
    
    def get_all(self):
        result = Appointment.query.all()
        return result
    
    def create(self, data):
        req_appointment = Appointment(data.id_patient, data.id_doctor, data.datetime, data.status, data.diagnose, data.notes, tim.now(), tim.now())
        try:
            db.session.add(req_appointment)
            db.session.commit()
            logger.info(f'Appointment created: {req_appointment.id}')
        except Exception as e:
            db.session.rollback() 
            logger.error(f'Error create appointment: {e}')
            return False
        return True
    
    def update(self, id, data):
        try:
            appointment = Appointment.query.filter_by(id=id).first()
            appointment.patient_id = data.id_patient
            appointment.doctor_id = data.id_doctor
            appointment.datetime = data.datetime
            appointment.status = data.status
            appointment.diagnose = data.diagnose
            appointment.notes = data.notes
            appointment.updated_at = tim.now()

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error update appointment: {e}')
            return False
        return True
    
    def delete(self, id):
        try:
            appointment = Appointment.query.filter_by(id=id).first()
            db.session.delete(appointment)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error delete appointment: {e}')
            return False, 'failed'
        return True, None
    
    def update_status(self, id, status):
        try:
            appointment = Appointment.query.filter_by(id=id).first()
            appointment.status = status
            appointment.updated_at = tim.now()

            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.error(f'Error update appointment: {e}')
            return False
        return True
    
    def get_by_date(self, doctor_id, datetime):
        result = Appointment.query.filter_by(doctor_id=doctor_id, datetime=datetime, status='in_queue').first()
        return result
    
    def get_by_patient(self, patient_id):
        result = Appointment.query.filter_by(patient_id=patient_id).all()
        return result
    
    def get_appointment_resgistered_last(self, patient_id, docktor_id, datetime):
        result = Appointment.query.filter_by(patient_id=patient_id, doctor_id=docktor_id, datetime=datetime, status='in_queue').first()
        return result