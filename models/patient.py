from ..configuration.database.postgree import db

class Patients(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(12), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    no_ktp = db.Column(db.String(20), nullable=False)
    address = db.Column(db.Text, nullable=False)
    vaccine_type = db.Column(db.String(80), nullable=True)
    vaccine_count = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, name, gender, birthday, no_ktp, address, vaccine_type, vaccine_count, created_at, updated_at) -> None:
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.no_ktp = no_ktp
        self.address = address
        self.vaccine_type = vaccine_type
        self.vaccine_count = vaccine_count
        self.created_at = created_at
        self.updated_at = updated_at
    

    def get_by_id(self):
        db_patient = Patients.query.filter_by(Patients.id==self.id).first()
        return db_patient
    
    def __repr__(self) -> str:
        return '<Patient %r>' % self.name