from flask import Blueprint, jsonify, Response
from flask_pydantic import validate
from ..entity.employee import RegisterEmployee
from ..service.employee_service import EmployeeService
import json

employee = Blueprint('employee', __name__, url_prefix='/employees')

@employee.route('/', methods=['GET'])
def index():
    return "welcome"

@employee.route('/<string:id>', methods=['GET'])
def get_by_id(id):
    return "detail employee " + id

@employee.route('/', methods=['POST'])
@validate()
def register(body: RegisterEmployee):
    codeError = 500
    es = EmployeeService()
    result, err = es.create(body)
    if err == 'Username already exists':
            codeError = 400
            
    if not result:
        return Response(status=codeError, mimetype='application/json', response=json.dumps({'status':'failed','message': err}))
    return Response(status=200, mimetype='application/json', response=json.dumps({'status':'success', 'message': 'create employee success'}))

@employee.route('/<string:id>', methods=['PUT'])
def update(id):
    return "update " + id

@employee.route('/<string:id>', methods=['DELETE'])
def delete(id):
    return "delete " + id