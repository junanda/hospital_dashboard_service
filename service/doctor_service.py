from ..repository.doctor_repository import DoctorRepository
from ..repository.user_repository import UserRepository
from ..entity.doctor import DoctorResult, Doctors as DoctorsEntity
from ..utils.utilities import hashing_password, generate_id
from datetime import datetime as tim

class DoctorService:
    def __init__(self):
        pass

    def get_by_id(self, id):
        result = DoctorRepository().get_by_id(id)
        if result is not None:
            return DoctorResult(
                id=result.id, 
                name=result.name, 
                gender=result.gender, 
                birthday=str(result.birthday), 
                work_start_time=str(result.work_start_time),
                work_end_time=str(result.work_end_time),
                created_at=str(result.created_at), 
                updated_at=str(result.updated_at)
                ).model_dump()
        return result

    def get_all(self):
        result = []
        doctors = DoctorRepository().get_all()
        if len(doctors) > 0:
            result = [DoctorResult(
                id=doc.id, 
                name=doc.name, 
                gender=doc.gender, 
                birthday=str(doc.birthday), 
                created_at=str(doc.created_at), 
                updated_at=str(doc.updated_at),
                work_start_time=str(doc.work_start_time),
                work_end_time=str(doc.work_end_time)
                ).model_dump() for doc in doctors]

        return result
    
    def create(self, data):
        result = False
        err = 'username_already_exists'

        if data.work_start_time > data.work_end_time:
            return result, 'greater_than', None

        pass_hash = hashing_password(data.password)
        dataDoctor = DoctorsEntity(
            id=generate_id(data.username), 
            name=data.name, 
            gender=data.gender, 
            birthday=data.birthday, 
            created_at=tim.now(), 
            updated_at=tim.now(),
            work_start_time=data.work_start_time,
            work_end_time=data.work_end_time, 
            username=data.username, 
            password=pass_hash,
            role=data.role
            )
        
        userCheck = UserRepository().get_by_username(data.username)
        if not userCheck:
            result, err = DoctorRepository().create(dataDoctor)
            doc_result = DoctorRepository().get_by_id(dataDoctor.id)
            data = DoctorResult(
                id=doc_result.id, 
                name=doc_result.name, 
                gender=doc_result.gender, 
                birthday=str(doc_result.birthday), 
                created_at=str(doc_result.created_at), 
                updated_at=str(doc_result.updated_at),
                work_start_time=str(doc_result.work_start_time),
                work_end_time=str(doc_result.work_end_time)
                )
            return result, err, data.model_dump()
        return result, err, None
    
    def update(self, id, data):
        result = False
        if data.work_start_time > data.work_end_time:
            return result, None, 'greater_than'
        
        result, err = DoctorRepository().update(id, data)
        if result:
            se = DoctorRepository().get_by_id(id)
            data = DoctorResult(
                id=se.id, 
                name=se.name, 
                gender=se.gender, 
                birthday=str(se.birthday), 
                created_at=str(se.created_at), 
                updated_at=str(se.updated_at),
                work_start_time=str(se.work_start_time),
                work_end_time=str(se.work_end_time)
                ).model_dump()
            return result, data, err
        return result, None, err
    
    def delete(self, id):
        result, err = DoctorRepository().delete(id)
        return result, err