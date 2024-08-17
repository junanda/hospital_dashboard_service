from flask import Flask
from flask_migrate import Migrate
from ...configuration.database.postgree import Postgree
from ...controller.auth_controller import auth
from ...controller.appointment_controller import appointment
from ...controller.doctor_controller import doctor
from ...controller.patient_controller import patient
from ...controller.employee_controller import employee
from ...configuration.config import ConfigEnvironment

def create_app():
    config = ConfigEnvironment()
    app = Flask(__name__)
    app.config.from_object(__name__)

    database = Postgree(config)
    database.connect(app)
    db = database.get_connection(app)

    migrate = Migrate(app, db)
    migrate.init_app(app)

    with app.app_context():
        database.create_tables()
    
    app.register_blueprint(auth)
    app.register_blueprint(appointment)
    app.register_blueprint(doctor)
    app.register_blueprint(patient)
    app.register_blueprint(employee)
   
    return app