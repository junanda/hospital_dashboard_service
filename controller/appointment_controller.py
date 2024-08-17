from flask import Blueprint, request

appointment = Blueprint('appointment', __name__, url_prefix='/appointments')

@appointment.route('/', methods=['GET'])
def index():
    return "welcome"

@appointment.route('/', methods=['POST'])
def register():
    return "registrasi appointment"

@appointment.route('/<string:id>', methods=['GET'])
def get_by_id(id):
    return "detail appointment " + id

@appointment.route('/<string:id>', methods=['PUT'])
def update(id):
    return "update " + id

@appointment.route('/<string:id>', methods=['DELETE'])
def delete(id):
    return "delete " + id