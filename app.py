from .cmd.api.server import create_app
from .models.employee import Employee
from .models.user import User
from .models.doctor import Doctors
from .models.appointment import Appointment
from .models.patient import Patients

if __name__ == '__main__':
    app = create_app()

    app.run(debug=True)