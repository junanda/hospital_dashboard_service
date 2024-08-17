from flask import Blueprint, request

patient = Blueprint('patient', __name__, url_prefix='/patients')

@patient.route('/', methods=['GET'])
def index():
    return "welcome"

@patient.route('/', methods=['POST'])
def register():
    return "welcome post"

@patient.route('/<string:id>', methods=['GET'])
def get_by_id(id):
    return "detail" + id

@patient.route('/<string:id>', methods=['PUT'])
def update(id):
    return "update " + id

@patient.route('/<string:id>', methods=['DELETE'])
def delete(id):
    return "delete " + id