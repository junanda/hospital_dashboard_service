from ..configuration.database.postgree import db

class Doctors(db.Model):
    id = db.Column(db.String(150), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(12), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    work_start_time = db.Column(db.Time, nullable=False)
    work_end_time = db.Column(db.Time, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, id, name, gender, birthday, work_start_time, work_end_time, created_at, updated_at) -> None:
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.work_start_time = work_start_time
        self.work_end_time = work_end_time
        self.created_at = created_at
        self.updated_at = updated_at
    
    def get_by_id(self):
        db_doctor = Doctors.query.filter_by(Doctors.id==self.id).first()
        return db_doctor
    
    def __repr__(self) -> str:
        return '<Doctor %r>' % self.name