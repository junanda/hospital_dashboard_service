from flask_sqlalchemy import SQLAlchemy
from .database import DatabaseInterface
from ...configuration.config import ConfigEnvironment


db = SQLAlchemy()

class Postgree(DatabaseInterface):
    def __init__(self, config: ConfigEnvironment):
        super().__init__(
            host_db=config.getHostDB(),
            port_db=config.getPortDB(),
            user_db=config.getUserDB(),
            pass_db=config.getPassDB(),
            nama_db=config.getNamaDB()
        )

    def connect(self, app):
        if not self.connection:
            connection_string = f"postgresql://{self.user_db}:{self.pass_db}@{self.host_db}:{self.port_db}/{self.nama_db}"
            
            app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
            app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
            
            db.init_app(app)
            self.connection = db

    def close(self):
        if self.connection:
            self.connection.session.close_all()
            self.connection = None

    def get_connection(self, app):
        if not self.connection:
            self.connect(app=app)
        return self.connection
    
    def create_tables(self):
        db.create_all()
