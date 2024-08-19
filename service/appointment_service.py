from ..repository.appointment_repository import AppointmentRepository
from ..repository.doctor_repository import DoctorRepository
from ..entity.appointment import Appointment
from datetime import datetime as tim

class AppointmentService:
    def __init__(self):
        pass

    def get_by_id(self, id):
        result = AppointmentRepository().get_by_id(id)
        if result is not None:
            return Appointment(
                id_appointment=result.id,
                id_patient=result.patient_id,
                id_doctor=result.doctor_id,
                datetime=str(result.datetime),
                status=result.status,
                diagnose=result.diagnose,
                notes=result.notes,
                created_at=str(result.created_at),
                updated_at=str(result.updated_at)
            ).model_dump()
        return result
    
    def get_all(self):
        result = []
        data = AppointmentRepository().get_all()
        if len(data) > 0:
            result = [Appointment(
                id_appointment=row.id,
                id_patient=row.patient_id,
                id_doctor=row.doctor_id,
                datetime=str(row.datetime),
                status=row.status,
                diagnose=row.diagnose,
                notes=row.notes,
                created_at=str(row.created_at),
                updated_at=str(row.updated_at)
            ).model_dump() for row in data]
        return result
    
    def create(self, data):
        docter = DoctorRepository().get_by_id(data.id_doctor)
        ftime = tim.strptime(data.datetime, '%Y-%m-%d %H:%M:%S').time()

        if docter is None:
            return False, 'doctor_not_found', None
        
        if not str(docter.work_start_time) <= str(ftime) <= str(docter.work_end_time):
            return False, 'doctor_not_available', None

        result = AppointmentRepository().get_by_date(data.id_doctor, data.datetime)
        if result is not None:
            return False, 'appointment_exist', None
        
        result_c = AppointmentRepository().create(data)
        dt_appointment = AppointmentRepository().get_appointment_resgistered_last(data.id_patient, data.id_doctor, data.datetime)
        data = Appointment(
            id_appointment=dt_appointment.id, 
            id_patient=dt_appointment.patient_id, 
            id_doctor=dt_appointment.doctor_id, 
            datetime=str(dt_appointment.datetime), 
            status=dt_appointment.status, 
            diagnose=dt_appointment.diagnose, 
            notes=dt_appointment.notes, 
            created_at=str(dt_appointment.created_at), 
            updated_at=str(dt_appointment.updated_at)
        ).model_dump()
        return result_c, None, data
    
    def update(self, id, data):
        result = AppointmentRepository().update(id, data)
        if result:
            re = AppointmentRepository().get_by_id(id)
            data = Appointment(
                id_appointment=re.id, 
                id_patient=re.patient_id, 
                id_doctor=re.doctor_id, 
                datetime=str(re.datetime), 
                status=re.status, 
                diagnose=re.diagnose, 
                notes=re.notes, 
                created_at=str(re.created_at), 
                updated_at=str(re.updated_at)
            ).model_dump()
            return result, None, data
        return result, 'failed', None
    
    def delete(self, id):
        result, err = AppointmentRepository().delete(id)
        return result, err