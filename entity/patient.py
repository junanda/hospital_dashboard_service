from pydantic import BaseModel, field_validator, constr
from typing import Optional
import string

class Patient(BaseModel):
    id: int
    name: str
    gender: str
    birthday: str
    no_ktp: str
    address: str
    vaccine_type: Optional[str] = None
    vaccine_count: Optional[str] = None
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True

class RequestPatient(BaseModel):
    name: str
    gender: str
    birthday: str
    no_ktp: Optional[constr(min_length=16, max_length=16)]
    address: str
    vaccine_type: Optional[str] = None
    vaccine_count: Optional[str] = None

    class Config:
        from_attributes = True

class ResponsePatient(BaseModel):
    id_pasien: int
    name: str
    gender: str
    birthday: str
    no_ktp: str
    address: str
    vaccine_type: Optional[str] = None
    vaccine_count: Optional[str] = None
    created_at: str
    updated_at: str
    appointment: Optional[list] = None

    class Config:
        from_attributes = True

class RequestUpdatePatient(BaseModel):
    name: str
    gender: str
    birthday: str
    no_ktp: Optional[constr(min_length=16, max_length=16)]
    address: str

    class Config:
        from_attributes = True