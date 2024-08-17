from flask import Blueprint, request
from flask_pydantic import validate
from ..entity.employee import RegisterEmployee
from ..service.employee_service import EmployeeService

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
    es = EmployeeService()
    result = es.create(body)
    return body

@employee.route('/<string:id>', methods=['PUT'])
def update(id):
    return "update " + id

@employee.route('/<string:id>', methods=['DELETE'])
def delete(id):
    return "delete " + id