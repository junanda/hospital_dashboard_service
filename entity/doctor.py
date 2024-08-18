from pydantic import BaseModel, field_validator
from datetime import datetime, time
from .employee import Role

class Doctors(BaseModel):
    id: str
    name: str
    gender: str
    birthday: str
    created_at: datetime
    updated_at: datetime
    username: str
    password: str
    work_start_time: time
    work_end_time: time
    role: str

    class Config:
        from_attributes = True

class DoctorResult(BaseModel):
    id: str
    name: str
    gender: str
    birthday: str
    created_at: str
    updated_at: str
    work_start_time: str
    work_end_time: str

    class config:
        from_attributes = True

class RequestRegistrationDoctor(BaseModel):
    name: str
    gender: str
    birthday: str
    username: str
    password: str
    work_start_time: str
    work_end_time: str
    role: Role


    class Config:
        from_attributes = True

class RequestUpdateDoctor(BaseModel):
    name: str
    gender: str
    birthday: str
    work_start_time: time
    work_end_time: time

    class Config:
        from_attributes = True