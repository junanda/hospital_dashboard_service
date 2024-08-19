from pydantic import BaseModel
from datetime import datetime as tim
from enum import Enum

class Role(str, Enum):
    employee = 'employee'
    doctor = 'doctor'
    admin = 'admin'

class Employee(BaseModel):
    id: str
    name: str
    gender: str
    birthday: str
    created_at: tim
    updated_at: tim
    username: str
    password: str
    role: str

    class Config:
        from_attributes = True

class EmployeeResult(BaseModel):
    id: str
    name: str
    gender: str
    birthday: str
    created_at: str
    updated_at: str

    class config:
        from_attributes = True

class RegisterEmployee(BaseModel):
    name: str
    gender: str
    birthday: str
    username: str
    password: str
    role: Role

    class Config:
        from_attributes = True

class RequestUpdateEmployee(BaseModel):
    name: str
    gender: str
    birthday: str

    class Config:
        from_attributes = True