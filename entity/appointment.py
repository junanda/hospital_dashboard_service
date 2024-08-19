from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from enum import Enum

class Status(str, Enum):
    waiting = 'in_queue'
    done = 'done'
    canceled = 'canceled'

class Appointment(BaseModel):
    id_appointment: int
    id_patient: int
    id_doctor: str
    datetime: str
    status: Optional[Status] = None
    diagnose: str
    notes: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True

class AppointmentResult(BaseModel):
    id_appointment: int
    id_patient: int
    id_doctor: str
    datetime: str
    status: Optional[Status] = None
    diagnose: str
    notes: str

    class Config:
        from_attributes = True

class RequestAppointment(BaseModel):
    id_patient: int
    id_doctor: str
    datetime: str
    status: Optional[Status] = None
    diagnose: str
    notes: str

    class Config:
        from_attributes = True

class RequestUpdateAppointment(BaseModel):
    id_patient: int
    id_doctor: str
    datetime: str
    status: Optional[Status] = None
    diagnose: str
    notes: str

    class Config:
        from_attributes = True