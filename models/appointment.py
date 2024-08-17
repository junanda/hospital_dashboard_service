from ..configuration.database.postgree import db


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    patient_id = db.Column(db.Integer, nullable=False)
    doctor_id = db.Column(db.String(150), nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.Enum('in_queue', 'done', 'canceled',name="status_appointment"), nullable=False, default='in_queue')
    diagnose = db.Column(db.Text, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, patient_id, doctor_id, datetime, status, diagnose, notes, created_at, updated_at) -> None:
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.datetime = datetime
        self.status = status
        self.diagnose = diagnose
        self.notes = notes
        self.created_at = created_at
        self.updated_at = updated_at
    
    def get_by_id(self):
        db_appointment = Appointment.query.filter_by(Appointment.id==self.id).first()
        return db_appointment
    
    def __repr__(self) -> str:
        return '<Appointment %r>' % self.patient_id