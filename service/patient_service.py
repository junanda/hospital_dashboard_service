from ..repository.patient_repository import PatientRepository
from ..repository.appointment_repository import AppointmentRepository
from ..entity.patient import ResponsePatient
from ..entity.appointment import AppointmentResult

class PatientService:
    def __init__(self):
        pass

    def get_by_id(self, id):
        result = PatientRepository().get_by_id(id)
        appoint_data = []
        if result is not None:
            appoint_patient = AppointmentRepository().get_by_patient(id)
            if len(appoint_patient) > 0:
                appoint_data = [AppointmentResult(
                    id_appointment=row.id, id_patient=row.patient_id, id_doctor=row.doctor_id, datetime=str(row.datetime), status=row.status, diagnose=row.diagnose, notes=row.notes
                ) for row in appoint_patient]
            data = ResponsePatient(
                id_pasien=result.id,
                name=result.name,
                gender=result.gender,
                birthday=str(result.birthday),
                no_ktp=result.no_ktp,
                address=result.address,
                vaccine_type=result.vaccine_type,
                vaccine_count=result.vaccine_count,
                created_at=str(result.created_at),
                updated_at=str(result.updated_at),
                appointment= appoint_data
            ).model_dump()
            return data
        return result
    
    def get_all(self):
        result = []
        data = PatientRepository().get_all()
        if len(data) > 0:
            result = [ResponsePatient(
                id_pasien=row.id,
                name=row.name,
                gender=row.gender,
                birthday=str(row.birthday),
                no_ktp=row.no_ktp,
                address=row.address,
                vaccine_type=row.vaccine_type,
                vaccine_count=row.vaccine_count,
                created_at=str(row.created_at),
                updated_at=str(row.updated_at)
            ).model_dump() for row in data]
        return result
    
    def create(self, data):
        if len(data.no_ktp) != 16:
            return False, 'ktp_not_valid', None
        result = PatientRepository().get_by_ktp(data.no_ktp)
        if not result:
            result, err = PatientRepository().create(data)
            patRes = PatientRepository().get_by_ktp(data.no_ktp)
            data = ResponsePatient(
                id_pasien=patRes.id, name=patRes.name, gender=patRes.gender, birthday=str(patRes.birthday), no_ktp=patRes.no_ktp, address=patRes.address, vaccine_type=patRes.vaccine_type, vaccine_count=patRes.vaccine_count, created_at=str(patRes.created_at), updated_at=str(patRes.updated_at)
            ).model_dump()
            return result, err, data
        return False, 'failed', None
    
    def update(self, id, data):
        if len(data.no_ktp) != 16:
            return False, 'ktp_not_valid', None
        result = PatientRepository().update(id, data)
        if result: 
            pr = PatientRepository().get_by_id(id)
            data = ResponsePatient(
                id_pasien=pr.id, name=pr.name, gender=pr.gender, birthday=str(pr.birthday), no_ktp=pr.no_ktp, address=pr.address, vaccine_type=pr.vaccine_type, vaccine_count=pr.vaccine_count, created_at=str(pr.created_at), updated_at=str(pr.updated_at)
            ).model_dump()
            return result, None, data
        return result, 'failed', None
    
    def delete(self, id):
        result, err = PatientRepository().delete(id)
        return result, err