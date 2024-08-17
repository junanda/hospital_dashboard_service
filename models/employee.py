from ..configuration.database.postgree import db
from .user import User

class Employee(db.Model):
    id = db.Column(db.String(150), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(12), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, id, name, gender, birthday, created_at, updated_at) -> None:
        self.id = id
        self.name = name
        self.gender = gender
        self.birthday = birthday
        self.created_at = created_at
        self.updated_at = updated_at

    def register_employee(self):
        db.session.add(self)
        db.session.commit()
        return True
    
    def get_by_id(self):
        db_employee = Employee.query.filter_by(Employee.id==self.id).first()
        return db_employee

    def __repr__(self):
        return '<Employee %r>' % self.name
 
