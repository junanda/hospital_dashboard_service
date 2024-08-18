from ..configuration.database.postgree import db

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

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'birthday': str(self.birthday),
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }

    def __repr__(self):
        return '<Employee %r>' % self.name
 
