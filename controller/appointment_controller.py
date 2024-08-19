from flask import Blueprint, request, Response
from flask_pydantic import validate
from ..entity.appointment import RequestAppointment, RequestUpdateAppointment
from ..service.appointment_service import AppointmentService
import json


appointment = Blueprint('appointment', __name__, url_prefix='/appointments')

@appointment.route('/', methods=['GET'])
def index():
    result = AppointmentService().get_all()
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'get all appointment', 'data': result}))

@appointment.route('/', methods=['POST'])
@validate()
def register(body: RequestAppointment):
    result, err, data = AppointmentService().create(body)
    if not result:
        return Response(status=500, mimetype='application/json', response=json.dumps({'status':'failed', 'message': err}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'create appointment success', 'data': data}))

@appointment.route('/<string:id>', methods=['GET'])
def get_by_id(id):
    result = AppointmentService().get_by_id(id)
    if result is not None:
        return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'get appointment success', 'data': result}))
    return Response(status=404, mimetype='application/json', response=json.dumps({'status':'failed', 'message': 'appointment not found'}))

@appointment.route('/<string:id>', methods=['PUT'])
def update(id):
    data = RequestUpdateAppointment(**request.get_json())
    result, _, data = AppointmentService().update(id, data)
    if not result:
        return Response(status=500, mimetype='application/json', response=json.dumps({'status':'failed', 'message': 'failed to update appointment'}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'update appointment success', 'data': data}))

@appointment.route('/<string:id>', methods=['DELETE'])
def delete(id):
    _, err = AppointmentService().delete(id)
    if err is not None:
        return Response(status=500, mimetype='application/json', response=json.dumps({'status':'failed', 'message': err}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'delete appointment success'}))