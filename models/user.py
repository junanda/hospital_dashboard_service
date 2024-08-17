from ..configuration.database.postgree import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_trace = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    role = db.Column(db.Enum('admin', 'doctor', 'employee', name='role_user'), nullable=False, default='employee')
    created_at = db.Column(db.DateTime, nullable=False)
    updated_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_trace, username, password, role, created_at, updated_at):
        self.id_trace = id_trace
        self.username = username
        self.password = password
        self.role = role
        self.created_at = created_at
        self.updated_at = updated_at

    def get_by_idtrace(self):
        db_user = User.query.filter_by(User.id_trace==self.id_trace).first()
        return db_user
    
    def create(self):
        db.session.add(self)
        db.session.commit()
        return True
    
    def __repr__(self):
        return '<User %r>' % self.username