from flask import Blueprint, Response, request
from flask_pydantic import validate
from ..entity.employee import RegisterEmployee, RequestUpdateEmployee
from ..service.employee_service import EmployeeService
from ..utils.utilities import error_number, message_error, authentication
import json

employee = Blueprint('employee', __name__, url_prefix='/employees')

@employee.route('/', methods=['GET'])
@authentication
def index():
    result = EmployeeService().get_all()
    return Response(status=200, mimetype='application/json', response=json.dumps(
        {'status':'success', 
         'message': 'get all employee success', 
         'data': result
         }
    ))

@employee.route('/<string:id>', methods=['GET'])
@authentication
def get_by_id(id):
    result = EmployeeService().get_by_id(id)
    if result is not None:
        return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'get employee success', 'data': result}))
    return Response(status=404, mimetype='application/json', response=json.dumps({'status':'failed', 'message': 'employee not found'}))

@employee.route('/', methods=['POST'])
@authentication
@validate()
def register(body: RegisterEmployee):
    codeError = 500
    es = EmployeeService()
    result, err, data = es.create(body)
    if err == 'Username already exists':
            codeError = 400
    if not result:
        return Response(status=codeError, mimetype='application/json', response=json.dumps({'status':'failed','message': err}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'create employee success', 'data': data}))

@employee.route('/<string:id>', methods=['PUT'])
@authentication
@validate()
def update(id:str):
    data = RequestUpdateEmployee(**request.get_json())
    result, data = EmployeeService().update(id, data)
    if not result:
        return Response(status=400, mimetype='application/json', response=json.dumps({'status':'failed', 'message': 'failed to update employee'}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'update employee success', 'data': data}))

@employee.route('/<string:id>', methods=['DELETE'])
@authentication
def delete(id):
    if not id:
        return Response(status=error_number('not_found'), mimetype='application/json', response=json.dumps({'status':'failed', 'message': 'Employee not found'}))
    _, err = EmployeeService().delete(id)
    if err is not None:
        return Response(status=error_number(err), mimetype='application/json', response=json.dumps({'status':'failed', 'message': message_error(err, 'delete')}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'delete employee success'}))
    