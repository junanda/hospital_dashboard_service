from flask import Blueprint, request, Response
from flask_pydantic import validate
from ..entity.patient import RequestPatient, RequestUpdatePatient
from ..service.patient_service import PatientService
from ..utils.utilities import authentication
import json

patient = Blueprint('patient', __name__, url_prefix='/patients')

@patient.route('/', methods=['GET'])
@authentication
def index():
    result = PatientService().get_all()
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'get all patient', 'data': result}))

@patient.route('/', methods=['POST'])
@authentication
@validate()
def register(body: RequestPatient):
    result, err, data = PatientService().create(body)
    if not result:
        return Response(status=500, mimetype='application/json', response=json.dumps({'status':'failed', 'message': err}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'create patient success', 'data': data}))

@patient.route('/<string:id>', methods=['GET'])
@authentication
def get_by_id(id):
    result = PatientService().get_by_id(id)
    if result is not None:
        return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'get patient success', 'data': result}))
    return Response(status=404, mimetype='application/json', response=json.dumps({'status':'failed', 'message': 'patient not found'}))

@patient.route('/<string:id>', methods=['PUT'])
@authentication
def update(id):
    data_req = RequestUpdatePatient(**request.get_json())
    result, _, data = PatientService().update(id, data_req)
    if not result:
        return Response(status=500, mimetype='application/json', response=json.dumps({'status':'failed', 'message': 'failed to update patient'}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'update patient success', 'data': data}))

@patient.route('/<string:id>', methods=['DELETE'])
@authentication
def delete(id):
    _, err = PatientService().delete(id)
    if err is not None:
        return Response(status=500, mimetype='application/json', response=json.dumps({'status':'failed', 'message': err}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'delete patient success'}))