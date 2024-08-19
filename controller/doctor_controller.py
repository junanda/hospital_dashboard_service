from flask import Blueprint, request, Response
from flask_pydantic import validate
from ..service.doctor_service import DoctorService
from ..entity.doctor import RequestRegistrationDoctor, RequestUpdateDoctor
from ..utils.utilities import error_number, message_error, authentication
import json

doctor = Blueprint('doctor', __name__, url_prefix='/doctors')

@doctor.route('/', methods=['GET'])
@authentication
def index():
    result = DoctorService().get_all()
    return Response(
        status=200, 
        mimetype='application/json', 
        response=json.dumps({'status':'success', 'message': 'get all doctor success', 'data': result})
        )

@doctor.route('/', methods=['POST'])
@authentication
@validate()
def register(body: RequestRegistrationDoctor):
    result, err, data = DoctorService().create(body)
    if not result:
        return Response(status=error_number('bad_request'), mimetype='application/json', response=json.dumps({'status':'failed', 'message': message_error(err, 'create')}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'create doctor success', 'data': data}))

@doctor.route('/<string:id>', methods=['GET'])
@authentication
def get_by_id(id):
    result = DoctorService().get_by_id(id)
    if result is not None:
        return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'get doctor success', 'data': result}))
    return Response(status=error_number('bad_request'), mimetype='application/json', response=json.dumps({'status':'failed', 'message': 'doctor not found'}))

@doctor.route('/<string:id>', methods=['PUT'])
@authentication
@validate()
def update(id:str):
    data = RequestUpdateDoctor(**request.get_json())
    result, data, err = DoctorService().update(id, data)
    if not result:
        return Response(status=error_number('bad_request'), mimetype='application/json', response=json.dumps({'status':'failed', 'message': message_error(err, 'update')}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'update doctor success', 'data': data}))

@doctor.route('/<string:id>', methods=['DELETE'])
@authentication
def delete(id):
    _, err = DoctorService().delete(id)
    if err is not None:
        return Response(status=error_number(err), mimetype='application/json', response=json.dumps({'status':'failed', 'message': message_error(err, 'delete')}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'delete doctor success'}))