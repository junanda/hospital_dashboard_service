from pydantic import BaseModel, field_validator
from datetime import datetime, time
from .employee import Role
from ..repository.user_repository import UserRepository

class Docters(BaseModel):
    id: int
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

class RegistrasiDoctor(BaseModel):
    name: str
    gender: str
    birthday: str
    username: str
    password: str
    work_start_time: time
    work_end_time: time
    role: Role

    @field_validator('work_start_time', 'work_end_time')
    def work_start_time_less_than_work_end_time(cls, v, values):
        if values['work_start_time'] >= values['work_end_time']:
            raise ValueError('work_start_time must be less than work_end_time')
        return v
    
    @field_validator('username')
    def validate_username(cls, v):
        user = UserRepository().get_by_username(v)
        if user is not None:
            raise ValueError('username already exists')
        return v

    class Config:
        from_attributes = True

class RequestUpdateDoctor(BaseModel):
    name: str
    gender: str
    birthday: datetime
    work_start_time: time
    work_end_time: time

    @field_validator('work_start_time', 'work_end_time')
    def work_start_time_less_than_work_end_time(cls, v, values):
        if values['work_start_time'] >= values['work_end_time']:
            raise ValueError('work_start_time must be less than work_end_time')
        return v

    class Config:
        from_attributes = True